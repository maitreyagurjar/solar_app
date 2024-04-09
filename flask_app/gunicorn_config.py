# -*- coding: UTF-8 -*-
"""
Gunicorn Configuration
================================================================================
This module contains the configuration settings for the gunicorn service workers
"""

import multiprocessing

import gunicorn

__author__ = "jadikesavan1@sheffield.ac.uk"

loglevel = "debug"

preload_app = True

worker_class = "gevent"

workers = multiprocessing.cpu_count() * 2 + 1

gunicorn.SERVER = "UNKNOWN"
