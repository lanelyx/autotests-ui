from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.input import Input
from elements.textarea import Textarea


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title_input = Input(page, 'create-course-form-title-input', 'Title input')
        self.estimated_time_input = Input(
            page, 'create-course-form-estimated-time-input', 'Estimated time input')
        self.description_textarea = Textarea(
            page, 'create-course-form-description-input', 'Description input')

        self.max_score_input = Input(page, 'create-course-form-max-score-input', 'Max score input')
        self.min_score_input = Input(page, 'create-course-form-min-score-input', 'Min score input')

    def fill(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.title_input.fill(title)
        self.estimated_time_input.fill(estimated_time)
        self.description_textarea.fill(description)
        self.max_score_input.fill(max_score)
        self.min_score_input.fill(min_score)

    def check_visible(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.title_input.check_visible()
        self.title_input.check_have_text(title)

        self.estimated_time_input.check_visible()
        self.estimated_time_input.check_have_value(estimated_time)

        self.description_textarea.check_visible()
        self.description_textarea.check_have_text(description)

        self.max_score_input.check_visible()
        self.max_score_input.check_have_text(max_score)

        self.min_score_input.check_visible()
        self.min_score_input.check_have_text(min_score)
