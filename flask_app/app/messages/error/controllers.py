# -*- coding: UTF-8 -*-
"""
Messages - Controllers
================================================================================
This module contains all the error messages to be returned by controllers
"""

__author__ = "jadikesavan1@sheffield.ac.uk"

INTERNAL_SERVER_ERROR = ("Internal Server Error!",
                         "internal.server.error")


class SecurityMessages:
    USER_NOT_FOUND = ("User not found",
                      "user.not.found")

    PASSWORD_MISMATCH = ("Password Mismatch",
                         "password.mismatch")

    USERNAME_TAKEN = ("Username taken already",
                      "user.name.taken")


class PaymentMessages:
    PAYMENT_NOT_FOUND = ("Payment not found",
                         "payment.not.found")
