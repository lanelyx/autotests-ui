from playwright.sync_api import Page
import pytest

from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

user_info_data = {
    "email": "username@gmail.com",
    "username": "username",
    "password": "password",
}
email = user_info_data['email']
username = user_info_data['username']
password = user_info_data['password']


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(
        chromium_page: Page,
        registration_page: RegistrationPage,
        dashboard_page: DashboardPage):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.fill_registration_form(email=email, username=username, password=password)
    registration_page.click_registration_button()
    dashboard_page.check_visible_dashboard_title()
