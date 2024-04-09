# -*- coding: UTF-8 -*-

import logging
from contextlib import contextmanager

from flask import current_app as app

from app import alchemy_fw

__author__ = "jadikesavan1@sheffield.ac.uk"

LOGGER = logging.getLogger(name=__name__)


@contextmanager
def get_session():
    session = alchemy_fw.session
    try:
        yield session
        session.commit()
    except Exception as ex:
        LOGGER.error("An error has occurred in the database")
        session.rollback()
        raise ex


def create_tables():
    if app.config["CREATE_TABLES"]:
        alchemy_fw.create_all()
