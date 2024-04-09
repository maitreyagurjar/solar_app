# -*- coding: UTF-8 -*-
"""
Health check route
================================================================================
This module contains an unauthenticated route for checking the health of the application
"""

from flask_restx import Namespace, Resource

__author__ = "jadikesavan1@sheffield.ac.uk"

health_ns = Namespace("health")


@health_ns.route("/")
class Health(Resource):
    def get(self):
        return {"Health": "OK"}
