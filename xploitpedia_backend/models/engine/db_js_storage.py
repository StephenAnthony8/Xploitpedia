#!/usr/bin/python3
"""
DB instantiation of models
"""
from os import getenv
from sqlalchemy import create_engine, select
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_models import Base
from models.ioc_envelop_body import BodyPayload, EnvelopPayload
from models.ip_ioc import IpBotnet, IpPayload
# hashes
from models.ioc_hashes import Md5Payload, Sha1Payload, Sha3Payload,\
    Sha256Payload
from models.domain_ioc import DomainBotnet, DomainPayload,\
    DomainSkimming
from models.stiix_data import StiixCampaign, StiixGroup,\
    StiixSoftware


class MySqJson:
    """ Db storage object """

    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = 'x_user'#getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = 'x_user_pwd'#getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = 'localhost'#getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = 'xploitpedia'#getenv('HBNB_MYSQL_DB')
        HBNB_ENV = 'prod'#'getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    # orm methods
    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
    
    # Stiix / ioc methods
    def get_count(self, obj):
        """ Returns a count of all objects within a table """
        return (self.__session.query(obj).count())

    def item_get(self, obj=None, id=None, category=None, item=None):
        """ retrieves a stiix object by its class name or id """

        stiix_obj = single_obj = None
        if (id): # single item via id
            stiix_obj = self.__session.query(obj).where(obj.id == id).first()
            if (stiix_obj):
                single_obj= stiix_obj if item else stiix_obj.to_dict()
            else:
                return None
        if (category): # malware or tools
            stiix_obj = self.__session.query(obj).where(obj.x_type == category)
        else: # other categories without consideration of other 2 parameters
            stiix_obj = self.__session.query(obj)

        return (single_obj if single_obj else stiix_obj)

    '''def ioc_get(self, obj=None, id=None, category=None):
        """ retrieves an ioc object by its cls_name | id | category """
        return ()'''
    
    # stiix methods
    def stiix_ref_get(self, obj, obj_id):
        """ retrieves all stiix linked objects via id """

        item = self.item_get(obj, obj_id)
        rtn_item = []
        for ref in item.get('external_references'):
            if (ref.get('url')):
                rtn_item.append(
                    {'name': ref.get('source_name'), 'link': (ref.get('url'))}
                    )


        return (rtn_item)


    def stiix_links_get(self, obj, obj_id):
        """ retrieves all stiix linked objects via id"""

        stiix_keys = [
            'group_software', 'group_campaign',
            'campaign_software', 'campaign_group',
            'software_group', 'software_campaign'
        ]

        link_dict = {
            'intrusion-set'
        }
        rtn_list =[]
        #item = 
        rtn_item = self.item_get(obj, obj_id)
        rtn_item_keys = rtn_item.keys()
        for item in stiix_keys:
            if item in rtn_item_keys and isinstance(rtn_item.get(item), dict):
                rtn_list.append({'name':item, 'content': [{'id': key, "name": value} for key, value  in rtn_item.get(item).items()]})
            elif item in rtn_item_keys and isinstance(rtn_item.get(item), str):
                rtn_list.append({'name':item, 'content': []}) 
        
        return (rtn_list)
    
    def stiix_get_first_item(self, obj=None, tag=None):
        """ retrieves first item from a table """

        if obj:
            return_list = ['id', 'name', 'description', 'type', 'created']
            return_item = {}
            if tag:
                item = self.__session.query(obj).filter(obj.x_type == tag).first()
            else:
                item = self.__session.query(obj).first()
            item_dict = item.to_dict()
            for key in return_list:
                if key == 'description':
                    return_item.update({key: item.get_description().get('string')})
                else:
                    return_item.update({key: item_dict.get(key)})

            return (return_item)
        return (None)

    

