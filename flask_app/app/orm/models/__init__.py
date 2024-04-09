# -*- coding: UTF-8 -*-
"""
Models - Initializer
================================================================================
This module contains the base entity mixin class that defines all the audit attributes for the database tables
"""
__author__ = "jadikesavan1@sheffield.ac.uk"

import logging

from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, TIMESTAMP, BOOLEAN, VARCHAR
from sqlalchemy.exc import MultipleResultsFound
from sqlalchemy.sql import func
from sqlalchemy_serializer import SerializerMixin

from app.errors.exceptions import AppError
from app.messages.error import UNKNOWN_ERROR
from app.messages.error.orm import ORMErrors
from app.utils.orm import get_username

LOGGER = logging.getLogger(__name__)


class EntityMixin(SerializerMixin):
    """
    Mixin class which needs to be inherited by all the ORM classes in the application

    :ivar id: The primary key identifier
    :vartype id: :class:`sqlalchemy.dialects.mysql.types.BIGINT`

    :ivar created_by: The name of the user who created the record
    :vartype created_by: :class:`sqlalchemy.dialects.mysql.types.VARCHAR`

    :ivar created_on: The timestamp corresponding to the record entry
    :vartype created_on: :class:`sqlalchemy.dialects.mysql.types.TIMESTAMP`

    :ivar last_updated_by: The name of the user who last updated the record
    :vartype last_updated_by: :class:`sqlalchemy.dialects.mysql.types.VARCHAR`

    :ivar last_updated_on: The timestamp corresponding to the latest updation of record
    :vartype last_updated_on: :class:`sqlalchemy.dialects.mysql.types.TIMESTAMP`

    :ivar active: The boolean variable indicating if the record is active
    :vartype active: :class:`sqlalchemy.sql.sqltypes.BOOLEAN`
    """
    id = Column(BIGINT, primary_key=True, nullable=False)

    created_by = Column(VARCHAR(255), default=get_username, nullable=False)

    created_on = Column(TIMESTAMP, default=func.now())

    last_updated_by = Column(VARCHAR(255), default=get_username, nullable=False)

    last_updated_on = Column(TIMESTAMP, default=func.now(),
                             onupdate=func.now())

    active = Column(BOOLEAN, default=True)

    @classmethod
    def load_by_id(cls, pkey_id, session):

        try:
            qry = session.query.filter(cls.id == pkey_id)
            return qry.one_or_none()

        except MultipleResultsFound:
            LOGGER.error("Multiple results found for the give ID", extra={"id": pkey_id}, exc_info=True)
            raise AppError(*ORMErrors.MULTIPLE_RESULTS_FOUND)
        except Exception as ex:
            LOGGER.error("Unknown error! Could not be handled!", exc_info=True)
            raise AppError(*UNKNOWN_ERROR) from ex

    def save(self, session):
        session.add(self)

    def update(self, session):
        session.merge(self)

    def delete(self, session):
        self.active = False
        session.delete(self)
