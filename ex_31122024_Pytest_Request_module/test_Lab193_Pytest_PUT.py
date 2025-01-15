import allure
import pytest
import requests


base_url="https://restful-booker.herokuapp.com"
Headers = {
        "Content-Type": "application/json"
    }

def create_token():
    path="/auth"
    URL=base_url+path

    payload={
            "username": "admin",
            "password": "password123"
        }
    responsebody=requests.post(url=URL, headers=Headers,json=payload)
    Token=responsebody.json()["token"]
    print(Token,len(Token))
    assert responsebody.status_code==200
    assert type(Token) == str
    assert len(Token) <=15
    return Token

def get_booking_id():
    path="/booking"
    URL=base_url+path
    request_body={
    "firstname" : "Jim ",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    response_body=requests.post(url=URL,headers=Headers,json=request_body)
    booking_id=response_body.json()["bookingid"]
    return booking_id


@allure.description("This verifies if the token is created with valid credentials")
@pytest.mark.regression
def test_PUT_request1():
    token=create_token()
    booking_id=get_booking_id()
    path="/booking/"+str(booking_id)
    URl=base_url+path
    cookie ="token="+token
    Headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    request_body = {
        "firstname": "James ",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response_body=requests.put(url=URl,headers=Headers,json=request_body)
    json_response=response_body.json()
    print(response_body)
    assert response_body.status_code==200
    assert json_response["firstname"]=="James"


def test_DELETE_request():
    token = create_token()
    booking_id = get_booking_id()
    path = "/booking/" + str(booking_id)
    URl = base_url + path
    cookie = "token=" + token
    Headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    response_body = requests.delete(url=URl, headers=Headers)
    assert response_body.status_code==201

