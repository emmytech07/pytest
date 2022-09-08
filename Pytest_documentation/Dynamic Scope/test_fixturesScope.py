import smtplib
from urllib import response

import pytest

@pytest.fixture(scope="module")
def smtp_connection():
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)

def test_echo (smtp_connection):
    response, msg = smtp_connection.echo()
    assert response ==250
    assert b"smtp.gmail.com" in msg
    assert 0

def test_noop (smtp_connection):
    response, msg = smtp_connection.noop()
    assert response ==250
    assert b"smtp.gmail.com" in msg
    assert 0