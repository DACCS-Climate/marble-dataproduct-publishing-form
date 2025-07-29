import shutil
import tempfile
from pathlib import Path

from pystac import Catalog, get_stac_version
from pystac import collection as pystac_collection
import pystac

client = MarbleClient()

form_result = "title=Test Title for Productq&desc=Here is a longer description of what it does&date=2024-12-19&fname=Cassandra&lname=Chanen&email[]=cassandra.chanen@gmail.com&geometry=Polygon&bbox1=-45&bbox2=45&bbox3=-180&bbox4=180&start_date=1980-01-01&end_date=2000-01-01&vehicle1=Bike&vehicle1=Bike&path=/mypublic/file/here&input=www.cmiplink.redoak&link="
fdict = {}
form = form_result.split("&")
for i in range(len(form)):
    var = form[i]
    var_list = var.split("=")
    fdict[var_list[0]] = var_list[1]
print(fdict)
"""
{'title': 'Test Title for Productq', 'desc': 'Here is a longer description of what it does', 'date': '2024-12-19', 'fname': 'Cassandra', 'lname': 'Chanen', 'email[]': 'cassandra.chanen@gmail.com', 'geometry': 'Polygon', 'bbox1': '-45', 'bbox2': '45', 'bbox3': '-180', 'bbox4': '180', 'start_date': '1980-01-01', 'end_date': '2000-01-01', 'vehicle1': 'Bike', 'path': '/mypublic/file/here', 'input': 'www.cmiplink.redoak', 'link': ''}
"""
# Setting up geometry
if fdict["geometry"] == "Point":
    item_bbox = [fdict["bbox1"], fdict["bbox2"]]
    item_coords = [fdict["bbox1"], fdict["bbox2"]]
if fdict["geometry"] == "Polygon":
    item_bbox = [fdict["bbox3"], fdict["bbox1"], fdict["bbox4"], fdict["bbox2"]]
    item_coords = [[fdict["bbox3"], fdict["bbox1"]], [fdict["bbox4"], fdict["bbox1"]], [fdict["bbox4"], fdict["bbox2"]],
                   [fdict["bbox3"], fdict["bbox2"]], [fdict["bbox3"], fdict["bbox1"]]]
if fdict["geometry"] == "null":
    item_bbox = null
    item_coords = null

# Setting Properties
from datetime import datetime

item_properties = {
    # date
    "datetime": None,
    "start_datetime": fdict["start_date"],
    "end_datetime": fdict["end_date"],
    "created": fdict["date"],
    # variables
    "variables": [
        "temperature",
        "pressure"
    ],
    # instruments
    "instruments": [
        "example"
    ],
    # models
    "models": [
        "example"
    ],
    "item_links": [{
        "rel": "self",
        "href": fdict["path"]
    },
        {
            "rel": "collection",
            "href": "https://landsat-stac.s3.amazonaws.com/landsat-8-l1/catalog.json"
        },
        {
            "rel": "parent",
            "href": "https://landsat-stac.s3.amazonaws.com/landsat-8-l1/107/018/catalog.json"
        },
        {
            "rel": "root",
            "href": "https://landsat-stac.s3.amazonaws.com/catalog.json"
        },
        {
            "rel": "derived_from",
            "href": [fdict["input"]]
        },
        {
            "rel": "linked_files",
            "href": [fdict["link"]]
        }]
}

##%%
item = pystac.Item(
    id = str(fdict["lname"]) + '-' + fdict["title"][:fdict["title"].find(" ")] + '-' + fdict["date"],
    geometry = {
           "type": fdict["geometry"],
           "coordinates": item_coords
       },
    bbox = item_bbox,
    datetime = None,
    properties=item_properties
)

import json
print(json.dumps(item.to_dict(), indent=4))
"""
{
    "type": "Feature",
    "stac_version": "1.0.0",
    "id": "Chanen-Test-2024-12-19",
    "properties": {
        "datetime": null,
        "start_datetime": "1980-01-01",
        "end_datetime": "2000-01-01",
        "created": "2024-12-19",
        "variables": [
            "temperature",
            "pressure"
        ],
        "instruments": [
            "example"
        ],
        "models": [
            "example"
        ],
        "item_links": [
            {
                "rel": "self",
                "href": "/mypublic/file/here"
            },
            {
                "rel": "collection",
                "href": "https://landsat-stac.s3.amazonaws.com/landsat-8-l1/catalog.json"
            },
            {
                "rel": "parent",
                "href": "https://landsat-stac.s3.amazonaws.com/landsat-8-l1/107/018/catalog.json"
            },
            {
                "rel": "root",
                "href": "https://landsat-stac.s3.amazonaws.com/catalog.json"
            },
            {
                "rel": "derived_from",
                "href": [
                    "www.cmiplink.redoak"
                ]
            },
            {
                "rel": "linked_files",
                "href": [
                    ""
                ]
            }
        ]
    },
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
                "-180",
                "-45"
            ],
            [
                "180",
                "-45"
            ],
            [
                "180",
                "45"
            ],
            [
                "-180",
                "45"
            ],
            [
                "-180",
                "-45"
            ]
        ]
    },
    "links": [],
    "assets": {},
    "bbox": [
        "-180",
        "-45",
        "180",
        "45"
    ],
    "stac_extensions": []
}
"""