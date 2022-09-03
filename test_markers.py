from re import L
import pytest

@pytest.mark.smoke
def test_login():
    print("Login done") 

@pytest.mark.regression
def test_product():
    print("Add product to the market")

@pytest.mark.smoke
def test_logut():
    print("Logging out of the system")