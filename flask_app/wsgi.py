# -*- coding: UTF-8 -*-
"""
WSGI
===================
This is the module used by web server to hook onto the web application
"""
# For asynchronous calls
from gevent import monkey

monkey.patch_all()

from app.factory import create_app

__author__ = "jadikesavan1@sheffield.ac.uk"

app = create_app()
