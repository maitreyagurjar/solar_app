# -*- coding: UTF-8 -*-
"""
Exceptions
================================================================================
This module contains the custom error classes for the application
"""
import json
from dataclasses import dataclass
from typing import Optional

from flask import Response
from werkzeug.exceptions import InternalServerError

__author__ = "jadikesavan1@sheffield.ac.uk"


@dataclass
class AppError(InternalServerError):
    """
    A custom error class for the application
    """

    message: str
    message_code: str
    data: Optional[dict] = None

    def __init__(self, message, message_code, data=None):
        self.message = message
        self.message_code = message_code
        self.data = data
        self.response = Response(json.dumps({"message": message,
                                             "message_code": message_code,
                                             "data": data}),
                                 status=self.code)
