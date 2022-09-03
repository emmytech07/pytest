import pytest
import sys

@pytest.mark.smoke
def test_login():
    print("Login done") 

@pytest.mark.regression
def test_product():
    print("Add product to the market")

@pytest.mark.smoke
def test_logut():
    print("Logging out of the system")

@pytest.mark.skip
def test_skipped():
    print("skipping this test function")

@pytest.mark.skipif(sys.version_info < (3,11), reason="Python version not supported")
def test_skippedif():
    print("Version is too slow for the process ")

@pytest.mark.xfail
def test_xfail():
    assert True
    print("skipping this test function")