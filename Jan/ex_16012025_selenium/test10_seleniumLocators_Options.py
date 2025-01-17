"""https://katalon-demo-cura.herokuapp.com/profile.php#login
   <a
   id="btn-make-appointment"
   href="./profile.php#login"
   class="btn btn-dark btn-lg">
   Make Appointment
   </a>
   """
import time
from selenium import webdriver
import allure
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@allure.title("open the Katalon demo")
@pytest.mark.positive
def test_katalon_chrome():

    chrome_options=Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment_button =driver.find_element(By.ID,"btn-make-appointment")
    make_appointment_button.click()
    time.sleep(5)
    assert driver.current_url =="https://katalon-demo-cura.herokuapp.com/profile.php#login"
    driver.quit()

