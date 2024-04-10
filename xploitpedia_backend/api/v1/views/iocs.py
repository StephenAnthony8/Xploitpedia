#!/usr/bin/python3
from models.ioc_envelop_body import BodyPayload, EnvelopPayload
from models.ip_ioc import IpBotnet, IpPayload
from models.ioc_hashes import Md5Payload, Sha1Payload, Sha3Payload,\
    Sha256Payload
from models.domain_ioc import DomainBotnet, DomainPayload,\
    DomainSkimming
from models.url_ioc import UrlBotnet, UrlPayload
from flask import abort, jsonify, make_response, request
from api.v1.views import app_views
from models import storage
import requests
from json import dumps
""" Filter limit is 10 - 20 items per request """
ioc_objects = {
    'Payload': [BodyPayload, EnvelopPayload, IpPayload, DomainPayload, UrlPayload],
    'Botnet': [IpBotnet, DomainBotnet, UrlBotnet],
    'Hash': [Md5Payload, Sha1Payload, Sha256Payload, Sha3Payload],
    'Skimming': [DomainSkimming]
}

# get all items by filter limit
#@app_views.route('iocs/<iocs>', methods=['GET'])
@app_views.route('iocs/list/<iocs>/<specific>', methods=['GET'])
def iocs_items_category(iocs, specific=None):
    """ Returns ioc objects by category """
    next = 0
    return_items = {}
    ioc_obj = ioc_objects.get(iocs)

    if (ioc_obj) :
        # check for filter limit & start/end filter parameters
        try:
            if iocs == "Hash":
                iocs = 'Payload'
            obj = eval(f'{specific}{iocs}')
            count = storage.get_count(obj)
            next = int(request.args.get('next')) if request.args.get('next') is not None else 0
            # if next:
            if (next > count):
                err_response = make_response(
                    jsonify({'error':"Invalid Query parameter 1"}), 403
                )
                return (err_response)
            return_query = storage.item_get(obj).offset(next).limit(20)

            

            return_items = {ioc.malware_printable: ioc.id for ioc in return_query}
            # return_items.update({'next': next + 20})

            response = make_response(jsonify(return_items))
            response.headers['next'] = next + 20 if next + 20 < count else 'end'
            response.headers['current'] = next

            return(response)

        except (TypeError, NameError):
            err_response = make_response(
                jsonify({'error': 'Invalid Query parameter'}), 403
            )
            return(err_response)
    abort(404)

# get single item by id & category
@app_views.route('iocs/<iocs>/<id>', methods=['GET'])
def get_ioc_id(iocs, id):
    """ retrieve an ioc by id """

    categories = ioc_objects.get(iocs)

    if categories:
        return_item = {}
        for object in categories:
            return_obj = storage.item_get(object, id)
            if isinstance(return_obj, dict):
                # configure date time objects 
                for key, value in return_obj.items():
                    if key not in ['_sa_instance_state', 'tags', 'anonymous']:
                        return_item.update({key: value})
                    
                    elif key == 'malware_printable':
                        return_item.update({'name': value})
                # returns a dict of the ioc item
                return (jsonify(return_item))
    abort(404)

# get recent iocs
@app_views.route('/iocs/recents', methods=['GET'])
def get_recent_iocs():
    """ return all recent iocs (7 days) """
    query_tags = dumps({"query": "get_iocs", "days": 7})

    recent_iocs = requests.post(
        'https://threatfox-api.abuse.ch/api/v1/', data=query_tags)
    
    if recent_iocs.reason == 'OK':
        # returns a list of the recent iocs
        return (jsonify(recent_iocs.json().get('data')))

# get iocs by search NAME query
@app_views.route('/iocs/search/<ioc_category>/<search_option>', methods=['GET'])
def query_ioc_filter(ioc_category, search_option):#, ioc_option, filter_option):
    """ search iocs via filter """
    # start with name, include other options later
    search_option = search_option.replace('+', ' ')
    search_category = ioc_objects.get(ioc_category)
    search_object = {}
    if search_category:
        for object in search_category:
            item_list = storage.item_get(object).filter(object.malware_printable == search_option)
            search_object.update(
                {f'{item.malware}--{item.ioc_value}': item.id for item in item_list}
                )
        if search_object:
            return (jsonify(search_object))
        else:
            abort(404)

    else:
        abort(404)
