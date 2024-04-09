# -*- coding: UTF-8 -*-
"""
Utilities - Application Configuration
================================================================================
This module contains the utility methods to handle the application configuration
"""
__author__ = "jadikesavan1@sheffield.ac.uk"


def construct_db_string(dialect, driver, username, password, host, port, database):
    """
    Method to construct the database connection string for use in SQLAlchemy

    :param dialect: The name of the database vendor
    :type dialect: str

    :param driver: The python driver used to connect to the vendor
    :type driver: str

    :param username: The username dedicated for the application
    :type username: str

    :param password: The password for the user created
    :type password: str

    :param host: The host address where the database service is run
    :type host: str

    :param port: The (mapped) port in the host, running the database
    :type port: str

    :param database: The name of the database created in the server, dedicated for the application
    :type database: str

    :return: The connection string as required by SQLAlchemy
    :rtype: str
    """
    conn_str = f"{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}"
    return conn_str
