# -*- coding: UTF-8 -*-
"""
Controller - Security
================================================================================
This module contains the methods to process the requests pertaining to the security and authentication
"""
import json
import logging
import os.path

import sqlalchemy.orm
from flask import current_app as app
from sqlalchemy.exc import NoResultFound

from app import alchemy_fw
from app.errors.exceptions import AppError
from app.messages.error.controllers import SecurityMessages, INTERNAL_SERVER_ERROR
from app.messages.error.orm import ORMErrors
from app.orm.manager import get_session
from app.orm.models.security import User, Role

__author__ = "jadikesavan1@sheffield.ac.uk"

LOGGER = logging.getLogger(__name__)

DATA_FOLDER = "data"
ROLES_JSON = "role_list.json"


def create_app_admin():
    """
    Method to create the application admin

    :return: Nothing
    :rtype: None
    """
    # Query the existing user records as dictionary
    users_dict = User.load_users_as_dict(session=alchemy_fw.session)

    # If the user is not present in the dictionary / records, create the user
    # This is to create the application admin only once during the application startup
    if app.config["APP_ADMIN_USERNAME"] not in users_dict.keys():
        admin_user = User()
        admin_user.email = app.config["APP_ADMIN_EMAIL"]
        admin_user.username = app.config["APP_ADMIN_USERNAME"]
        admin_user.password = app.config["APP_ADMIN_PASSWORD"]

        # Work with SQLAlchemy session
        with get_session() as t_session:
            admin_user.save(session=t_session)
            add_role_to_user(user=app.config["APP_ADMIN_USERNAME"], role="ADMIN", session=t_session)


def populate_roles():
    """
    Method to create the roles of the application as database entries

    :return: Nothing
    :rtype: None
    """
    # Query the existing role records as dictionary
    roles_in_db = Role.load_roles_as_dict(session=alchemy_fw.session)

    # Find the configuration file that contains the list of all the roles
    role_fp = os.path.join(app.instance_path, DATA_FOLDER, ROLES_JSON)
    # Open the config file
    with open(role_fp, "r") as fp:
        role_dict = json.load(fp=fp)

    for role in role_dict:
        # If the role is not present in the dictionary / records, create the role entry
        # This is to detect role changes that need to be updated in the database
        if role["name"] not in roles_in_db.keys():
            new_role = Role()
            new_role.name = role["name"]
            new_role.description = role["desc"]

            # Work with SQLAlchemy session
            with get_session() as t_session:
                new_role.save(session=t_session)


def create_user(email, username, password, role="USER"):
    """
    Method to create a user in the database

    :param email: The email of the user
    :type email: str

    :param username: The username chosen by the user
    :type username: str

    :param password: The secret authentication password chosen by the user
    :type password: str

    :param role: The role assigned to the user
    :type role: str

    :return: A boolean value indicating if the user creation is successful
    :rtype: bool
    """
    try:
        user = find_user(user=username)

        if user is not None:
            raise AppError(*SecurityMessages.USERNAME_TAKEN)

        user = User()
        user.username = username
        user.email = email
        user.password = password

        with get_session() as t_session:
            user.save(session=t_session)
            add_role_to_user(user=user.username, role=role, session=t_session)


    except Exception as exc:
        raise AppError(*INTERNAL_SERVER_ERROR) from exc


def add_role_to_user(user: "User", role: str, session: sqlalchemy.orm.Session = alchemy_fw.session) -> bool:
    """
    Method to add a role to a user. This means that the user is associated with a role authorizing him to use the
    intended role

    :param user: The user to manipulate.
    :type user: :class:`app.orm.models.security.User`

    :param role: The role to add to the user
    :type role: str

    :return: True is role was added, False if role already existed.
    :rtype: bool
    """
    role_obj = find_role(role)
    user = find_user(user)
    if not role_obj:
        raise AppError(*ORMErrors.NO_RESULTS_FOUND)
    if role_obj not in user.roles:
        user.roles.append(role_obj)
        user.update(session=session)
        return True
    return False


def add_roles_to_user(username, roles):
    """
    Method to add roles to the user

    :param username: The username chosen by the user
    :type username: str

    :param roles: The list of roles to be associated
    :type roles: list

    :return: Nothing
    :rtype: None
    """
    try:
        user = find_user(user=username)

        for role in roles:
            role_obj = find_role(role)
            if role_obj not in user.roles:
                add_role_to_user(user=user.username, role=role, session=alchemy_fw.session)

        for role in user.roles:
            if role.name not in roles:
                remove_role_from_user(user=user, role=role.name, session=alchemy_fw.session)

        alchemy_fw.session.commit()

    except Exception as exc:
        raise AppError(*INTERNAL_SERVER_ERROR) from exc


def remove_role_from_user(user: "User", role: str, session: sqlalchemy.orm.Session = alchemy_fw.session) -> bool:
    """
    Removes a role from a user. This means that the user is dissociated with a role de-authorizing him to use the
    intended role

    :param user: The user to manipulate.
    :type user: :class:`app.orm.models.security.User`

    :param role: The role to add to the user
    :type role: str

    :return: True is role was removed, False otherwise
    :rtype: bool
    """
    rv = False
    role_obj = find_role(role)

    if not role_obj:
        raise AppError(*ORMErrors.NO_RESULTS_FOUND)

    if role_obj in user.roles:
        rv = True
        user.roles.remove(role_obj)
        user.update(session=session)
    return rv


