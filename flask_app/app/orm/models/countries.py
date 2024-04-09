# -*- coding: UTF-8 -*-
"""
Models - Countries
================================================================================
This module contains the ORM models for storing the data pertaining to the countries handled by the application
"""

import logging

from sqlalchemy import Column
from sqlalchemy.dialects.mysql import VARCHAR, DOUBLE, LONGTEXT
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm.session import Session

from app import alchemy_fw
from app.errors.exceptions import AppError
from app.messages.error.orm import ORMErrors
from app.orm.models import EntityMixin

__author__ = "jadikesavan1@sheffield.ac.uk"

LOGGER = logging.getLogger(__name__)


class Country(alchemy_fw.Model, EntityMixin):
    """
    ORM class representing the country information to be stored in the database tables

    :ivar iso_code: ISO code of the country
    vartype: iso_code: :class:`sqlalchemy.dialects.mysql.types.VARCHAR`

    :ivar name: The name of the country
    :vartype name: :class:`sqlalchemy.dialects.mysql.types.VARCHAR`

    :ivar population: The population of the country
    :vartype population: :class:`sqlalchemy.dialects.mysql.types.DOUBLE`

    :ivar solar_potential: The solar potential of the country in kWh/m^2/year
    :vartype solar_potential: :class:`sqlalchemy.dialects.mysql.types.DOUBLE`

    :ivar lcoe_solar: The levelized cost of electricity generated through solar energy in USD/kWh
    :vartype lcoe_solar: :class:`sqlalchemy.dialects.mysql.types.DOUBLE`

    :ivar description: The description of the countries to be displayed to the users
    :vartype description: :class:`sqlalchemy.dialects.mysql.types.LONGTEXT`

    :ivar latitude: A latitude coordinate of a marker to be pointed in the country
    :vartype latitude: :class:`sqlalchemy.dialects.mysql.types.DOUBLE`

    :ivar longitude: A longitude coordinate of a marker to be pointed in the country
    :vartype longitude: :class:`sqlalchemy.dialects.mysql.types.DOUBLE`
    """
    __tablename__ = "countries"

    iso_code = Column(VARCHAR(16), unique=True, nullable=False)
    name = Column(VARCHAR(255), unique=True, nullable=False)
    population = Column(DOUBLE, nullable=False)
    lcoe_solar = Column(DOUBLE, nullable=True)
    solar_potential = Column(DOUBLE, nullable=True)
    description = Column(LONGTEXT, nullable=False)
    latitude = Column(DOUBLE, nullable=True)
    longitude = Column(DOUBLE, nullable=True)

    @classmethod
    def load_countries_as_dict(cls, session: Session = alchemy_fw.session):
        """
        Method to load all the countries form the database and return as a dictionary

        :param session: An SQLAlchemy session
        :type session: :class:`sqlalchemy.orm.Session`

        :return: A dictionary of records
        :rtype: dict
        """
        try:
            return_dict = dict()
            results = session.query(cls).all()

            for country in results:
                return_dict[country.name] = country

            return return_dict
        except NoResultFound:
            LOGGER.error("No results found", exc_info=True)
            raise AppError(*ORMErrors.NO_RESULTS_FOUND)
        except Exception as exc:
            LOGGER.error("Could not execute query", exc_info=True)
            raise AppError(*ORMErrors.QUERY_FAILED, data=exc.args) from exc
