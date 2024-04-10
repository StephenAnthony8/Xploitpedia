#!/usr/bin/python3
""" Campaign route bp / module """
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.stiix_data import StiixCampaign, StiixGroup, StiixSoftware


option = {
    'campaigns': StiixCampaign,
    'groups': StiixGroup,
    'tool': StiixSoftware,
    'malware': StiixSoftware
}

# get one item by id/name
@app_views.route('stiix/<options>/<obj_id>', methods=['GET'])
def get_item_by_name_id(options, obj_id):
    """ retrieves a campaign item by its name or id """
    if options in option:
        """ invalid_items = [
            'x_mitre_contributors', 'x_mitre_version',
            'cls_name'
            ] """

        rtn_obj = storage.item_get(option.get(options), obj_id, item='yes')
        # if (isinstance(rtn_obj, dict)):


        if (isinstance(rtn_obj, option.get(options))):
            return_dict = rtn_obj.to_dict()
            description = rtn_obj.get_description()
            return_dict.update({'description': description})
        else:
            abort(404)
            
        return(jsonify(return_dict))

    abort(404)

# get items linked to a stiix_object
@app_views.route('stiix/<options>/linked_items/<obj_id>', methods=['GET'])
def get_linked_items(options, obj_id):
    """ return all linked items """
    if options in option:
        return_item = storage.stiix_links_get(option.get(options), obj_id)

        return  (jsonify(return_item))
    
    abort(404)

# get reference items linked to a stiix_object
@app_views.route('stiix/<options>/reference_urls/<obj_id>', methods=['GET'])
def get_ref_items(options, obj_id):
    """ retrieve reference urls for an object """
    if options in option:
        rtn_obj = storage.stiix_ref_get(option.get(options), obj_id)

        if (isinstance(rtn_obj, list)):
            return(jsonify(rtn_obj))
    abort(404)

# get first stiix item 
@app_views.route('stiix/<options>/display_item', methods=['GET'])
def get_first_item(options):
    """ returns first item from the list """

    if options in option:
        tag = options if options in ['tool', 'malware'] else None
        return_response = jsonify(
            storage.stiix_get_first_item(option.get(options), tag)#.first()
        )

        return(return_response)
    abort(404)

#get items by category
@app_views.route('stiix/<options>', methods=['GET'])
def get_items_by_category(options):
    """ Retrieves all stiix items by category """

    if options in option:
        category = option.get(options)

        if options in ['tool', 'malware']:
            items = storage.item_get(category).filter(category.x_type == options)
        else:
            items = storage.item_get(category)

        return_items = {item.id: item.name for item in items}
    
        return (jsonify(return_items))

    abort(404)
