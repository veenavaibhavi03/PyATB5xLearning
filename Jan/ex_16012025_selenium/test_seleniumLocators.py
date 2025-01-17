import time
from selenium import webdriver
import allure
import pytest
from selenium.webdriver.common.by import By
@allure.title("open the Katalon demo")
@pytest.mark.positive
def test_katalon_chrome():
    driver =webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    """
    https://katalon-demo-cura.herokuapp.com/profile.php#login
    <a 
    id="btn-make-appointment" 
    href="./profile.php#login" 
    class="btn btn-dark btn-lg">
    Make Appointment
    </a>
    """
    make_appointment_button =driver.find_element(By.ID,"btn-make-appointment")
    make_appointment_button.click()

    assert driver.current_url =="https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(7)
    driver.quit()

