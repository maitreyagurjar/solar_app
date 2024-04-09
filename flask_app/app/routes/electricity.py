# -*- coding: UTF-8 -*-
"""
Routes - Electricity
================================================================================
This module contains the routes for handling requests pertaining to electricity
"""

from flask_restx import Namespace, Resource

from app.controllers.electricity import get_zones, get_carbon_intensity

__author__ = "jadikesavan1@sheffield.ac.uk"

electricity_ns = Namespace("electricity")


@electricity_ns.route("/zones")
class Zones(Resource):
    def get(self):
        return get_zones()


@electricity_ns.route("/carbon_intensity")
class CarbonIntensity(Resource):
    def get(self):
        return get_carbon_intensity()
