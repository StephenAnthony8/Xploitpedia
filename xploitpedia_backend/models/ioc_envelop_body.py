#!/usr/bin/python3
""" Creates Body ioc objects """
from models.base_models import IocBaseModel, Base

class BodyPayload(IocBaseModel, Base):
    """creates Body type iocs with payloads objects"""
    __tablename__ = "body_payload"


class EnvelopPayload(IocBaseModel, Base):
    """creates Envelop type iocs with payloads objects"""
    __tablename__ = "envelop_payload"