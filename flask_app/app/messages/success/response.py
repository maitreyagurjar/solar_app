# -*- coding: UTF-8 -*-
"""
Messages - Success
================================================================================
This module contains the class containing all the success response messages
"""

__author__ = "jadikesavan1@sheffield.ac.uk"


class SecurityMessages:
    """
    Class containing response messages that need to be returned after successfully handling security requests
    """
    AUTH_SUCCESSFUL = ("User authentication successful",
                       "user.auth.successful")

    USER_CREATION_SUCCESSFUL = ("User created successfully",
                                "user.creation.successful")

    AUTH_NOT_SUCCESSFUL = ("User authentication not successful",
                           "user.auth.not_successful")

    ROLES_ADDED_SUCCESSFUL = ("User updated with the new set of roles",
                              "user.role.association.success")

    USER_DATA_EDIT_SUCCESSFUL = ("User updated successfully",
                                 "user.update.successful")

    USER_REMOVE_SUCCESSFUL = ("User deleted successfully",
                              "user.delete.successful")

    FUND_DELETE_SUCCESSFUL = ("Fund data removed from the system",
                              "fund.data.removal.success")
