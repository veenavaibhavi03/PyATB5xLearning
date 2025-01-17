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

    free_trial=driver.find_element(By.CLASS_NAME,"text-link")
    free_trial.click()
    time.sleep(5)
    assert driver.current_url ==os.getenv("currentUrl")


    #assert error_Message.text==os.getenv("ErrorMessage")

    """make_appointment_button =driver.find_element(By.ID,"btn-make-appointment")
    make_appointment_button.click()"""
  
    
    driver.quit()

