#!/usr/bin/python3
"""Json_storage: instantiates & stores data """
from datetime import datetime
import json
from mitreattack.stix20 import MitreAttackData
import time
from models import storage


mitre_attack_data = MitreAttackData('setup_initialization/json_files/enterprise-attack.json')

def malware_fam(x):
    with open(x, 'r') as mmf:
        m_families = json.load(mmf)
    return (m_families)

def stiix_ref_list(get='', mid='', using='', object_id=""):
    """ return stiix objects as a dict of id: names """
    function_string = 'mitre_attack_data.get_{}_{}_{}("{}")'.format(
        get, mid, using, object_id
    )
    item_list = eval(function_string)

    rtn_dict = {
        x.get('object').get('id'): x.get('object').get('name') 
        for x in item_list
        }
    return (rtn_dict)

def stiix_sort(stiix_obj):#, category):
    """ organizes stiix objects into a list of dicts """
    from dateutil import parser

    obj_keys = [
        'id', 'x_mitre_platforms','description',#'x_type',
        'name','x_mitre_version','x_mitre_contributors'
        ]
    time_tags = [
        'created','modified',
        'first_seen', 'last_seen'
        ]
    references = {
        'group_software': ['groups', 'using', 'software'],
        'campaign_software': ['campaigns', 'using', 'software'],
        'software_group': ['software', 'used_by', 'group'],
        'campaign_group': ['campaigns', 'attributed_to', 'group'],
        'group_campaign': ['groups', 'attributing_to', 'campaign'],
        'software_campaign': ['software', 'used_by', 'campaign']
    }
    alias = [
        'x_mitre_aliases','aliases',
        'external_references', 'x_mitre_platforms'
        ]
    rtn_list = []

    for item in stiix_obj:
        
        item_dict = {}
        obj_name = item.get('type')
        obj_id = item.get('id')

        for key, value in item.items():
            if key in obj_keys:

                item_dict.update({key : value})
            elif key == 'type':
                item_dict.update({'x_type': value})

            elif key in alias:
                    if key == 'external_references':
                        item_dict.update(
                            {key: json.dumps([dict(x) for x in value])}
                            )
                    else:
                        item_dict.update(
                            {key: json.dumps([x for x in value])}
                            )

            elif key in time_tags:
                item_dict.update({key: parser.parse(str(value))})

        for key, value in references.items():
            if obj_name == key.split('_')[1]:
                # value.append(obj_id)
                item_dict.update(
                    {key: json.dumps(stiix_ref_list(*(value + [obj_id])))}
                    )

        rtn_list.append(item_dict)

    return (rtn_list)

def json_org(x):
    ioc_types = [
        'sha3_384_hash.payload',
        'md5_hash.payload',
        'sha1_hash.payload',
        'url.payload_delivery',
        'domain.payload_delivery',
        'ip:port.payload_delivery',
        'url.botnet_cc',
        'domain.botnet_cc',
        'ip:port.botnet_cc',
        'envelope_from.payload_delivery',
        'body_from.payload_delivery',
        'domain.cc_skimming',
        'sha256_hash.payload'
        ]
    with open(x, 'r') as fj:
        ioc_file = json.load(fj)
    dict_ioc = {}
    for ioc in ioc_types:
        ioc_type, threat_type = ioc.split('.')
        ioc_items = {
                ioc:{ v[0].get('ioc_value'): v[0] for v in ioc_file.values() if (
                    v[0].get('ioc_type') == ioc_type and (v[0].get('threat_type') == threat_type)
                    )}
                }

        dict_ioc.update(ioc_items)
    return (dict_ioc)

def ioc_to_sql(serial):
    from models.url_ioc import UrlBotnet, UrlPayload
    from models.domain_ioc import DomainBotnet, DomainPayload, DomainSkimming
    from models.ip_ioc import IpBotnet, IpPayload
    from models.ioc_envelop_body import EnvelopPayload, BodyPayload
    from models.ioc_hashes import Md5Payload, Sha256Payload, Sha3Payload, Sha1Payload
    storage.reload()
    diocs = {
        'url.payload_delivery': UrlPayload,
        'url.botnet_cc': UrlBotnet,
        'domain.payload_delivery': DomainPayload,
        'domain.botnet_cc': DomainBotnet,
        'domain.cc_skimming': DomainSkimming,
        'ip:port.payload_delivery': IpPayload,
        'ip:port.botnet_cc': IpBotnet,
        'envelope_from.payload_delivery': EnvelopPayload,
        'body_from.payload_delivery': BodyPayload,
        'md5_hash.payload': Md5Payload,
        'sha1_hash.payload': Sha1Payload,
        'sha3_384_hash.payload': Sha3Payload,
        'sha256_hash.payload': Sha256Payload
    }
    time = "%Y-%m-%d %H:%M:%S"
    first = 'first_seen_utc'
    last = 'last_seen_utc'
    count = 0
    for key, value in serial.items():
        """ if (count != 0):
            try:
                input("continue?")
            except(EOFError):
                exit() """
        count = 0
        for item in value.values():
            # item['id'] = uuid.uuid4()
            item.update({first: datetime.strptime(item.get(first), time)})
            if item.get(last):
                item.update({last: datetime.strptime(item.get(last), time)})

            storage.new(diocs.get(key)(**item))
            count += 1
            if (count % 1000) == 0:
                storage.save()
                print(f"{key} instance saved : {count}")
            if (count % 100000) == 0:
                storage.close()
                storage.reload()
        storage.save()
        print(f"{key} instance saved : {count}")

def stiix_to_sql():
    """  """
    from models.stiix_data import StiixCampaign,\
        StiixGroup, StiixSoftware
    
    software = mitre_attack_data.get_software(remove_revoked_deprecated=True)
    campaign = mitre_attack_data.get_campaigns(remove_revoked_deprecated=True)
    group = mitre_attack_data.get_groups(remove_revoked_deprecated=True)

    json_objects = {
        'softwares': stiix_sort(software),
        'groups': stiix_sort(group),
        'campaigns': stiix_sort(campaign)
    }

    table_objects = {
        'softwares': StiixSoftware,
        'groups': StiixGroup,
        'campaigns': StiixCampaign
    }

    storage.reload()
    for key, value in json_objects.items():
        count = 0
        for item in value:
            storage.new(table_objects.get(key)(**item))
            count += 1
        storage.save()
        print(f"{key} instance saved : {count}")

def setup_init():
    # stiix_json = 'setup_initialization/enterprise-attack.json'

    stiix_to_sql()
    iocs_json = 'setup_initialization/json_files/full.json'
    ioc_objects = json_org(iocs_json)
    ioc_to_sql(ioc_objects)

if __name__ == "___main__":
    setup_init()
