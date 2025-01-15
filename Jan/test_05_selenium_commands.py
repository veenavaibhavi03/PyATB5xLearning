
from selenium import webdriver
import allure
import pytest

@allure.title("open the app vwo.com")
@pytest.mark.positive
def test_vwo_login():
    driver =webdriver.Edge()
    driver.get("https://app.vwo.com")
    print(driver.title)
    print(driver.current_url)
    print(driver.page_source)
    assert driver.title =="Login - VWO"