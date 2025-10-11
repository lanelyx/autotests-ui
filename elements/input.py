import allure
from ui_coverage_tool import ActionType

from elements.base_element import BaseElement
from playwright.sync_api import expect, Locator

from tools.logger import get_logger

logger = get_logger("INPUT")


class Input(BaseElement):
    @property
    def type_of(self):
        return 'input'

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        return super().get_locator(nth, **kwargs).locator('input')

    def get_raw_locator(self, nth: int = 0, **kwargs) -> str:
        return f'{super().get_raw_locator(nth, **kwargs)}//input'

    def fill(self, value: str, nth: int = 0, **kwargs):
        step = f'Filling {self.type_of} "{self.name}" with "{value}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.fill(value)

        self.track_coverage(action_type=ActionType.FILL, nth=nth, **kwargs)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" has a value "{value}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_value(value)

        self.track_coverage(action_type=ActionType.VALUE, nth=nth, **kwargs)
