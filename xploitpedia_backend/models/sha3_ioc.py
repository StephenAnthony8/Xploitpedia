#!/usr/bin/python3
""" Creates sha3 ioc objects """
from models.base_models import IocBaseModel, Base

class Sha3Payload(IocBaseModel, Base):
    """creates sha3 type iocs with payloads objects"""
    __tablename__ = "sha3_payload"