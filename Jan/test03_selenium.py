import time

from selenium import webdriver
import allure
import pytest

@allure.title("open the app vwo.com")
@pytest.mark.positive
def test_vwo_login():
    driver =webdriver.chrome()  # this code is translated into API request
    #POST request -browser driver (server)
    # It will create a new session(fresh copy of browser) and  a session id is created -16 digit
    driver.get("https://app.vwo.com")
    # GET - GET API request to navigate to particular page
    # browser will navigate to The URL

    time.sleep(15)