import allure

from curl import main_page_url
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    @allure.step('Дождаться загрузку главной страницы')
    def wait_for_main_page(self):
        self.driver.get(main_page_url)

    @allure.step('Дождаться загрузку вопросов')
    def wait_for_questions_list(self):
        self.wait_for_element(MainPageLocators.question_link)

    @allure.step('Открыть вопрос')
    def click_on_question(self, question_number, timeout=10):
        question_locator = MainPageLocators.question_number(question_number)
        self.scroll_to_element(question_locator)
        self.click_on_element(question_locator, timeout)

    @allure.step('Дождаться, пока откроется нужный ответ')
    def wait_for_answer_visible(self, answer_number):
        self.wait_for_element(MainPageLocators.answer_number(answer_number))

    @allure.step('Сравнить ответ вопроса')
    def check_answer_name(self, expected_text, answer_number):
        actual_text = self.get_text_on_element(MainPageLocators.answer_number(answer_number))
        return actual_text == expected_text

