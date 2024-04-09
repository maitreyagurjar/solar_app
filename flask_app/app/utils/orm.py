# -*- coding: UTF-8 -*-

from contextlib import contextmanager

from flask import current_app as app
from flask_security import current_user
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app import alchemy_fw

__author__ = "jadikesavan1@sheffield.ac.uk"


def create_alchemy_engine(bind_key=None):
    if bind_key is None:
        bind_key = app.config["DEFAULT_BIND_KEY"]

    binds = app.config["SQLALCHEMY_BINDS"][bind_key]
    engine = create_engine(binds)

    return engine


def create_connection(engine=None):
    if engine is None:
        engine = create_alchemy_engine()

    return engine.connect()


@contextmanager
def get_session(bind_key=None):
    if bind_key is None:
        bind_key = app.config["DEFAULT_BIND_KEY"]
    engine = app.config["ENGINES"][bind_key]

    with Session(bind=engine) as session:
        try:
            yield session
            session.commit()
        except Exception as exc:
            app.logger.error("Error in the session... Rolling back the changes")
            session.rollback()
            raise exc


def create_all_tables():
    if app.config["DB_CREATE_TABLES"]:
        alchemy_fw.create_all()


def get_username():
    if hasattr(current_user, "username"):
        return getattr(current_user, "username")
    return app.config["DEFAULT_USERNAME"]
