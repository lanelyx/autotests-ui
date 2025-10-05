from playwright.sync_api import sync_playwright

from tools.routes import AppRoute

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(
        AppRoute.LOGIN,
        wait_until='networkidle'  # поможет подождать пока все запросы к серверу для рендера страницы прогрузятся
    )

    registration_link = page.get_by_test_id('login-page-registration-link')
    registration_link.hover()

    page.wait_for_timeout(5000)