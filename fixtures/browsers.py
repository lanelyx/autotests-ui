import pytest
from playwright.sync_api import Page, Playwright

from pages.authentication.registration_page import RegistrationPage
from playwright_step_12_ import registration_button


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()


@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page)
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.registration_form.fill(email='user.name@gmail.com', username='username', password='password')
    registration_page.click_registration_button()
    context.storage_state(path='browser_state.json')
    browser.close()

@pytest.fixture
def chromium_page_with_state(playwright: Playwright, initialize_browser_state) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser_state.json')
    page = context.new_page()
    yield page
    browser.close()