import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'create-course-exercises-box-toolbar-title-text', 'Title')
        self.create_button = Button(
            page, 'create-course-exercises-box-toolbar-create-exercise-button', 'Create button')

    @allure.step('Check visible create course exercises toolbar view')
    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Exercises')

        self.create_button.check_visible()

    def click_create_exercise_button(self):
        self.create_button.click()
