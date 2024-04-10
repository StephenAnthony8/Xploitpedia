#!/usr/bin/python3
""" api blueprint setup(s) """

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# views imports here
    # ioc
    # malware_families
    # groups
    # campaigns
    # malware
    # tools
from api.v1.views.stiix_items import *
from api.v1.views.iocs import *