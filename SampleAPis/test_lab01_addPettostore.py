

import allure
import  pytest
import requests
from requests import request

"""def test_storeinventory():
    url="https://petstore.swagger.io/v2/store/inventory"
    Headers={
        "accept": "application/json"
    }
    response_body=requests.get(url,Headers)
    assert response_body.status_code==200
"""

base_url="https://petstore.swagger.io/v2/pet"
Headers={
    "accept": "application/json",
    "Content-Type":"application/json"
    }

def  addpettostore():
    pay_load= {
            "id": 0,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": "doggie",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
    }
    body_response=requests.post(base_url,headers=Headers,json=pay_load)
    json_response=body_response.json()
    petId=json_response["id"]
    return petId


def test_updatepet():
    payload={
        "id": 0,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "pinky",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "pinky"
            }
        ],
        "status": "available"
    }
    body_response = requests.put(base_url, headers=Headers, json=payload)
    assert body_response.status_code==200

def test_findpetbystatus():
    status = ["pending", "available", "sold"]

    path_url="/findByStatus?status="+status[1]
    url=base_url+path_url
    b_response=requests.get(url,Headers)
    assert b_response.status_code==200

def test_deletepet():
    ID=addpettostore()
    pathurl="/"+str(ID)
    full_url=base_url+pathurl
    bresponse=requests.delete(full_url,headers=Headers)
    assert bresponse.status_code==200




