#!/usr/bin/python3
""" Xiopedia blueprint setup(s) """

from flask import Blueprint

xiopedia_views = Blueprint('xiopedia_views', __name__, url_prefix='/api/v1')

# views imports here
    # ioc
    # malware_families
    # groups
    # campaigns
    # malware
    # tools