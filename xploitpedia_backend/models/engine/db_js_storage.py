#!/usr/bin/python3
"""
DB instantiation of models
"""
from os import getenv
from sqlalchemy import create_engine, select
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_models import Base
from models.body_ioc import BodyPayload
from models.envelop_ioc import EnvelopPayload
from models.ip_ioc import IpBotnet, IpPayload
from models.md5_ioc import Md5Payload
from models.sha1_ioc import Sha1Payload
from models.sha3_ioc import Sha3Payload
from models.sha256_ioc import Sha256Payload
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

    # retrieval methods
    def item_get(self, obj=None, id=None, category=None):
        """ retrieves a stiix object by its class name or id """

        stiix_obj = single_obj = None
        if (id): # single item via id
            stiix_obj = self.__session.query(obj).where(obj.id == id)
            single_obj = stiix_obj[0].to_dict()
        if (category): # malware or tools
            stiix_obj = self.__session.query(obj).where(obj.x_type == category)
        else: # other categories without consideration of other 2 parameters
            stiix_obj = self.__session.query(obj)

        return (single_obj if single_obj else stiix_obj)

    '''def ioc_get(self, obj=None, id=None, category=None):
        """ retrieves an ioc object by its cls_name | id | category """
        return ()'''
    
    def stiix_ref_get(self, obj, obj_id):
        """ retrieves all stiix linked objects via id """

        item = self.item_get(obj, obj_id)
        rtn_item = item.to_dict()
        

    def stiix_links_get(self, obj, obj_id):
        """ retrieves all stiix linked objects via id"""
    
    def get_first_item(self, obj):
        """ retrieves first item from a table """

    

