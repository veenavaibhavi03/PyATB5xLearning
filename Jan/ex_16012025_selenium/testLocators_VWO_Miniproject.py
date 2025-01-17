import time
from os import getenv

from dotenv import load_dotenv

from selenium import webdriver
import allure
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os

@allure.title("open the Katalon demo")
@pytest.mark.positive
def test_katalon_chrome():
    load_dotenv()
    chrome_options=Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(chrome_options)
    driver.get(getenv("Url"))

    user_name=driver.find_element(By.ID,"login-username")
    user_name.send_keys(os.getenv("Invalid_username"))
    time.sleep(5)

    user_password= driver.find_element(By.NAME, "password")
    user_password.send_keys(os.getenv("Invalid_password"))
    time.sleep(5)

    user_signin=driver.find_element(By.ID,"js-login-btn")
    user_signin.click()
    time.sleep(5)

    error_Message=driver.find_element(By.ID,"js-notification-box-msg")
    #print(error_Message.text)
    assert error_Message.text==os.getenv("ErrorMessage")

    """make_appointment_button =driver.find_element(By.ID,"btn-make-appointment")
    make_appointment_button.click()
  
    assert driver.current_url =="""
    driver.quit()

