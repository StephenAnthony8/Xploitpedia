#!/usr/bin/python3
"""
Initialize session and storage
"""

from models.engine.db_js_storage import MySqJson

storage = MySqJson()
storage.reload()