"""
precondition
    setup, Connection API

Test
Test
Assertion
Postcon
    clean, close, close

"""
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver= None

@pytest.fixture
def setup():
    global driver
    print("Start Browser")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield
    driver.quit()
    print("Close Browser")

def test_1(setup):
    driver.get("https://www.facebook.com")
    print("Test 1 executed")
    

def test_2(setup):
    driver.get("https://www.facebook.com")
    print("Test 2 executed")
    

def test_3(setup):
    driver.get("https://www.facebook.com")
    print("Test 3 executed")
    