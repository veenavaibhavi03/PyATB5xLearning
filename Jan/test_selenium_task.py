import time
from selenium import webdriver
import allure
import pytest

@allure.title("open the demo.us.espocrm.com")
@pytest.mark.positive
def test_espocrm_login():
    driver =webdriver.Chrome()
    driver.get("https://demo.us.espocrm.com/")
    time.sleep(6)
    assert driver.current_url== "https://demo.us.espocrm.com/"
    assert driver.title == "EspoCRM Demo"
