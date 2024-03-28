#!/usr/bin/python3
""" Creates md5 ioc objects """
from models.base_models import IocBaseModel, Base

class Md5Payload(IocBaseModel, Base):
    """creates md5 type iocs with payloads objects"""
    __tablename__ = "md5_payload"