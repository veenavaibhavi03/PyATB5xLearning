import allure
import pytest
import requests

@allure.title("TC 1 -Create Booking CRUD Positive")
@allure.description("verify the create booking")
@pytest.mark.regression
def  test_Post_request_positive():
    B_URL="https://restful-booker.herokuapp.com"
    Base_path="/booking"
    fullUrl=B_URL+Base_path
    Headers={
        "Content-Type":"application/json"
    }
    Payload={
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
    response_data = requests.post(url=fullUrl,headers=Headers,json=Payload)
    # status code verification
    assert response_data.status_code == 200
    #booking id >0
    response_data_json=response_data.json()
    bookingId=response_data_json["bookingid"]
    assert bookingId >0
    assert bookingId is not None
    assert type(bookingId) == int

    firstname=response_data_json["booking"]["firstname"]
    Lastname=response_data_json["booking"]["lastname"]
    TotalPrice=response_data_json["booking"]["totalprice"]
    Depositpaid=response_data_json["booking"]["depositpaid"]
    Checkin=response_data_json["booking"]["bookingdates"]["checkin"]
    Checkout=response_data_json["booking"]["bookingdates"]["checkout"]
    assert firstname=="Jim"
    assert Lastname=="Brown"
    assert type(firstname)==str
    assert Checkin=="2018-01-01"
    assert Checkout=="2019-01-01"
    assert TotalPrice==111
    assert Depositpaid==True

@allure.title("TC 2-Create Booking CRUD Negative")
@allure.description("verify the create booking")
@pytest.mark.regression
def  test_Post_request_Negativetc1():
    B_URL="https://restful-booker.herokuapp.com"
    Base_path="/booking"
    fullUrl=B_URL+Base_path
    Headers={
        "Content-Type":"application/json"
    }
    Payload={ }
    response_data = requests.post(url=fullUrl,headers=Headers,json=Payload)
    # status code verification
    assert response_data.status_code == 500
    print(response_data.text)
    assert response_data.text== "Internal Server Error"


@allure.title("TC 1 -Create Booking CRUD Positive")
@allure.description("verify the create booking")
@pytest.mark.regression
def test_Post_request_positive():
    B_URL = "https://restful-booker.herokuapp.com"
    Base_path = "/booking"
    fullUrl = B_URL + Base_path
    Headers = {
        "Content-Type": "application/json"
    }
    Payload = {
        "firstname": " ",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response_data = requests.post(url=fullUrl, headers=Headers, json=Payload)
    # status code verification
    assert response_data.status_code == 500
    # booking id >0
    response_data_json = response_data.json()
    Firstname=response_data_json["booking"]["firstname"]
    assert Firstname == None

