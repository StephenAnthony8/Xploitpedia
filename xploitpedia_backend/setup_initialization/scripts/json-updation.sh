#!/usr/bin/env bash
# updates all json files used for storage

curl -x GET https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json > ../models/storage/json_files/enterprise-attack.json

# malware families
curl -X GET https://malpedia.caad.fkie.fraunhofer.de/api/get/families > ../models/storage/json_files/malpedia-malware_families.json

# obtain most recent iocs
curl -X POST https://threatfox-api.abuse.ch/api/v1/ -d '{ "query": "get_iocs", "days": 7 }' > ../models/storage/json_files/recent_iocs.json

# obtain ioc types 
curl -X POST https://threatfox-api.abuse.ch/api/v1/ -d '{ "query": "types" }' > ../models/storage/json_files/ioc_types.json

# obtain all iocs(zip) via all descriptions
curl -X GET https://threatfox.abuse.ch/export/json/full/ > ../models/storage/zip_files/all_data.zip && mkdir -p ../models/storage/zip_files/all_data && unzip -d ../models/storage/zip_files/all_data ../models/storage/zip_files/all_data.zip