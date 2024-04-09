# -*- coding: UTF-8 -*-
"""
Exception Handlers
================================================================================
This module contains the method to handle the exceptions
"""

from app import api
from app.errors.exceptions import AppError

__author__ = "jadikesavan1@sheffield.ac.uk"


@api.errorhandler(AppError)
def handle_validation_exception(exc):
    return {"message": exc.message,
            "message_code": exc.message_code,
            "exception": exc.__class__.__name__}, exc.code
