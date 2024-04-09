"""
Routes - Funds
================================================================================
This module contains the routes to handles requests pertaining to fund data handled in the application
"""

from flask import jsonify
from flask_restx import Namespace, Resource, reqparse

from app.controllers.funds import add_funds, read_funds, delete_fund_by_id
from app.controllers.funds import aggregate_fund_by_country, aggregate_funds_by_date
from app.controllers.funds import get_landing_page_stats

__author__ = "mmgurjar1@sheffield.ac.uk"

funds_ns = Namespace("funds")


@funds_ns.route("/add")
@funds_ns.param(name="emission_current", description="")
@funds_ns.param(name="emission_offset", description="")
@funds_ns.param(name="username", description="")
@funds_ns.param(name="country_of_choice", description="")
@funds_ns.param(name="donated_amount", description="")
@funds_ns.param(name="donated_panels", description="")
class AddFund(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument("emission_current", type=str, help="Current emission of the user")
        parser.add_argument("emission_offset", type=str, help="Emission to offset")
        parser.add_argument("username", type=str, help="Name of user")
        parser.add_argument("country_of_choice", type=str, help="Name of the country")
        parser.add_argument("donated_amount", type=str, help="Amount donated")
        parser.add_argument("donated_panels", type=str, help="Number of panels donated")

        emission_current = parser.parse_args()["emission_current"]
        emission_offset = parser.parse_args()["emission_offset"]
        username = parser.parse_args()["username"]
        country_of_choice = parser.parse_args()["country_of_choice"]
        donated_amount = parser.parse_args()["donated_amount"]
        donated_panels = parser.parse_args()["donated_panels"]

        add_funds(username=username,
                  emission_current=float(emission_current),
                  emission_offset=float(emission_offset),
                  country_of_choice=country_of_choice,
                  donated_amount=float(donated_amount),
                  donated_panels=float(donated_panels))

        return jsonify({"message": "Funds added to table"})


@funds_ns.route("/read")
class ReadFund(Resource):
    def get(self):
        return jsonify(read_funds())


@funds_ns.route("/fund_countries")
class FundsForCountry(Resource):
    def get(self):
        return jsonify(aggregate_fund_by_country())


@funds_ns.route("/fund_date")
class FundsByDate(Resource):
    def get(self):
        return jsonify(aggregate_funds_by_date())


@funds_ns.route("/landing_stats")
class LandingStats(Resource):
    def get(self):
        return jsonify(get_landing_page_stats())


@funds_ns.route("/delete_funds")
@funds_ns.param("fund_id", "Fund ID to be deleted")
class DeleteFund(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("fund_id", type=str, help="Fund ID to be deleted")

        fund_id = parser.parse_args()["fund_id"]

        delete_fund_by_id(fund_id)

        return jsonify({"message": "Fund data removed"})
