# -*- coding: UTF-8 -*-
"""
Routes - Initializer
================================================================================
This module contains the initializer methods for routes handling all the requests
"""

from http import HTTPStatus

from flask import jsonify

__author__ = "jadikesavan1@sheffield.ac.uk"


def success_response(message, message_code, data=None):
    """
    Method to return a success response with the given message

    :param message: The message to be returned
    :type message: str

    :param message_code: The message code
    :type message_code: str

    :param data: The data to be returned
    :type data: dict

    :return: A Flask Response
    :rtype: :class:`flask.wrappers.Response`
    """
    return_dict = {
        "message": message,
        "message_code": message_code,
        "status": HTTPStatus.OK
    }

    if data is not None:
        return_dict = {**return_dict, **data}

    return jsonify(return_dict)
