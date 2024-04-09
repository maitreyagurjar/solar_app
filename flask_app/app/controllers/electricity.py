# -*- coding: UTF-8 -*-
"""
Controller - Electricity
================================================================================
This module contains the methods to process the requests pertaining to electricity data. These data are to be fetched
from an external API whose details can be found in the requirement documentation
"""

import requests
from flask import current_app as app
from requests.adapters import HTTPAdapter, Retry
from requests.exceptions import ConnectionError, InvalidURL

from app.errors.exceptions import AppError
from app.messages.error.controllers import INTERNAL_SERVER_ERROR

__author__ = "jadikesavan1@sheffield.ac.uk"


def get_request_session():
    """
    Method to return an request session for querying an external API service

    :return: A request session
    :rtype: :class:`requests.sessions.Session`
    """
    # Create a requests session
    session = requests.Session()

    # Create a retry strategy
    # NOTE: Read more on retry: https://requests.readthedocs.io/en/latest/user/advanced/
    retries = Retry(total=3, backoff_factor=0.3, status_forcelist=(500, 502, 504))

    # Mount the session to perform HTTP and HTTPS requests
    session.mount("http://", HTTPAdapter(max_retries=retries))
    session.mount("https://", HTTPAdapter(max_retries=retries))

    # Return the session
    return session


def get_data(url, headers=None, params=None):
    """
    Method to perform a HTTP GET on the given URL with the passed headers and the parameters for querying

    :param url: The URL to perform a HTTP GET
    :type url: str

    :param headers: The additional headers that needs to be passed
    :type headers: Union[dict, None]

    :param params: The query parameters that needs to be passed
    :type params: Union[dict, None]

    :return: The data returned as JSON
    :rtype: dict
    """
    # If no headers are passed
    if headers is None:
        headers = {}

    # If no query parameters are passed
    if params is None:
        params = {}

    # Request a session
    session = get_request_session()
    try:
        # Get the response data from the API
        data = session.get(url=url, headers={**headers}, params={**params})

        # Return if the data is valid, else raise an error
        if data is not None:
            return data.json()
        else:
            raise AppError(*INTERNAL_SERVER_ERROR)
    except ConnectionError as c_err:
        raise c_err

    except InvalidURL as invalid_err:
        raise invalid_err


def get_zones():
    """
    Method to get all the zones in the electricity API

    :return: A dictionary containing the list of all zones present
    :rtype: dict
    """
    zones = get_data(url=app.config["ELECTRICITY_API_ZONES_URL"])
    return zones


def get_carbon_intensity(country_code="GB"):
    """
    Method to get the current carbon intensity

    :param country_code: The ISO country code
    :type country_code: str

    :return: A dictionary containing the carbon intensity and its units
    :rtype: dict
    """
    carbon_intensity = get_data(url=app.config["ELECTRICITY_API_CARBON_INTENSITY_URL"],
                                headers={app.config["ELECTRICITY_API_HEADER"]: app.config[
                                    "ELECTRICITY_API_PRIMARY_KEY"]},
                                params={"countryCode": country_code})

    return carbon_intensity
