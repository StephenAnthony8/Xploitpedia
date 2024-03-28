#!/usr/bin/python3
""" Creates sha256 ioc objects """
from models.base_models import IocBaseModel, Base

class Sha256Payload(IocBaseModel, Base):
    """creates sha256 type iocs with payloads objects"""
    __tablename__ = "sha256_payload"