import time
from selenium import webdriver
import allure
import pytest

@pytest.mark.positive
def test_katalon_Edge_login():
    driver =webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/"


@pytest.mark.positive
def test_katalon_chrome_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"

@pytest.mark.positive
def test_katalon_firefox_login():
    driver = webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
