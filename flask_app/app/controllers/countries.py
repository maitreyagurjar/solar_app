# -*- coding: UTF-8 -*-
"""
Controllers - Countries
================================================================================
This module contains the methods to process the requests pertaining to country data. These data are to be loaded during
the application startup from the data folder
"""
import json
import logging
import os

from flask import current_app as app
from sqlalchemy.exc import MultipleResultsFound, NoResultFound

from app import alchemy_fw
from app.controllers.electricity import get_carbon_intensity
from app.errors.exceptions import AppError
from app.messages.error.orm import ORMErrors
from app.orm.manager import get_session
from app.orm.models.countries import Country

DATA_FOLDER = "data"
COUNTRIES_JSON = "countries_list.json"

__author__ = "jadikesavan1@sheffield.ac.uk"
LOGGER = logging.getLogger(__name__)


def populate_countries():
    """
    Method to populate the database with country data during the application startup

    :return: Nothing
    :rtype: None
    """
    # Query the existing country records as dictionary
    countries_in_db = Country.load_countries_as_dict(session=alchemy_fw.session)

    # Find the configuration file that contains the list of all the countries
    countries_fp = os.path.join(app.instance_path, DATA_FOLDER, COUNTRIES_JSON)
    # Open the config file
    with open(countries_fp, "r") as fp:
        countries_dict = json.load(fp=fp)

    for country in countries_dict:
        # If the country is not present in the dictionary / records, create the country
        # This is to detect the changes that need to be updated in the database
        if country["name"] not in countries_in_db.keys():
            new_country = Country()
            new_country.iso_code = country["iso_code"]
            new_country.name = country["name"]
            new_country.description = country["description"]
            new_country.population = country["population"]
            new_country.latitude = country["latitude"]
            new_country.longitude = country["longitude"]
            new_country.lcoe_solar = country["lcoe"]
            new_country.solar_potential = country["solar_potential"]

            with get_session() as t_session:
                new_country.save(session=t_session)


def find_country(country):
    """
    Method to find the country in the database and return the Country object

    :param country: The name of the country to be searched
    :type country: str

    :return: An instance of the Country if found, None otherwise
    :rtype: Union[:class:`app.orm.models.countries.Country`, None]
    """
    try:
        return Country.query.filter_by(name=country).one_or_none()  # type: ignore

    except MultipleResultsFound as m_exc:
        LOGGER.error("More than one result found", extra={"name": country}, exc_info=True)
        raise AppError(*ORMErrors.MULTIPLE_RESULTS_FOUND) from m_exc

    except NoResultFound as no_exc:
        LOGGER.error("No result found", extra={"name": country}, exc_info=True)
        raise AppError(*ORMErrors.NO_RESULTS_FOUND) from no_exc


def get_country_display_data(country):
    """
    Method to get the data to be displayed about the country

    :param country: The name of the country whose information is to be displayed
    :type country: str

    :return: A dictionary containing country information, if country is found, None otherwise
    :rtype: Union[:class:`app.orm.models.countries.Country`, None]
    """
    if country is None:
        raise AppError(*ORMErrors.QUERY_FAILED)

    country_obj = find_country(country=country)
    country_dict = country_obj.to_dict()
    country_dict["co2_data"] = round(float(get_carbon_intensity(country_code=country_obj.iso_code)["data"][
                                               "carbonIntensity"]), 2)
    country_dict["solar_data"] = round(float(country_obj.solar_potential), 2)
    country_dict["lcoe_solar"] = round(float(country_dict["lcoe_solar"]), 2)
    country_dict["population"] = round(float(country_dict["population"]), 2)

    return country_dict


def get_solar_potential(country):
    country_obj = find_country(country=country)
    return country_obj.solar_potential


def get_lcoe_solar(country):
    country_obj = find_country(country=country)
    return country_obj.lcoe_solar


def get_all_countries():
    """
    Method to list all the countries configured in the database

    :return: A list of all countries
    :rtype: list
    """
    country_dict = Country.load_countries_as_dict(session=alchemy_fw.session)
    return list(country_dict.keys())


def get_all_countries_data():
    """
    Method to get the data for rendering the country information

    :return: List of information of all the configured countries
    :rtype: list
    """
    country_dict = Country.load_countries_as_dict(session=alchemy_fw.session)
    return_list = list()
    max_possible_score = 0
    for key, value in country_dict.items():
        country_data = value.to_dict()

        co2_data = get_carbon_intensity(country_code=value.iso_code)["data"]
        if "carbonIntensity" not in co2_data.keys():
            co2_data = 0
        else:
            co2_data = co2_data["carbonIntensity"]

        country_data["co2_data"] = round(float(co2_data), 2)
        country_data["solar_data"] = round(float(value.solar_potential), 2)

        co2_emission = country_data["co2_data"]
        population = country_data["population"]
        carbon_per_capita = co2_emission / float(population)
        lcoe_solar = country_data["lcoe_solar"]

        if carbon_per_capita != 0:
            score = (country_data["solar_data"] / carbon_per_capita) * (1 / float(lcoe_solar))
        else:
            score = (country_data["solar_data"] / 1) * (1 / float(lcoe_solar))

        if max_possible_score < score:
            max_possible_score = score

        percentage = score * 100 / max_possible_score
        country_data["value"] = round(float(percentage), 2)

        country_data["lcoe_solar"] = round(float(country_data["lcoe_solar"]), 2)
        country_data["population"] = round(float(country_data["population"]), 2)

        return_list.append(country_data)

    return return_list


def add_country(country_name, country_iso_code, country_description, country_population, country_latitude,
                country_longitude, country_lcoe_solar, country_solar_potential):
    """
    Method to add a new country to the Countries database
    :return:
    """

    country_data = Country()
    country_data.name = country_name
    country_data.description = country_description
    country_data.iso_code = country_iso_code
    country_data.population = country_population
    country_data.latitude = country_latitude
    country_data.longitude = country_longitude
    country_data.lcoe_solar = country_lcoe_solar
    country_data.solar_potential = country_solar_potential
    with get_session() as t_session:
        country_data.save(session=t_session)


def update_country(country_name, country_iso_code, country_description, country_population, country_latitude,
                   country_longitude, country_lcoe_solar, country_solar_potential):
    """
    Method to update country in the Countries database
    :return:
    """

    country_data = find_country(country=country_name)
    country_data.name = country_name
    country_data.description = country_description
    country_data.iso_code = country_iso_code
    country_data.population = country_population
    country_data.latitude = country_latitude
    country_data.longitude = country_longitude
    country_data.lcoe_solar = country_lcoe_solar
    country_data.solar_potential = country_solar_potential

    with get_session() as t_session:
        country_data.update(session=t_session)


def delete_country(country):
    """
   Method to delete a country to the Countries database
   :param country: country details to be updated
   :type country: str
   :return:
   """
    if country is None:
        raise AppError(*ORMErrors.QUERY_FAILED)

    country_obj = find_country(country=country)

    with get_session() as t_session:
        country_obj.delete(session=t_session)
