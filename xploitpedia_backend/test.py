#!/usr/bin/python3
""" from setup_initialization.json_storage import setup_init
setup_init() """

from models import storage
from models.stiix_data import StiixSoftware

x = storage.item_get(
    StiixSoftware, category='tool'#, 'campaign--df74f7ad-b10d-431c-9f1d-a2bc18dadefa'
    )
# print(type(x[0]))
[print(f'{key}: {value}\n')for key, value in x[0].get_description().items()]
# print(x[0].get_description()[0][0])
#[print(f'{_}\n') for _ in x[0].get_description()]
print('------------------------------------------------------------------')
print(x[0].description)

""" 

[print(f'{key}: {value}') for key, value in x[1].to_dict().items()] """