def find_role(role):
    """
    Method to find the role in the database and return the Role object

    :param role: The name of the role to be searched
    :type role: str

    :return: An instance of the role if found, None otherwise
    :rtype: Union[:class:`app.orm.models.security.Role`, None]
    """
    try:
        return Role.query.filter_by(name=role).one_or_none()  # type: ignore
    except NoResultFound:
        LOGGER.error("No results found", exc_info=True)
        raise AppError(*ORMErrors.NO_RESULTS_FOUND)
    except Exception as exc:
        LOGGER.error("Could not execute query", exc_info=True)
        raise AppError(*ORMErrors.QUERY_FAILED, data=exc.args) from exc


def find_user(user):
    """
    Method to find the user in the database and return the User object

    :param user: The email of the user to be searched
    :type user: str

    :return: An instance of the user if found, None otherwise
    :rtype: Union[:class:`app.orm.models.security.User`, None]
    """
    try:
        return User.query.filter_by(username=user).one_or_none()  # type: ignore
    except NoResultFound:
        LOGGER.error("No results found", exc_info=True)
        raise AppError(*ORMErrors.NO_RESULTS_FOUND)
    except Exception as exc:
        LOGGER.error("Could not execute query", exc_info=True)
        raise AppError(*ORMErrors.QUERY_FAILED, data=exc.args) from exc


def login_user(username, password):
    """
    Method to authenticate user with the given credentials i.e., username and password

    :param username: The username chosen by the user at the time of registration
    :type username: str

    :param password: The password of the user
    :type password: str

    :return: A boolean value indicating if the user authentication is unsuccessful, the user object as dictionary
             otherwise
    :rtype: Union[bool, dict]
    """
    try:
        user = find_user(user=username)
        return_role = "USER"

        if user is None:
            raise AppError(*SecurityMessages.USER_NOT_FOUND)

        if user.password != password:
            return False

        for role in user.roles:
            return_role = role.name
        return {"role": return_role}
    except Exception as exc:
        raise AppError(*INTERNAL_SERVER_ERROR)


def roles_of_user(username):
    """
    Method to list the roles of the user

    :param username: The username chosen by the user
    :type username: str

    :return: A list of roles associated with the user
    :rtype: list
    """
    try:
        user = find_user(user=username)

        if user is None:
            raise AppError(*SecurityMessages.USER_NOT_FOUND)

        return_list = list()

        for role in user.roles:
            return_list.append(role.name)

        return return_list
    except Exception as exc:
        raise AppError(*INTERNAL_SERVER_ERROR)


def list_roles():
    """
    Method to list all the roles configured in the application

    :return: A list of roles
    :rtype: list
    """
    try:
        role_dict = Role.load_roles_as_dict(session=alchemy_fw.session)
        return list(role_dict.keys())
    except Exception as exc:
        raise AppError(*INTERNAL_SERVER_ERROR) from exc


def list_users():
    """
    Method to list all the users added in the application

    :return: A list of users
    :rtype: list
    """
    try:
        return_list = list()
        user_list = User.load_app_users(session=alchemy_fw.session)
        for value in user_list:
            user_val = value.to_dict()
            return_list.append(user_val)

        return return_list

    except Exception as exc:
        raise AppError(*INTERNAL_SERVER_ERROR) from exc


def list_staff():
    """
    Method to list all the staff added in the application

    :return: A list of staff
    :rtype: list
    """
    try:
        return_list = list()
        user_list = User.load_staff(session=alchemy_fw.session)
        for value in user_list:
            user_val = value.to_dict()
            user_val["level"] = value.roles[0].name
            return_list.append(user_val)

        return return_list

    except Exception as exc:
        raise AppError(*INTERNAL_SERVER_ERROR) from exc


def list_admins():
    """
    Method to list all the admins added in the application

    :return: A list of admins
    :rtype: list
    """
    try:
        return_list = list()
        user_list = User.load_app_admins(session=alchemy_fw.session)
        for value in user_list:
            user_val = value.to_dict()
            return_list.append(user_val)

        return return_list

    except Exception as exc:
        raise AppError(*INTERNAL_SERVER_ERROR) from exc


def edit_user_data(username, email=None, new_username=None):
    try:
        user = find_user(user=username)

        if user is None:
            raise AppError(*SecurityMessages.USER_NOT_FOUND)

        elif new_username is None and email:
            user.email = email

        elif email is None and new_username:
            user.username = new_username

        else:
            user.email = email
            user.username = new_username

        alchemy_fw.session.commit()

    except Exception as exc:
        raise AppError(*INTERNAL_SERVER_ERROR)


def delete_user_data(username):
    try:
        user = find_user(user=username)

        if user is None:
            raise AppError(*SecurityMessages.USER_NOT_FOUND)

        alchemy_fw.session.delete(user)
        alchemy_fw.session.commit()

    except Exception as exc:
        raise AppError(*INTERNAL_SERVER_ERROR)


def update_password(username, password, new_password):
    try:
        user = find_user(user=username)

        if user is None:
            raise AppError(*SecurityMessages.USER_NOT_FOUND)

        if user.password != password:
            raise AppError(*SecurityMessages.PASSWORD_MISMATCH)

        user.password = new_password
        alchemy_fw.session.commit()

    except Exception as exec:
        raise AppError(*INTERNAL_SERVER_ERROR)
