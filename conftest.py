import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import TestLocators
from data import TestUrls
from data import TestPersonData


@pytest.fixture             # Настройки
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1600,900')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(TestUrls.url_main_paige)
    yield driver
    driver.quit()


@pytest.fixture             # Авторизация
def login(driver):
    driver.get(TestUrls.url_login)
    
    
    driver.find_element(*TestLocators.EMAIL).send_keys(TestPersonData.login)
    driver.find_element(*TestLocators.PASSWORD).send_keys(TestPersonData.password)
    driver.find_element(*TestLocators.BUTTON_LOGIN).click()

    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.BUTTON_PLACE_ORDER))
    
    return driver
