import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from curl import order_page_url, main_page_url
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators

class TestButtonsOneTheMainPage:
    @allure.title('Нажатие на кнопку Заказать вверху страницы ведет на поле оформления заказа')
    def test_successful_tab_on_the_order_button_on_the_top(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        main_page.click_on_element(MainPageLocators.order_button_on_top)
        assert driver.current_url == order_page_url

    @allure.title('Нажатие на кнопку Заказать внизу страницы ведет на поле оформления заказа')
    def test_successful_tab_on_the_order_button_from_below(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        main_page.scroll_to_element(MainPageLocators.order_button_from_below)
        main_page.click_on_element(MainPageLocators.order_button_from_below, 5000)
        assert driver.current_url == order_page_url

    @allure.title('Нажатие на логотип Самоката ведет на главную страницу Самоката')
    def test_successful_tab_on_the_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        main_page.click_on_element(MainPageLocators.scooter_button)
        assert driver.current_url == main_page_url

    @allure.title('Нажатие на логотип Яндекса ведет на страницу Дзена через редирект')
    def test_successful_tab_on_the_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        main_page.click_on_element(MainPageLocators.yandex_button)
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        new_window = driver.window_handles[1]
        driver.switch_to.window(new_window)
        WebDriverWait(driver, 1000).until(EC.url_contains('dzen'))
        assert 'dzen.ru' in driver.current_url











