# import email
# from emaillib import Email, MailAdminClient
import pytest

class MailAdminClient:
    def create_user(self):
        return MailUser()
            
    def delete_user(self, user):
        pass

class MailUser:
    def __init__(self):
        self.inbox = []

    def send_email(self, email, other):
        other.inbox.append(email)

    def clear_mailbox(self):
        self.inbox.clear()

class Email:
    def __init__(self, subject, body):
        self.subject = subject
        self.body = body

@pytest.fixture
def mail_admin():
    return MailAdminClient()

@pytest.fixture
def sending_user(mail_admin):
    user = mail_admin.create_user()
    yield user
    mail_admin.delete_user(user)

@pytest.fixture
def recieving_user(mail_admin):
    user = mail_admin.create_user()
    yield user
    user.clear_mailbox()
    mail_admin.delete_user(user)

def test_email_recieved(sending_user, recieving_user):
    email = Email(subject="Hey!", body="How are you")
    sending_user.send_email(email, recieving_user)
    assert email in recieving_user.inbox