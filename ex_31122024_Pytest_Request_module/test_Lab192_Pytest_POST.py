import allure
import pytest
import requests
from dotenv import load_dotenv
import os

base_url="https://restful-booker.herokuapp.com"
Headers = {
        "Content-Type": "application/json"
    }
@allure.title("TC 1-verify the create token ")
@allure.description("This verifies if the token is created with valid credentials")
@pytest.mark.regression
def test_create_token():
    load_dotenv()

    payload = {
        "username":os.getenv("USER_NAME"),
        "password" :os.getenv("PASS_WORD")
    }

    print(os.getenv("USERNAME"))
    print(os.getenv("PASSWORD"))

    path="/auth"
    URL=base_url+path
    responsebody=requests.post(url=URL, headers=Headers,json=payload)
    Token=responsebody.json()["token"]
   # print(Token,len(Token))
    assert responsebody.status_code==200
    assert type(Token) == str
    assert len(Token) <=15
    return payload

test_create_token()
