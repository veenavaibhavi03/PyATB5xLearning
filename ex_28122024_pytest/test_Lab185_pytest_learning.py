import pytest

def method1():
    print("Hello World")

@pytest.mark.smoke
def test_method2():
    print("This is first test case")
    assert True==False

@pytest.mark.smoke
def test_method3():
    print("test2")
    assert 1+2==3