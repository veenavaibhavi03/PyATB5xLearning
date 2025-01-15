import time
from selenium import webdriver
import allure
import pytest

@allure.title("open the app vwo.com")
@pytest.mark.positive
def test_katalon_Edge():
    driver =webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(7)
    assert driver.current_url =="https://katalon-demo-cura.herokuapp.com/"
    driver.quit()

