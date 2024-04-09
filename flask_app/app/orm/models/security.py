# -*- coding: UTF-8 -*-
"""
Models - Security
================================================================================
This module contains all the ORM models for storing the information related to application security
"""
import logging

import sqlalchemy.orm
from flask_security.models.fsqla import UserMixin, RoleMixin
from sqlalchemy import Column, Table, ForeignKey, or_
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.exc import MultipleResultsFound, NoResultFound
from sqlalchemy.orm import relationship

from app import alchemy_fw
from app.errors.exceptions import AppError
from app.messages.error.orm import ORMErrors
from app.orm.models import EntityMixin

__author__ = "jadikesavan1@sheffield.ac.uk"

LOGGER = logging.getLogger(name=__name__)

# Table for storing the user-role association
user_role_table = Table(
    "user_role_table",
    alchemy_fw.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("role_id", ForeignKey("roles.id"))
)


class User(alchemy_fw.Model, EntityMixin, UserMixin):
    """
    ORM Class representing the user table for storing the security information pertaining to users

    :ivar email: The principal email of the user
    :vartype email: :class:`sqlalchemy.dialects.mysql.types.VARCHAR`

    :ivar username: The username of the user account
    :vartype username: :class:`sqlalchemy.dialects.mysql.types.VARCHAR`

    :ivar password: The secure password for the user
    :vartype password: :class:`sqlalchemy.dialects.mysql.types.VARCHAR`
    """
    __tablename__ = "users"

    email = Column(VARCHAR(255), unique=True, nullable=False, index=True)
    username = Column(VARCHAR(255), unique=True, nullable=False, index=True)
    password = Column(VARCHAR(255), nullable=False)

    roles = relationship("Role", secondary=user_role_table, backref="users")

    def to_dict(self, only=(), rules=(),
                date_format=None, datetime_format=None, time_format=None, tzinfo=None,
                decimal_format=None, serialize_types=None):
        return_dict = dict()
        return_dict["email"] = self.email
        return_dict["password"] = self.password
        return_dict["name"] = self.username

        return return_dict

    @classmethod
    def load_user_with_username(cls, username: str, session: sqlalchemy.orm.Session = alchemy_fw.session):
        """
        Class method to load the user with the chosen username

        :param username: The username chosen by the user
        :type username: str

        :param session: An SQLAlchemy session
        :type session: :class:`sqlalchemy.orm.Session`

        :return: An instance of user if username matches, None otherwise
        :rtype: Union[:class:`app.orm.models.security.User`, None]
        """
        try:
            return session.query(cls).filter(cls.username == username).one_or_none()
        except MultipleResultsFound:
            LOGGER.error("More than one record found for the username", exc_info=True, extra={"username": username})
            raise AppError(*ORMErrors.MULTIPLE_RESULTS_FOUND)
        except Exception as exc:
            LOGGER.error("Could not execute query", exc_info=True)
            raise AppError(*ORMErrors.QUERY_FAILED, data=exc.args) from exc

    @classmethod
    def load_users_as_dict(cls, session: sqlalchemy.orm.Session = alchemy_fw.session):
        """
        Class method to load the user records and return them as dictionary

        :param session: An SQLAlchemy session
        :type session: :class:`sqlalchemy.orm.Session`

        :return: A dictionary of records
        :rtype: dict
        """
        try:
            return_dict = dict()
            results = session.query(cls).all()

            for user in results:
                return_dict[user.username] = user

            return return_dict
        except NoResultFound:
            LOGGER.error("No results found", exc_info=True)
            raise AppError(*ORMErrors.NO_RESULTS_FOUND)
        except Exception as exc:
            LOGGER.error("Could not execute query", exc_info=True)
            raise AppError(*ORMErrors.QUERY_FAILED, data=exc.args) from exc

    @classmethod
    def load_app_users(cls, session: sqlalchemy.orm.Session = alchemy_fw.session):
        """
        Class method to load the application user and return them as list

        :param session: An SQLAlchemy session
        :type session: :class:`sqlalchemy.orm.Session`

        :return: A dictionary of records
        :rtype: list
        """
        try:
            return session.query(cls).join(user_role_table).join(Role).filter("USER" == Role.name).all()
        except Exception as exc:
            LOGGER.error("Could not execute query", exc_info=True)
            raise AppError(*ORMErrors.QUERY_FAILED, data=exc.args) from exc

    @classmethod
    def load_app_admins(cls, session: sqlalchemy.orm.Session = alchemy_fw.session):
        """
        Class method to load the application admins and return them as list

        :param session: An SQLAlchemy session
        :type session: :class:`sqlalchemy.orm.Session`

        :return: A list of records
        :rtype: list
        """
        try:
            return session.query(cls).join(user_role_table).join(Role).filter("ADMIN" == Role.name).all()
        except Exception as exc:
            LOGGER.error("Could not execute query", exc_info=True)
            raise AppError(*ORMErrors.QUERY_FAILED, data=exc.args) from exc

    @classmethod
    def load_staff(cls, session: sqlalchemy.orm.Session = alchemy_fw.session):
        """
        Class method to load the application user and return them as list

        :param session: An SQLAlchemy session
        :type session: :class:`sqlalchemy.orm.Session`

        :return: A dictionary of records
        :rtype: dict
        """
        try:
            cond = or_(Role.name == "LEVEL-1", Role.name == "LEVEL-2")
            return session.query(cls).join(user_role_table).join(Role).filter(cond).all()
        except Exception as exc:
            LOGGER.error("Could not execute query", exc_info=True)
            raise AppError(*ORMErrors.QUERY_FAILED, data=exc.args) from exc


class Role(alchemy_fw.Model, EntityMixin, RoleMixin):
    """
    ORM class representing the security roles that are permitted in the application

    :ivar name: The name of the security role
    :vartype name: :class:`sqlalchemy.dialects.mysql.types.VARCHAR`

    :ivar description: The human readable description of the role
    :vartype description: :class:`sqlalchemy.dialects.mysql.types.VARCHAR`
    """
    __tablename__ = "roles"

    name = Column(VARCHAR(255), unique=True, nullable=False)
    description = Column(VARCHAR(255))

    @classmethod
    def load_roles_as_dict(cls, session: sqlalchemy.orm.Session = alchemy_fw.session):
        """
        Method to load all the roles form the database and return as a dictionary

        :param session: An SQLAlchemy session
        :type session: :class:`sqlalchemy.orm.Session`

        :return: A dictionary of records
        :rtype: dict
        """
        try:
            return_dict = dict()
            results = session.query(cls).all()

            for role in results:
                return_dict[role.name] = role

            return return_dict
        except NoResultFound:
            LOGGER.error("No results found", exc_info=True)
            raise AppError(*ORMErrors.NO_RESULTS_FOUND)
        except Exception as exc:
            LOGGER.error("Could not execute query", exc_info=True)
            raise AppError(*ORMErrors.QUERY_FAILED, data=exc.args) from exc
