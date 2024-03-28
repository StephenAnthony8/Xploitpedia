#!/usr/bin/python3
""" Creates Envelop ioc objects """
from models.base_models import IocBaseModel, Base

class EnvelopPayload(IocBaseModel, Base):
    """creates Envelop type iocs with payloads objects"""
    __tablename__ = "envelop_payload"