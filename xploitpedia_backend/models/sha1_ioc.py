#!/usr/bin/python3
""" Creates sha1 ioc objects """
from models.base_models import IocBaseModel, Base

class Sha1Payload(IocBaseModel, Base):
    """creates sha1 type iocs with payloads objects"""
    __tablename__ = "sha1_payload"