import allure
import pytest

def method1():
    print("Hello World")

@allure.title("Test-1 Authentication")
@pytest.mark.smoke
def test_method2():
    print("This is first test case")
    assert True==False

@allure.title("Test-2 Authentication")
@pytest.mark.smoke
def test_method3():
    print("test2")
    assert 1+2==3