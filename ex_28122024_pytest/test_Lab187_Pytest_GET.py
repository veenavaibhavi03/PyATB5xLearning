from types import NoneType

import allure
import pytest
import requests

@allure.title("Get request  for RESTFUL BOOKER")
@allure.description("This test attempts to check the status code of the request with valid id")
@pytest.mark.getrequestpositive
def  test_get_request_positive():
    URL="https://restful-booker.herokuapp.com/booking/1"
    response_data=requests.get(url=URL)
    assert response_data.status_code==200

@allure.title("Get request  for RESTFUL BOOKER")
@allure.description("This test attempts to check the status code of the request with invalid id ")
@pytest.mark.getrequestpositive
def  test_get_request_negative1():
    Url_get="https://restful-booker.herokuapp.com/booking/-1"
    response_data=requests.get(url=Url_get)
    assert response_data.status_code==404


@allure.title("Get request  for RESTFUL BOOKER")
@allure.description("This test attempts to check the status code of the request with invalid id ")
@pytest.mark.getrequestpositive
def  test_get_request_negative2():
    Url_get="https://restful-booker.herokuapp.com/booking/0"
    response_data=requests.get(url=Url_get)
    assert response_data.status_code == 404

@allure.title("Get request  for RESTFUL BOOKER")
@allure.description("This test attempts to check the status code of the request with invalid id ")
@pytest.mark.getrequestpositive
def  test_get_request_negative3():
    Url_get="https://restful-booker.herokuapp.com/booking/abc"
    response_data=requests.get(url=Url_get)
    assert response_data.status_code == 404


@allure.title("Get request  for RESTFUL BOOKER")
@allure.description("This test attempts to check the status code of the request with invalid id ")
@pytest.mark.getrequestpositive
def  test_get_request_negative4():
    Url_get="https://restful-booker.herokuapp.com/booking/ab12"
    response_data=requests.get(url=Url_get)
    assert response_data.status_code == 404

@allure.title("Get request  for RESTFUL BOOKER")
@allure.description("This test attempts to check the status code of the request with invalid id ")
@pytest.mark.getrequestpositive
def  test_get_request_negative5():
    Url_get="https://restful-booker.herokuapp.com/booking/أَبْجَدِيّ"
    response_data=requests.get(url=Url_get)
    assert response_data.status_code == 200







