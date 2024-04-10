#!/usr/bin/python3
""" Creates md5 ioc objects """
from models.base_models import IocBaseModel, Base

class Md5Payload(IocBaseModel, Base):
    """creates md5 type iocs with payloads objects"""
    __tablename__ = "md5_payload"

class Sha1Payload(IocBaseModel, Base):
    """creates sha1 type iocs with payloads objects"""
    __tablename__ = "sha1_payload"

class Sha3Payload(IocBaseModel, Base):
    """creates sha3 type iocs with payloads objects"""
    __tablename__ = "sha3_payload"

class Sha256Payload(IocBaseModel, Base):
    """creates sha256 type iocs with payloads objects"""
    __tablename__ = "sha256_payload"