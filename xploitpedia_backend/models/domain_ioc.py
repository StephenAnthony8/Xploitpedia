#!/usr/bin/python3
""" creates domain ioc objects """
from models.base_models import IocBaseModel, Base

class DomainPayload(IocBaseModel, Base):
    """creates Domain type iocs with payloads objects"""
    __tablename__ = "domain_payload"

class DomainBotnet(IocBaseModel, Base):
    """creates Domain type iocs with payload objects"""
    __tablename__ = "domain_botnet"

class DomainSkimming(IocBaseModel, Base):
    """creates Domain type iocs with skimming objects"""
    __tablename__ = "domain_skimming"