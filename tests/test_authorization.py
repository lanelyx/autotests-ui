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
    login_page.fill_login_form(email=email, password=password)
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()

    #
    # chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    #
    # email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    # email_input.fill(email)
    #
    # password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    # password_input.fill(password)
    #
    # # login_button = page.locator('//button[@data-testid="login-page-login-button"]') # поиск по классическому локатору
    # login_button = chromium_page.get_by_test_id(
    #     'login-page-login-button')  # поиск по data-testid(у Playwright нативная поддержка данного атрибута)
    # login_button.click()
    #
    # wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
    # expect(wrong_email_or_password_alert).to_be_visible()
    # expect(wrong_email_or_password_alert).to_have_text('Wrong email or password')
