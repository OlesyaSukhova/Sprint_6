import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import credentials_1, credentials_2
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage


class TestMakeAnOrder:
    @allure.title('Оформление заказа')
    @pytest.mark.parametrize('credentials', [credentials_1, credentials_2])
    def test_successful_order(self, driver, credentials):
        order_page = OrderPage(driver)
        order_page.wait_for_order_page()
        order_page.test_successful_completion_of_the_order_form(
            credentials['name'],
            credentials['last_name'],
            credentials['address'],
            credentials['phone_number'],
            credentials['comment']
        )
        WebDriverWait(driver, 100).until(EC.text_to_be_present_in_element(OrderPageLocators.order_created, 'Заказ оформлен'))
        assert driver.find_element(*OrderPageLocators.see_status_button).is_displayed()









