import time
from itertools import dropwhile
from allure_commons import fixture
from dotenv import load_dotenv
from selenium import webdriver
import allure
import pytest
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@allure.title("Login into espocrm")
@allure.description("verify if login  works")
@pytest.mark.positive
def test_espocrm_login():
    load_dotenv()
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    driver =webdriver.Chrome(chrome_options)
    driver.get(os.getenv("espo_url"))
    time.sleep(6)

    #button type="submit" class="btn btn-primary btn-s-wide" id="btn-login">Login</button>
    login_element=driver.find_element(By.ID,"btn-login")
    login_element.click()
    print(driver.current_url)
    time.sleep(5)

    time.sleep(7)
    #assert driver.current_url==os.getenv("espo_current_url")

@allure.title("click on Advanced Pack")
@allure.description("verify if Hyperlink works for Advanced Pack")
@pytest.mark.positive
def test_espocrm_advancedPack():
    load_dotenv()
    chrome_options = Options()
    driver =webdriver.Chrome(chrome_options)
    driver.get(os.getenv("espo_url"))
    time.sleep(6)
    #<a href="https://www.espocrm.com/extensions/advanced-pack/"
    # target="_blank">Advanced Pack</a>
    login_element=driver.find_element(By.LINK_TEXT,"Advanced Pack")
    login_element.click()
    time.sleep(5)
   #<a data-name="logout" role="button" tabindex="0" class="nav-link action">Log Out</a>
    time.sleep(7)


@allure.title("click on Sales Pack")
@allure.description("verify if Hyperlink works for Sales Pack")
@pytest.mark.positive
def test_espocrm_salesPack():
    load_dotenv()
    chrome_options = Options()
    driver =webdriver.Chrome(chrome_options)
    driver.get(os.getenv("espo_url"))
    time.sleep(6)
    #< a
    #href = "https://www.espocrm.com/extensions/sales-pack/"
    #target = "_blank" > Sales
    #Pack < / a >
    login_element=driver.find_element(By.LINK_TEXT,"Sales Pack")
    login_element.click()
    time.sleep(5)
   #<a data-name="logout" role="button" tabindex="0" class="nav-link action">Log Out</a>
    driver.quit()


@allure.title("click on Project Mangement")
@allure.description("verify if Hyperlink works for Project Management")
@pytest.mark.positive
def test_espocrm_ProjectManagement():
    load_dotenv()
    chrome_options = Options()
    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("espo_url"))
    time.sleep(6)
    # <a href="https://www.espocrm.com/extensions/project-management/"
    # target="_blank">Project Management</a>
    login_element = driver.find_element(By.LINK_TEXT, "Project Management")
    login_element.click()
    time.sleep(5)
    driver.quit()


@allure.title("click on Personal Demo")
@allure.description("verify if Hyperlink works for personal demo")
@pytest.mark.positive
def test_espocrm_PersonalDemo():
    load_dotenv()
    chrome_options = Options()
    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("espo_url"))
    time.sleep(6)
    # <a href="https://www.espocrm.com/cloud-registration/?plan=demo">personal demo</a>
    login_element = driver.find_element(By.LINK_TEXT, "personal demo")
    login_element.click()
    time.sleep(5)
    driver.quit()















