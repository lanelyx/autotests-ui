from typing import Pattern

from playwright.sync_api import Page, expect


class BaseComponent:
    def __init__(self, page: Page):
        self.page = page

    def check_current_url(self, expected_url: Pattern[str]):
        expect(self.page).to_be_visible(expected_url)

    