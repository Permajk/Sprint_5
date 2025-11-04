from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import TestLocators
from data import TestUrls, TestRandomUser, TestRandomIncorrectPassword


                                                    # Тесты на Регистрацию
class TestRegistration:
    def test_successful_registration(self, driver): # Успешная Регистрация

        driver.get(TestUrls.url_register)

        driver.find_element(*TestLocators.NAME).send_keys(TestRandomUser.user_name)
        driver.find_element(*TestLocators.EMAIL).send_keys(TestRandomUser.login)
        driver.find_element(*TestLocators.PASSWORD).send_keys(TestRandomUser.password)

        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        WebDriverWait(driver, 7).until(expected_conditions.presence_of_element_located(TestLocators.BUTTON_LOGIN))

        button_login = driver.find_element(*TestLocators.BUTTON_LOGIN)
        assert driver.current_url == TestUrls.url_login and button_login.text == 'Войти'

    def test_incorrect_password(self, driver,):     # Некорректный пароль

        driver.get(TestUrls.url_register)

        driver.find_element(*TestLocators.NAME).send_keys(TestRandomIncorrectPassword.user_name)
        driver.find_element(*TestLocators.EMAIL).send_keys(TestRandomIncorrectPassword.login)
        driver.find_element(*TestLocators.PASSWORD).send_keys(TestRandomIncorrectPassword.password)

        driver.find_element(*TestLocators.BUTTON_REGISTER).click()
        WebDriverWait(driver, 7).until(expected_conditions.presence_of_element_located(TestLocators.INCORRECT_PASSWORD))
        incorrect_password = driver.find_element(*TestLocators.INCORRECT_PASSWORD)

        assert incorrect_password.text == 'Некорректный пароль'
