from playwright.sync_api import sync_playwright, expect


def test_wrong_email_or_password_authorization():
    with sync_playwright() as playwright:  # контекстный менеджер
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        email_input = page.get_by_test_id('login-form-email-input').locator('input')
        email_input.fill("user.name@gmail.com")

        password_input = page.get_by_test_id('login-form-password-input').locator('input')
        password_input.fill("Password")

        # login_button = page.locator('//button[@data-testid="login-page-login-button"]') # поиск по классическому локатору
        login_button = page.get_by_test_id(
            'login-page-login-button')  # поиск по data-testid(у Playwright нативная поддержка данного атрибута)
        login_button.click()

        wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
        expect(wrong_email_or_password_alert).to_be_visible()
        expect(wrong_email_or_password_alert).to_have_text('Wrong email or password')
