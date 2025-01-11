from selenium.webdriver.common.by import By

class OrderPageLocators:
    consent_button = [By.CSS_SELECTOR, 'div[class^=App_CookieConsent] button']
    for_whom_scooter_link = [By.XPATH, '//*[@id="root"]/div/div[2]/div[1]']
    name_field = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/input']
    last_name_field = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/input']
    address_field = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[3]/input']
    metro_station_field = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[4]/div/div/input']
    metro_station_name = [By.XPATH, '//div[@class="select-search__select"]//div[text()="Лубянка"]']
    metro_station_name_1 = [By.XPATH, '//div[@class="select-search__select"]//div[text()="Сокол"]']
    telephone_number_field = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[5]/input']
    further_button = [By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/button']
    rent_header = [By.CSS_SELECTOR, 'div[class^="Order_Header"]']
    time_to_deliver_field = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/input']
    date = [By.CLASS_NAME, 'react-datepicker__day--025']
    date_1 = [By.CLASS_NAME, 'react-datepicker__day--028']
    days_of_rent = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[1]/div[1]']
    rent_duration = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[3]']
    rent_duration_1 = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[7]']
    scooter_color = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[3]']
    black_colour = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[3]/label[1]']
    grey_colour = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[3]/label[2]']
    comment_field = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[4]/input']
    order_button_on_page_order = [By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/button[2]']
    back_button = [By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/button[1]']
    do_you_want_to_make_an_order_link = [By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/div[1]']
    yes_button = [By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/div[2]/button[2]']
    no_button = [By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/div[2]/button[1]']
    see_status_button = [By.XPATH, '/html/body/div/div/div[2]/div[5]/div[2]/button']
    order_created = [By.CSS_SELECTOR, '.Order_ModalHeader__3FDaJ']







