# -*- coding: UTF-8 -*-
"""
Configuration - Default
================================================================================
This module contains the default configuration to be loaded to the application. The production and testing
environments will be extension of these default configuration settings
"""
import os

from app.utils.configs import construct_db_string

__author__ = "jadikesavan1@sheffield.ac.uk"


class DefaultConfig:
    """
    Class containing the default configuration settings for the application
    """

    APPLICATION_ROOT = "/"
    DEFAULT_USERNAME = "SYSTEM"
    SECRET_KEY = "23ae3f49d8065ba7c0e3171d6a42baef6ca304e6ddd314a32ab832d7974c58de"

    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_size": 20,
        "max_overflow": 10,
        "pool_pre_ping": True,
        "echo": False
    }

    FLASK_CACHING_CONFIGS = {
        "CACHE_TYPE": "FileSystemCache",
        "CACHE_DEFAULT_TIMEOUT": 3600,
        "CACHE_DIR": "cache"
    }
    SQLALCHEMY_DATABASE_URI = construct_db_string(dialect="mysql",
                                                  driver="pymysql",
                                                  username=os.getenv("DB_USER", "solar_app"),
                                                  password=os.getenv("DB_PASSWORD", "root"),
                                                  host="solar_app_db",
                                                  port="3306",
                                                  database="solar_app_db")

    DB_BIND_KEY = "PRIMARY_DB_BIND_KEY"

    SQLALCHEMY_BINDS = {
        "PRIMARY_DB_BIND_KEY": SQLALCHEMY_DATABASE_URI
    }

    SESSION_COOKIE_NAME = "appSession"
    SESSION_COOKIE_SECURE = True
    PERMANENT_SESSION_LIFETIME = 10 * 60

    PROPAGATE_EXCEPTIONS = False
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024

    DEBUG = True
    CREATE_TABLES = True
    TEMPLATES_AUTO_RELOAD = True
    TRAP_HTTP_EXCEPTIONS = True

    APP_ADMIN_EMAIL = "no-reply@gmail.com"
    APP_ADMIN_USERNAME = "admin"
    APP_ADMIN_FIRSTNAME = "Application"
    APP_ADMIN_LASTNAME = "Admin"
    APP_ADMIN_PASSWORD = os.getenv("APP_ADMIN_PASSWORD", "root")

    APP_ADMIN_PARAMS = {
        "email": APP_ADMIN_EMAIL,
        "username": APP_ADMIN_USERNAME,
        "password": APP_ADMIN_PASSWORD
    }

    SECURITY_PASSWORD_SALT = os.getenv("PASSWORD_SALT", "some-salt")
    SECURITY_PASSWORD_SINGLE_HASH = os.getenv("PASSWORD_SINGLE_HASH", "plaintext")

    ELECTRICITY_API_ZONES_URL = "https://api.electricitymap.org/v3/zones"
    ELECTRICITY_API_HEADER = "auth-token"
    ELECTRICITY_API_PRIMARY_KEY = "K5mwMSPJwLmUxYOLkavZ1hhjosANNV3m"
    ELECTRICITY_API_CARBON_INTENSITY_URL = "https://api.co2signal.com/v1/latest"

    POPULATE_SYNTHETIC_DATA = True
