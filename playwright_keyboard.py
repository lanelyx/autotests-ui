from playwright.sync_api import sync_playwright

from tools.routes import AppRoute

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(AppRoute.LOGIN)

    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.focus()

    for char in 'user@gmail.com': # тут ввод побуквенно как пользак
        page.keyboard.type(char, delay=300)

    page.keyboard.press('ControlOrMeta+A') # выделяем весь текст

    page.wait_for_timeout(5000)