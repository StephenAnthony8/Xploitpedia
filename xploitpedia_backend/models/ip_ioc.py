#!/usr/bin/python3
""" Creates Ip ioc objects """
from models.base_models import IocBaseModel, Base

class IpPayload(IocBaseModel, Base):
    """creates Ip type iocs with payloads objects"""
    __tablename__ = "ip_payload"

class IpBotnet(IocBaseModel, Base):

    """creates Ip type iocs with payload objects"""
    __tablename__ = "ip_botnet"

