from typing import Any, Generator

import pytest
from playwright.sync_api import Page, Playwright

from pages.authentication.registration_page import RegistrationPage
from _pytest.fixtures import SubRequest

from tools.playwright.pages import initialize_playwright_page
from config import settings


@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright, test_name=request.node.name)
    #
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context(record_video_dir='./videos')
    # context.tracing.start(screenshots=True, snapshots=True, sources=True)
    # page = context.new_page()
    #
    # yield page
    #
    # context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    # browser.close()
    #
    # allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')
    # allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)


@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page)
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.registration_form.fill(
        email=settings.test_user.email,
        username=settings.test_user.username,
        password=settings.test_user.password,
    )
    registration_page.click_registration_button()
    context.storage_state(path=settings.browser_state_file)
    browser.close()


@pytest.fixture
def chromium_page_with_state(request: SubRequest, playwright: Playwright, initialize_browser_state) -> Page:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        storage_state=settings.browser_state_file)
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context(storage_state='browser_state.json', record_video_dir='./videos')
    # context.tracing.start(screenshots=True, snapshots=True, sources=True)
    # page = context.new_page()
    #
    # yield page
    #
    # context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    # browser.close()
    #
    # allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')
    # allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)
