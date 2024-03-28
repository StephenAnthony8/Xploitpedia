#!/usr/bin/python3
""" Creates url ioc objects """
from models.base_models import IocBaseModel, Base

class UrlPayload(IocBaseModel, Base):
    """creates url type iocs with payloads objects"""
    __tablename__ = "url_payload"

class UrlBotnet(IocBaseModel, Base):

    """creates url type iocs with payload objects"""
    __tablename__ = "url_botnet"

