from selenium.webdriver.common.by import By

class MainPageLocators:
    order_button_on_top = [By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/button[1]']
    order_button_from_below = [By.XPATH, '//*[@id="root"]/div/div/div[4]/div[2]/div[5]/button']
    question_link = [By.XPATH, '//*[@id="root"]/div/div/div[5]/div[1]']
    scooter_button = [By.XPATH, '//*[@id="root"]/div/div/div[1]/div[1]/a[2]']
    yandex_button = [By.XPATH, '//*[@id="root"]/div/div/div[1]/div[1]/a[1]']

    @staticmethod
    def question_number(question):
        return By.CSS_SELECTOR, f'.accordion .accordion__item:nth-child({question}) .accordion__heading'

    @staticmethod
    def answer_number(answer):
        return By.CSS_SELECTOR, f'.accordion .accordion__item:nth-child({answer}) .accordion__panel'


