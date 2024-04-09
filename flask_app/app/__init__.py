# -*- coding: UTF-8 -*-
"""
Initializer - Application
================================================================================
This is the initializer module for the Flask application. The sub-components and dependencies of the application can
be declared here and initialized later in the factory
"""

from flask_caching import Cache
from flask_cors import CORS
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

__author__ = "jadikesavan1@sheffield.ac.uk"

# Dependency on Flask-RestX for Rapid API development
api = Api()

# Dependency on Flask-SQLAlchemy for database integration
alchemy_fw = SQLAlchemy()

# Dependency on Flask-CORS to allow cross-origin requests
cors = CORS()

# Dependency on Flask-Caching
cache = Cache()
