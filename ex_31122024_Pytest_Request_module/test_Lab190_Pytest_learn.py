import allure
import pytest
import requests

@allure.title("TC 2-verify that 2-2==0")
@allure.description("This verifies the operation")
@pytest.mark.regression
def test_basic_math():
    assert 2-2 == 0


@allure.title("TC 2-verify that 2-2==0")
@allure.description("This verifies the operation")
@pytest.mark.smoke
def test_basic_math1():
    assert 2 + 2 == 4


@pytest.mark.skip(reason="Not working, skip it")
def test_basic_math1():
    assert 2 + 1 == 6




