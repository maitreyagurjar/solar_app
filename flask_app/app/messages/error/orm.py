# -*- coding: UTF-8 -*-
"""
Error Messages - ORM
================================================================================
This module contains the class for rendering the ORM error messages
"""
__author__ = "jadikesavan1@sheffield.ac.uk"


class ORMErrors:
    """
    Class containing the ORM error messages
    """

    MULTIPLE_RESULTS_FOUND = ("Multiple results found for the query",
                              "error.orm.multiple.results")
    """
    Response to be returned when multiple results are found when one or no result is expected
    """

    NO_RESULTS_FOUND = ("No results found for the query",
                        "error.orm.no.results")
    """
    Response to be returned when no matching results are found
    """

    QUERY_FAILED = ("Query results could not be fetched",
                    "error.orm.query.failed")
    """
    Response to be returned when the query execution has failed
    """
