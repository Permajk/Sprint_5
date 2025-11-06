from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import TestLocators
from data import TestUrls


class TestExit:
    def test_exit_in_account(self, login): # Выход из аккаунта
        
        driver = login # Авторизация

        driver.find_element(*TestLocators.BUTTON_PERS_ACCOUNT).click()
        WebDriverWait(driver, 7).until(expected_conditions.presence_of_element_located(TestLocators.BUTTON_EXIT))

        driver.find_element(*TestLocators.BUTTON_EXIT).click()
        WebDriverWait(driver, 7).until(expected_conditions.presence_of_element_located(TestLocators.BUTTON_LOGIN))

        button_login = driver.find_element(*TestLocators.BUTTON_LOGIN)
        assert driver.current_url == TestUrls.url_login and button_login.text == 'Войти'
