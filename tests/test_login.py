from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import TestLocators
from data import TestUrls, TestPersonData


                                         # Тесты на вход
class TestLogin:
    def test_authorization(self, login): # Авторизация
        
        driver = login

        button_place_order = driver.find_element(*TestLocators.BUTTON_PLACE_ORDER)
        assert driver.current_url == TestUrls.url_main_paige and button_place_order.text == 'Оформить заказ'

    def test_login_in_account(self, driver): # Войти в аккаунт

        driver.find_element(*TestLocators.BUTTON_LOGIN_IN_ACCOUNT).click()
        WebDriverWait(driver, 7).until(expected_conditions.presence_of_element_located(TestLocators.BUTTON_LOGIN))

        driver.find_element(*TestLocators.EMAIL).send_keys(TestPersonData.login)
        driver.find_element(*TestLocators.PASSWORD).send_keys(TestPersonData.password)

        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 7).until(expected_conditions.presence_of_element_located(TestLocators.BUTTON_PLACE_ORDER))

        button_place_order = driver.find_element(*TestLocators.BUTTON_PLACE_ORDER)
        assert driver.current_url == TestUrls.url_main_paige and button_place_order.text == 'Оформить заказ'

    def test_pers_account(self, driver): # Личный Кабинет

        driver.find_element(*TestLocators.BUTTON_PERS_ACCOUNT).click()
        WebDriverWait(driver, 7).until(expected_conditions.presence_of_element_located(TestLocators.BUTTON_LOGIN))

        driver.find_element(*TestLocators.EMAIL).send_keys(TestPersonData.login)
        driver.find_element(*TestLocators.PASSWORD).send_keys(TestPersonData.password)

        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 7).until(expected_conditions.presence_of_element_located(TestLocators.BUTTON_PLACE_ORDER))

        button_place_order = driver.find_element(*TestLocators.BUTTON_PLACE_ORDER)
        assert driver.current_url == TestUrls.url_main_paige and button_place_order.text == 'Оформить заказ'

    def test_login_in_form_registration(self, driver): # Войти в форме Регистрации

        driver.get(TestUrls.url_register)

        driver.find_element(*TestLocators.TEXT_LOGIN).click()
        WebDriverWait(driver, 7).until(expected_conditions.presence_of_element_located(TestLocators.BUTTON_LOGIN))

        driver.find_element(*TestLocators.EMAIL).send_keys(TestPersonData.login)
        driver.find_element(*TestLocators.PASSWORD).send_keys(TestPersonData.password)

        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 7).until(expected_conditions.presence_of_element_located(TestLocators.BUTTON_PLACE_ORDER))

        button_place_order = driver.find_element(*TestLocators.BUTTON_PLACE_ORDER)
        assert driver.current_url == TestUrls.url_main_paige and button_place_order.text == 'Оформить заказ'

    def test_login_in_form_recover_password(self, driver): # Войти в форме Восстановить пароль

        driver.get(TestUrls.url_forgot_password)

        driver.find_element(*TestLocators.TEXT_LOGIN).click()
        WebDriverWait(driver, 7).until(expected_conditions.presence_of_element_located(TestLocators.BUTTON_LOGIN))

        driver.find_element(*TestLocators.EMAIL).send_keys(TestPersonData.login)
        driver.find_element(*TestLocators.PASSWORD).send_keys(TestPersonData.password)

        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 7).until(expected_conditions.presence_of_element_located(TestLocators.BUTTON_PLACE_ORDER))

        button_place_order = driver.find_element(*TestLocators.BUTTON_PLACE_ORDER)
        assert driver.current_url == TestUrls.url_main_paige and button_place_order.text == 'Оформить заказ'
