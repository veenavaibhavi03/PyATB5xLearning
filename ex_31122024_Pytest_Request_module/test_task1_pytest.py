import allure
import pytest
import requests
from requests import request

Base_URL="https://restful-booker.herokuapp.com/booking"
_headers ={
    "Content-Type":"application/json"
}

@allure.title("Creating a booking")
@allure.description("creating a booking with valid credentials")
def test_createabooking():
    payload= {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }

    post_request1=requests.post(Base_URL,headers=_headers,json=payload)
    assert post_request1.status_code==200
    assert post_request1.status_code !=201
    pay_load = {
        "firstname": None,
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    post_request2 = requests.post(Base_URL, headers=_headers, json=pay_load)
    json_response=post_request2.json()
    booking_id=json_response["bookingid"]
    assert post_request2.status_code == 500
    post_request=requests.post(Base_URL,headers=_headers,json=pay_load)
    assert post_request.status_code==200
    assert post_request.status_code !=201
    return booking_id