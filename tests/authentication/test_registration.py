import pytest
import allure
from allure_commons.types import Severity

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
class TestRegistration:
    @allure.title('Registration with correct email, username and password')
    @allure.severity(Severity.CRITICAL)
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
