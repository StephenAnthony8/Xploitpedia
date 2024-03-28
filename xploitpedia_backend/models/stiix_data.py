#!/usr/bin/python3
""" Creates all stiix objects """

from models.base_models import StiixBaseModel, Base
from sqlalchemy import JSON, String, Column, DateTime
from datetime import datetime


class StiixSoftware(StiixBaseModel, Base):
    """ creates stiix sofware objects """
    __tablename__ = "stiix_software"
    # labels = Column(JSON, nullable=False)
    x_mitre_platforms = Column(JSON, nullable=True)
    x_mitre_aliases = Column(JSON, nullable=True) # software exclusive parameter
    # get_groups_using_software()
    group_software = Column(JSON, nullable=True) # dict obj of group_id : [campaign_id]
    # get_campaigns_using_software()
    campaign_software = Column(JSON, nullable=True)

    cls_name = 'softwares'

class StiixGroup(StiixBaseModel, Base):
    """ creates stiix group objects """
    __tablename__ = "stiix_group"
    aliases = Column(JSON, nullable=True)
    # get_software_used_by_group()
    software_group = Column(JSON, nullable=True) # dict of campaign_id : [software_id]
    # get_campaigns_attributed_to_group()
    campaign_group = Column(JSON, nullable=True)

    cls_name = 'groups'

class StiixCampaign(StiixBaseModel, Base):
    """ creates stiix campaign objects """
    __tablename__ = "stiix_campaign"
    first_seen = Column(DateTime, nullable=False)
    last_seen = Column(DateTime, nullable=False)
    aliases = Column(JSON, nullable=True)
    # get_groups_attributing_to_campaign()
    group_campaign = Column(JSON, nullable=True) # dict of group_id : [software_id]
    # get_software_used_by_campaign()
    software_campaign = Column(JSON, nullable=True)

    cls_name = 'campaigns'


