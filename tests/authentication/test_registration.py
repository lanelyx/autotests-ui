import pytest

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
class TestRegistration:
    def test_successful_registration(self,
            registration_page: RegistrationPage,
            dashboard_page: DashboardPage):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill(email="username@gmail.com", username="username", password="password")
        registration_page.registration_form.check_visible(
            email="username@gmail.com",
            username="username",
            password="password"
        )
        registration_page.click_registration_button()
        dashboard_page.toolbar_view.check_visible()
