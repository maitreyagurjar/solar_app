"""
Models - Funds
================================================================================
This module contains the ORM models for storing the data pertaining to the funds and transactions handled by the application
"""
import logging

import sqlalchemy
from sqlalchemy import Column, ForeignKey, UniqueConstraint
from sqlalchemy import text
from sqlalchemy.dialects.mysql import DOUBLE
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm.session import Session

from app import alchemy_fw
from app.errors.exceptions import AppError
from app.messages.error.orm import ORMErrors
from app.orm.models import EntityMixin

__author__ = "mmgurjar1@sheffield.ac.uk"

LOGGER = logging.getLogger(__name__)


class Funds(alchemy_fw.Model, EntityMixin):
    """
    ORM class representing the fund information to be stored in the database tables

    :ivar emission_current: current emission of the user
    vartype: emission_current: :class:`sqlalchemy.dialects.mysql.types.DOUBLE`

    :ivar emission_offset: The emission the user is offsetting
    :vartype emission_offset: :class:`sqlalchemy.dialects.mysql.types.DOUBLE`

    :ivar donated_amount: The amount donated by the user
    :vartype donated_amount: :class:`sqlalchemy.dialects.mysql.types.DOUBLE`

    :ivar donated_panels: The number of solar panels donated by the user
    :vartype solar_potential: :class:`sqlalchemy.dialects.mysql.types.DOUBLE`
    """
    __tablename__ = "funds"
    __table_args__ = (UniqueConstraint('user_id', 'created_on'),)

    emission_current = Column(DOUBLE, nullable=False)
    emission_offset = Column(DOUBLE, nullable=True)
    donated_amount = Column(DOUBLE, nullable=False)
    donated_panels = Column(DOUBLE, nullable=False)
    user_id = Column(ForeignKey("users.id"))
    country_id = (Column(ForeignKey("countries.id")))

    @classmethod
    def load_funds_as_dict(cls, session: Session = alchemy_fw.session):
        """
        Method to load all the fund data form the database and return as a dictionary

        :param session: An SQLAlchemy session
        :type session: :class:`sqlalchemy.orm.Session`

        :return: A dictionary of records
        :rtype: dict
        """
        try:
            return_dict = dict()
            results = session.query(cls).all()

            for fund in results:
                return_dict[str(fund.user_id) + str(fund.created_on)] = fund

            return return_dict
        except NoResultFound:
            LOGGER.error("No results found", exc_info=True)
            raise AppError(*ORMErrors.NO_RESULTS_FOUND)
        except Exception as exc:
            LOGGER.error("Could not execute query", exc_info=True)
            raise AppError(*ORMErrors.QUERY_FAILED, data=exc.args) from exc

    @classmethod
    def qry_sum_by_country(self):
        """
        Method to query the database to get the aggregated sum of donations made w.r.t each country

        :return: The donations made for each country
        :rtype: dict
        """

        return_list = list()

        qry = f"""
                SELECT 
                    countries.name AS `country`,
                    SUM(donated_amount) AS `donation`
                FROM
                    solar_app_db.funds
                        INNER JOIN
                    countries ON countries.id = funds.country_id
                GROUP BY country;
        """

        qry = text(qry)

        results = alchemy_fw.session.execute(qry)

        for entry in results:
            return_dict = dict()
            return_dict["name"] = entry[0]
            return_dict["value"] = entry[1]
            return_list.append(return_dict)

        return return_list

    @classmethod
    def qry_landing_stats(self):
        """
        Method to query the database to get the aggregated sum of donations made w.r.t each country

        :return: The donations made for each country
        :rtype: dict
        """

        return_keys = ["users", "countries", "donation"]
        return_values = list()

        qry = f"""
               SELECT 
                    COUNT(DISTINCT(user_id)) AS `USERS`,
                    COUNT(DISTINCT(country_id)) AS `COUNTRIES`,
                    SUM(donated_amount) AS `AMOUNT`
                FROM
                    solar_app_db.funds;
        """

        qry = text(qry)

        results = alchemy_fw.session.execute(qry)

        values = results.fetchall()[0]
        return_values.extend([values[0], values[1], values[2]])

        return dict(zip(return_keys, return_values))

    @classmethod
    def qry_sum_by_date(self):
        """
        Method to query the database to get the sum of donations made on each day

        :return: The donations made on each day as a list of lists
        :rtype: list
        """

        return_dict = dict()
        datelist = list()
        value_list = list()

        qry = f"""
                SELECT 
                    created_on AS `date`, 
                    SUM(donated_amount) AS `donation`
                FROM
                    solar_app_db.funds
                GROUP BY date
                ORDER BY date;
        """

        qry = text(qry)

        results = alchemy_fw.session.execute(qry)

        for entry in results:
            datelist.append(entry[0].strftime("%Y-%m-%d"))
            value_list.append(entry[1])

        return_dict["dates"] = datelist
        return_dict["values"] = value_list
        return return_dict
