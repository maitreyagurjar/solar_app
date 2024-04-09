# -*- coding: UTF-8 -*-
"""
Routes - House
================================================================================
This module contains the routes to handles requests pertaining to houses handled in the application
"""

from flask import jsonify
from flask_restx import Namespace, Resource

from app.controllers.house import read_house_types, read_house_descriptions, read_house_information

__author__ = "jadikesavan1@sheffield.ac.uk"

house_ns = Namespace("house")


@house_ns.route("/read_list")
class HouseList(Resource):
    def get(self):
        return jsonify(read_house_types())


@house_ns.route("/read_descriptions")
class HouseDescriptions(Resource):
    def get(self):
        return jsonify(read_house_descriptions())


@house_ns.route("/read_info")
class HouseTypeInformation(Resource):
    def get(self):
        return jsonify(read_house_information())
