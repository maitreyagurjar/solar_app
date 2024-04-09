# -*- coding: UTF-8 -*-
"""
Routes - Security
================================================================================
This module contains the routes for handling the requests related to security of the application
"""
from flask import jsonify
from flask_restx import Namespace, Resource, reqparse

from app.controllers.security import delete_user_data, update_password, create_user
from app.controllers.security import list_users, list_staff, list_admins
from app.controllers.security import login_user, roles_of_user, list_roles, add_roles_to_user, edit_user_data
from app.messages.success.response import SecurityMessages
from app.routes import success_response

__author__ = "jadikesavan1@sheffield.ac.uk"

security_ns = Namespace("security")


@security_ns.route("/login")
@security_ns.param("username", "Name of the user")
@security_ns.param("password", "Password of the user")
class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str, help="Name of the user")
        parser.add_argument("password", type=str, help="Password of the user")

        username = parser.parse_args()["username"]
        password = parser.parse_args()["password"]

        success_auth = login_user(username=username, password=password)

        if success_auth:
            return success_response(*SecurityMessages.AUTH_SUCCESSFUL, data=success_auth)
        return success_response(*SecurityMessages.AUTH_NOT_SUCCESSFUL)


@security_ns.route("/create_user")
@security_ns.param("email", "Email of the user")
@security_ns.param("username", "Name of the user")
@security_ns.param("password", "Password of the user")
class CreateUser(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("email", type=str, help="Email of the user")
        parser.add_argument("username", type=str, help="Name of the user")
        parser.add_argument("password", type=str, help="Password of the user")

        email = parser.parse_args()["email"]
        username = parser.parse_args()["username"]
        password = parser.parse_args()["password"]

        create_user(email=email, username=username, password=password)

        return success_response(*SecurityMessages.USER_CREATION_SUCCESSFUL)


@security_ns.route("/create_staff")
@security_ns.param("email", "Email of the staff")
@security_ns.param("username", "Name of the staff")
@security_ns.param("password", "Password of the staff")
class CreateStaff(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("email", type=str, help="Email of the staff")
        parser.add_argument("username", type=str, help="Name of the staff")
        parser.add_argument("password", type=str, help="Password of the staff")

        email = parser.parse_args()["email"]
        username = parser.parse_args()["username"]
        password = parser.parse_args()["password"]

        create_user(email=email, username=username, password=password, role="LEVEL-1")

        return success_response(*SecurityMessages.USER_CREATION_SUCCESSFUL)


@security_ns.route("/user_roles")
@security_ns.param("username", "Name of the user")
class UserRoles(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str, help="Name of the user")

        username = parser.parse_args()["username"]

        return jsonify(roles_of_user(username=username))


@security_ns.route("/add_roles")
@security_ns.param("username", "Name of the user")
@security_ns.param("roles", "Roles to be added as a list")
class AddUserRoles(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str, help="Name of the user")
        parser.add_argument("roles", action="append", help="Roles to be added")

        username = parser.parse_args()["username"]
        roles = parser.parse_args()["roles"]

        add_roles_to_user(username, roles)

        return success_response(*SecurityMessages.ROLES_ADDED_SUCCESSFUL)


@security_ns.route("/roles")
class ListRoles(Resource):
    def get(self):
        return jsonify(list_roles())


@security_ns.route("/list_users")
class ListUsers(Resource):
    def get(self):
        return jsonify(list_users())


@security_ns.route("/list_staff")
class ListStaff(Resource):
    def get(self):
        return jsonify(list_staff())


@security_ns.route("/list_admin")
class ListAdmin(Resource):
    def get(self):
        return jsonify(list_admins())


@security_ns.route("/edit_user")
@security_ns.param("username", "Name of the user")
@security_ns.param("email", "Email of the user")
@security_ns.param("new_username", "New username of the user")
class EditUser(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str, help="Name of the user")
        parser.add_argument("email", type=str, help="Email of the user")
        parser.add_argument("new_username", type=str, help="New username for the user")

        username = parser.parse_args()["username"]
        email = parser.parse_args()["email"]
        new_username = parser.parse_args()["new_username"]

        edit_user_data(username, email, new_username)

        return success_response(*SecurityMessages.USER_DATA_EDIT_SUCCESSFUL)


@security_ns.route("/remove_user")
@security_ns.param("username", "Name of the user")
class RemoveUser(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str, help="Name of the user")

        username = parser.parse_args()["username"]

        delete_user_data(username)

        return success_response(*SecurityMessages.USER_REMOVE_SUCCESSFUL)


@security_ns.route("/change_password")
@security_ns.param("username", "Name of the user")
@security_ns.param("password", "Current Password")
@security_ns.param("new_password", "New Password")
class ChangePassword(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str, help="Name of the user")
        parser.add_argument("password", type=str, help="Password of the user")
        parser.add_argument("new_password", type=str, help="New Password of the user")

        username = parser.parse_args()["username"]
        password = parser.parse_args()["password"]
        new_password = parser.parse_args()["new_password"]

        update_password(username, password, new_password)
        return success_response(*SecurityMessages.USER_DATA_EDIT_SUCCESSFUL)
