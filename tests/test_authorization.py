import pytest

from pages.login_page import LoginPage

authorization_data_email_pass = [
    ("user.name@gmail.com", "password"),
    ("user.name@gmail.com", "  "),
    ("  ", "password")
]


def unpackage_auth_data(authorization_data_email_pass):
    return [f"Email : {email!r} , Password : {password!r}" for email, password in authorization_data_email_pass]


@pytest.mark.parametrize(
    'email, password',
    authorization_data_email_pass,
    ids=unpackage_auth_data(authorization_data_email_pass)
)
@pytest.mark.regression
@pytest.mark.authorization
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):
    login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
    login_page.login_form.fill(email=email, password=password)
    login_page.login_form.check_visible(email=email, password=password)
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()
