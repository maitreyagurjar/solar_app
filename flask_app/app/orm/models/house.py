# -*- coding: UTF-8 -*-
"""
Models - House
================================================================================
This module contains the ORM classes to store the house information in database
"""

import logging

from sqlalchemy import Column, UniqueConstraint
from sqlalchemy.dialects.mysql import VARCHAR, SMALLINT, DOUBLE
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm.session import Session

from app import alchemy_fw
from app.errors.exceptions import AppError
from app.messages.error.orm import ORMErrors
from app.orm.models import EntityMixin

__author__ = "jadikesavan1@sheffield.ac.uk"

LOGGER = logging.getLogger(name=__name__)


class HouseType(alchemy_fw.Model, EntityMixin):
    """
    ORM class representing various house types that are present in the UK

    :ivar name: The type of the house
    :vartype name: :class:`sqlalchemy.dialects.mysql.types.VARCHAR`

    :ivar no_of_rooms: The number of rooms (assumed for the house type)
    :vartype no_of_rooms: :class:`sqlalchemy.dialects.mysql.types.SMALLINT`

    :ivar no_of_people: The number of people living in the house
    :vartype no_of_people: :class:`sqlalchemy.dialects.mysql.types.SMALLINT`

    :ivar floor_area: The flooring area for the house (assumed for the house type)
    :vartype floor_area: :class:`sqlalchemy.dialects.mysql.types.DOUBLE`

    :ivar gas_usage: The energy consumed in usage of gas
    :vartype gas_usage: :class:`sqlalchemy.dialects.mysql.types.DOUBLE`

    :ivar electricity_usage: The energy consumed in usage of electricity
    :vartype electricity_usage: :class:`sqlalchemy.dialects.mysql.types.DOUBLE`

    :ivar gas_emissions: The CO2 emissions generated in gas consumption
    :vartype gas_emissions: :class:`sqlalchemy.dialects.mysql.types.DOUBLE`

    :ivar electricity_emissions: The CO2 emissions generated in electricity consumption
    :vartype electricity_emissions: :class:`sqlalchemy.dialects.mysql.types.DOUBLE`

    """
    __tablename__ = "house_type"
    __tableargs__ = UniqueConstraint("name", "no_of_rooms")

    name = Column(VARCHAR(64), unique=False, nullable=False)

    no_of_rooms = Column(SMALLINT, nullable=False)
    no_of_people = Column(SMALLINT, nullable=False)
    floor_area = Column(DOUBLE)

    gas_usage = Column(DOUBLE)
    electricity_usage = Column(DOUBLE)

    gas_emissions = Column(DOUBLE)
    electricity_emissions = Column(DOUBLE)

    @classmethod
    def load_house_types_as_dict(cls, session: Session = alchemy_fw.session):
        """
        Class method to load the house type records and return them as dictionary

        :param session: An SQLAlchemy session
        :type session: :class:`sqlalchemy.orm.Session`

        :return: A dictionary of records
        :rtype: dict
        """
        try:
            return_dict = dict()
            results = session.query(cls).all()

            for house_type in results:
                return_dict[str(house_type.name) + str(house_type.no_of_rooms)] = house_type

            return return_dict
        except NoResultFound:
            LOGGER.error("No results found", exc_info=True)
            raise AppError(*ORMErrors.NO_RESULTS_FOUND)
        except Exception as exc:
            LOGGER.error("Could not execute query", exc_info=True)
            raise AppError(*ORMErrors.QUERY_FAILED, data=exc.args) from exc
