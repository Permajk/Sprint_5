from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import TestLocators
from data import TestUrls



class TestTransitionInPersAccount:
    def test_transition_in_pers_account(self, login): # Переход в Личный кабинет из Конструктора
        
        driver = login                                # Авторизация

        driver.find_element(*TestLocators.BUTTON_PERS_ACCOUNT).click()
        WebDriverWait(driver, 7).until(expected_conditions.presence_of_element_located(TestLocators.BUTTON_PROFILE))
        
        driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver, 7).until(expected_conditions.presence_of_element_located(TestLocators.TEXT_PACK_BURGER))
        
        driver.find_element(*TestLocators.BUTTON_PERS_ACCOUNT).click()
        WebDriverWait(driver, 7).until(expected_conditions.presence_of_element_located(TestLocators.BUTTON_PROFILE))

        exit = driver.find_element(*TestLocators.BUTTON_EXIT)
        assert driver.current_url == TestUrls.url_profile and exit.text == 'Выход'
