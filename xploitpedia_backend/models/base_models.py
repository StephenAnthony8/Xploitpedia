#!/usr/bin/python3
"""
Base_models:
Creates all relevant base model objects
- Ioc objects
- Stixx objects
"""
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Integer, Float, JSON
from sqlalchemy.ext.declarative import declarative_base
import uuid
import json
import re

Base = declarative_base()

class IocBaseModel:
    """Base Model class from which all IOC objects inherit"""

    id = Column(String(60), primary_key=True, default=uuid.uuid4)
    ioc_value = Column(String(512), nullable=False)
    ioc_type = Column(String(512), nullable=False)
    threat_type = Column(String(60), nullable=False)
    malware = Column(String(128), nullable=False)
    confidence_level = Column(Integer, nullable=False)
    malware_printable = Column(String(128), nullable=False)
    reporter = Column(String(60), nullable=False)
    first_seen_utc = Column(DateTime, nullable=False)
    tags = Column(String(512), nullable=True)
    reference = Column(String(512), nullable=True)
    last_seen_utc = Column(DateTime, nullable=True)
    malware_alias = Column(String(512), nullable=True)
    anonymous = Column(String(128), nullable=True)


    def to_dict(self):
        """ returns a dictionary version of the input """
        dict_items = {}

        for key, value in self.__dict__.items():
            if key in ['first_seen_utc', 'last_seen_utc'] and value is not None:
                dict_items.update({key: value.isoformat()[:10]})
            else:
                dict_items.update({key: value})
        return(dict_items)


class StiixBaseModel:
    """Base Model class from which all Stiix objects inherit"""
    id = Column(String(60), primary_key=True)
    x_type = Column(String(60), nullable=False)
    
    description = Column(String(2048), nullable=False)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    name = Column(String(60), nullable=False)
    x_mitre_version = Column(Float)
    external_references = Column(JSON, nullable=False)
    x_mitre_contributors = Column(JSON, nullable=True)


    """ def __str__(self): """


    def to_dict(self):
        """ converts all objects to their dictionary format """
        
        json_items = [
            'external_references', 'x_mitre_contributors',
            'x_mitre_platforms', 'x_mitre_aliases', 'aliases',
            'group_software', 'campaign_software',
            'software_group', 'campaign_group',
            'group_campaign', 'software_campaign'
            ]
        dict_items = {}
        for key, value in self.__dict__.items():
            # print(f'{type(value)}: {value}')
            if key in json_items:
                if isinstance(value, str):
                    dict_items.update(
                        {key: json.loads(value)}
                    )
                elif value is None:
                    dict_items.update({key: 'data unavailable'})
            elif key == 'x_type':
                dict_items.update({'type': value})
            else:
                if key not in ['x_mitre_version', 'cls_name', '_sa_instance_state']:
                    if key in ['created', 'modified']:
                        dict_items.update({key: value.isoformat()[:10]})
                    else:
                        dict_items.update({key: value})
        return (dict_items)

    def get_external_references(self):
        """ returns a dict from 'external_references json """
        item = [{
            'source_name':'unknown',
            'url': 'unknown'
            }]
        if self.external_references: 
            if isinstance(self.external_references, list) is False:
                item = json.loads(self.external_references)
            else:
                item = self.external_references
        return (item)

    def get_description(self):
        """ returns the description string stripped of links """
        rtn = {
            'name': 'unknown',
            'link': 'unknown',
            'string': 'unknown'
        }

        if self.description:
            resources  = re.findall(
                r"(\[[\w/ ]*\])\((https?:[\w/.-]*)\)", self.description)
            # citation = re.findall(r"", self.description)

            rtn = {x[0]: x[1] for x in resources}

            rtn['string'] = re.subn(
                r'\(https?:[\w/.-]*\)',
                '',
                self.description
                )[0].split('(Citation:')[0]
            
            
            return (rtn)#, citation)#, y)


    """ lists (Use a JSON column)
    # x_mitre_contributors = Column() # software exclusive parameter
    # labels = Column() #software exclusive parameter
    # x_mitre_aliases = Column() # software exclusive parameter
    """

    """ groups parameters 
    # aliases """

    """ campaigns parameters
     # first_seen
    # last_seen
    # aliases : group reference
    #  """

    """ to be ignored 
     # created_by_ref = Column()
    # revoked = Column()
    # object_marking_refs = Column()
    # x_mitre_attack_spec_version = Column()
    # x_mitre_deprecated = Column()
    # x_mitre_domains = Column()
    # x_mitre_modified_by_ref = Column() """

