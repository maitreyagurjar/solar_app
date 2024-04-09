# -*- coding: UTF-8 -*-
"""
Routes - Country
================================================================================
This module contains the routes to handles requests pertaining to countries handled in the application
"""

from flask import jsonify
from flask_restx import Namespace, Resource, reqparse

from app import cache
from app.controllers.countries import delete_country, add_country
from app.controllers.countries import get_all_countries_data
from app.controllers.countries import get_country_display_data, get_all_countries
from app.controllers.countries import update_country

__author__ = "jadikesavan1@sheffield.ac.uk"

country_ns = Namespace("countries")


@country_ns.route("/display_data")
@country_ns.param("country", "Name of the country")
class DisplayData(Resource):
    @cache.cached(timeout=3600)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("country", type=str, help="Name of the country")
        country = parser.parse_args()["country"]
        return jsonify(get_country_display_data(country=country))


@country_ns.route("/list")
class ListCountries(Resource):
    @cache.cached(timeout=3600)
    def get(self):
        return jsonify(get_all_countries())


@country_ns.route("/all_country_data")
class AllCountries(Resource):
    @cache.cached(timeout=3600)
    def get(self):
        return jsonify(get_all_countries_data())


@country_ns.route("/add_country_data")
@country_ns.param("country_iso_code", "Name of country")
@country_ns.param("country_name", "Name of country")
@country_ns.param("country_description", "Description of the country")
@country_ns.param("country_population", "Population of the country")
@country_ns.param("country_latitude", "Latitude of the country")
@country_ns.param("country_longitude", "Longitude of the country")
@country_ns.param("country_lcoe_solar", "The levelized cost of electricity generated through solar energy in USD/kWh")
@country_ns.param("country_solar_potential", "The solar potential of the country")
class AddCountry(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("country_iso_code", type=str, help="ISO Code of the country")
        parser.add_argument("country_name", type=str, help="Name of the country")
        parser.add_argument("country_description", type=str, help="Description of the country")
        parser.add_argument("country_population", type=int, help="Population of the country")
        parser.add_argument("country_latitude", type=float, help="Latitude of the country")
        parser.add_argument("country_longitude", type=float, help="Longitude of the country")
        parser.add_argument("country_lcoe_solar", type=float,
                            help="The levelized cost of electricity generated through solar energy in USD/kWh")
        parser.add_argument("country_solar_potential", type=float, help="The solar potential of the country")
        country_iso_code = parser.parse_args()["country_iso_code"]
        country_name = parser.parse_args()["country_name"]
        country_description = parser.parse_args()["country_description"]
        country_population = parser.parse_args()["country_population"]
        country_latitude = parser.parse_args()["country_latitude"]
        country_longitude = parser.parse_args()["country_longitude"]
        country_lcoe_solar = parser.parse_args()["country_lcoe_solar"]
        country_solar_potential = parser.parse_args()["country_solar_potential"]
        add_country(country_iso_code=country_iso_code, country_name=country_name,
                    country_description=country_description, country_population=int(country_population),
                    country_latitude=float(country_latitude),
                    country_longitude=float(country_longitude), country_lcoe_solar=float(country_lcoe_solar),
                    country_solar_potential=float(country_solar_potential))
        return jsonify({"message": "Country added to table"})


@country_ns.route("/update_country_data")
@country_ns.param("country_iso_code", "Name of country")
@country_ns.param("country_name", "Name of country")
@country_ns.param("country_description", "Description of the country")
@country_ns.param("country_population", "Population of the country")
@country_ns.param("country_latitude", "Latitude of the country")
@country_ns.param("country_longitude", "Longitude of the country")
@country_ns.param("country_lcoe_solar", "The levelized cost of electricity generated through solar energy in USD/kWh")
@country_ns.param("country_solar_potential", "The solar potential of the country")
class UpdateCountry(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("country_iso_code", type=str, help="ISO Code of the country")
        parser.add_argument("country_name", type=str, help="Name of the country")
        parser.add_argument("country_description", type=str, help="Description of the country")
        parser.add_argument("country_population", type=int, help="Population of the country")
        parser.add_argument("country_latitude", type=float, help="Latitude of the country")
        parser.add_argument("country_longitude", type=float, help="Longitude of the country")
        parser.add_argument("country_lcoe_solar", type=float,
                            help="The levelized cost of electricity generated through solar energy in USD/kWh")
        parser.add_argument("country_solar_potential", type=float, help="The solar potential of the country")
        country_iso_code = parser.parse_args()["country_iso_code"]
        country_name = parser.parse_args()["country_name"]
        country_description = parser.parse_args()["country_description"]
        country_population = parser.parse_args()["country_population"]
        country_latitude = parser.parse_args()["country_latitude"]
        country_longitude = parser.parse_args()["country_longitude"]
        country_lcoe_solar = parser.parse_args()["country_lcoe_solar"]
        country_solar_potential = parser.parse_args()["country_solar_potential"]
        update_country(country_iso_code=country_iso_code, country_name=country_name,
                       country_description=country_description, country_population=int(country_population),
                       country_latitude=float(country_latitude),
                       country_longitude=float(country_longitude), country_lcoe_solar=float(country_lcoe_solar),
                       country_solar_potential=float(country_solar_potential))
        return jsonify({"message": "Country updated"})


@country_ns.route("/delete_country")
@country_ns.param("country", "Name of country")
class DeleteCountry(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("country", type=str, help="Name of the country")
        country = parser.parse_args()["country"]
        delete_country(country)
