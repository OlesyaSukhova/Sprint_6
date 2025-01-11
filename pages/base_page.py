import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver
from curl import main_page_url


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Дождаться загрузку главной страницы')
    def wait_for_main_page(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.url_to_be(main_page_url))

    @allure.step('Подождать видимость элемента')
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Подождать кликабельность элемента')
    def wait_for_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator, timeout=10):
        element = self.wait_for_element_clickable(locator, timeout)
        element.click()

    @allure.step('Ввести текст в поле ввода')
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step('Получить текст элемента')
    def get_text_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step('Подождать и проверить, что атрибут элемента содержит текст')
    def wait_for_attribute(self, locator, attribute,  value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element_attribute(locator, attribute, value))