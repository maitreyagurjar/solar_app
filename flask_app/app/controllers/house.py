# -*- coding: UTF-8 -*-
"""
Controllers - House
================================================================================
This module contains the controllers for processing house information
"""
import json
import logging
import os

from flask import current_app as app

from app import alchemy_fw
from app.orm.manager import get_session
from app.orm.models.house import HouseType

__author__ = "jadikesavan1@sheffield.ac.uk"

LOGGER = logging.getLogger(__name__)

DATA_FOLDER = "data"
HOUSE_TYPES_JSON = "house_type_list.json"


def populate_house_types():
    """
    Method to populate the database with house data during the application startup

    :return: Nothing
    :rtype: None
    """
    # Load all the existing house type configured in the database
    houses_in_db = HouseType.load_house_types_as_dict(session=alchemy_fw.session)

    # Find the configuration file that contains the list of all the countries
    houses_fp = os.path.join(app.instance_path, DATA_FOLDER, HOUSE_TYPES_JSON)
    # Open the config file
    with open(houses_fp, "r") as fp:
        house_types_dict = json.load(fp=fp)

    for house_type in house_types_dict:
        if str(house_type["name"]) + str(house_type["no_of_rooms"]) not in houses_in_db.keys():
            house_type_obj = HouseType()
            house_type_obj.name = house_type["name"]
            house_type_obj.no_of_people = house_type["no_of_people"]
            house_type_obj.no_of_rooms = house_type["no_of_rooms"]
            house_type_obj.floor_area = house_type["floor_area"]
            house_type_obj.electricity_usage = house_type["electricity_usage"]
            house_type_obj.gas_usage = house_type["gas_usage"]
            house_type_obj.electricity_emissions = house_type["electricity_emissions"]
            house_type_obj.gas_emissions = house_type["gas_emissions"]

            with get_session() as t_session:
                house_type_obj.save(session=t_session)


def read_house_types():
    """
    Method to read all the house types configured in the database

    :return: A list of house types
    :rtype: list
    """
    house_type_dict = HouseType.load_house_types_as_dict(session=alchemy_fw.session)
    return list(house_type_dict.keys())


def read_house_information():
    """
    Method to read the information of house types configured in the database

    :return: A list of house types
    :rtype: list
    """
    house_type_dict = HouseType.load_house_types_as_dict(session=alchemy_fw.session)
    return_dict = dict()
    for key, value in house_type_dict.items():
        return_dict[key] = {
            "people": round(value.no_of_people, 2),
            "room number": round(value.no_of_rooms, 2),
            "electrical usage": round(value.electricity_usage, 2),
            "electrical emission": round(value.electricity_emissions, 2),
            "gas usage": round(value.gas_usage, 2),
            "gas emission": round(value.gas_emissions, 2),
            "offset value": round(value.gas_emissions + value.electricity_emissions, 2),
            "area": round(value.floor_area, 2)
        }

    return return_dict


def read_house_descriptions():
    """
    Method to read all the house types with their descriptions

    :return: A list of house types with their corresponding human readable descriptions
    :rtype: dict
    """
    house_type_dict = HouseType.load_house_types_as_dict(session=alchemy_fw.session)

    return_dict = dict()
    for key, value in house_type_dict.items():
        desc = f"""
        You live in a space with {value.no_of_people} (including yourself) and {value.no_of_rooms} rooms spread 
        across {round(value.floor_area, 2)} squared meters\n". Your typical electrical usage would be
         {round(value.electricity_usage, 2)} kWh/year (emitting {round(value.electricity_emissions, 2)} kgCO2/year) and 
         your typical gas usage would be {round(value.gas_usage, 2)} kWh/year (emitting {round(value.gas_emissions, 2)} 
         kgCO2/year) \n
        You should try to offset at-least {round(value.gas_emissions + value.electricity_emissions, 2)} kgCO2
        """

        return_dict[key] = desc

    return return_dict
