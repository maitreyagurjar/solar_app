# -*- coding: UTF-8 -*-
"""
App Factory
================================================================================
This module contains the method to create and return an application to be used by the spawned workers.
Factory design pattern is used to return the same application instance
"""
from flask import Flask

from app import api, alchemy_fw, cors, cache
from app.controllers.countries import populate_countries
from app.controllers.funds import populate_synthetic_data
from app.controllers.house import populate_house_types
from app.controllers.security import create_app_admin, populate_roles
from app.health import health_ns
from app.orm.manager import create_tables
from app.routes.countries import country_ns
from app.routes.electricity import electricity_ns
from app.routes.funds import funds_ns
from app.routes.house import house_ns
from app.routes.security import security_ns
from configs.default import DefaultConfig

__author__ = "jadikesavan1@sheffield.ac.uk"

TEMPLATE_FOLDER = "templates/web/layout"
STATIC_FOLDER = "templates/web/static"


def create_app():
    """
    Method to create an application and return it to the worker

    :return: A Flask application
    :rtype: :class:`flask.app.Flask`
    """
    app = Flask(__name__,
                instance_relative_config=True,
                static_folder=STATIC_FOLDER,
                template_folder=TEMPLATE_FOLDER)

    app.config.from_object(DefaultConfig)

    with app.app_context():
        api.add_namespace(electricity_ns, "/electricity")
        api.add_namespace(security_ns, "/security")
        api.add_namespace(health_ns, "/health")
        api.add_namespace(country_ns, "/countries")
        api.add_namespace(funds_ns, "/funds")
        api.add_namespace(house_ns, "/house")

        api.init_app(app=app)
        alchemy_fw.init_app(app=app)
        cors.init_app(app=app)
        cache.init_app(app=app, config=app.config["FLASK_CACHING_CONFIGS"])

        create_tables()
        populate_roles()
        create_app_admin()
        populate_countries()
        populate_house_types()

        if app.config["POPULATE_SYNTHETIC_DATA"]:
            populate_synthetic_data()

    return app
