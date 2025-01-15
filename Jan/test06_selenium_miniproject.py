import time
from selenium import webdriver
import allure
import pytest

@allure.title("open the app vwo.com")
@pytest.mark.positive
def test_cura_login():
    driver =webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    if "CURA Healthcare Service" in driver.page_source:
        print("Text Found!!, Test case passed !")
    else:
        print("Text Not Found on the page")  # function to specially fail the testcase
        pytest.fail("Text Not Found on the page")