from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import TestLocators
from data import TestUrls


                                # Тесты переход из личного кабинета в конструктор и на логотоп СтелларБургер
class TestTransitionInConstructor:
    def test_profile(self, login): # Вход в профиль

        driver = login             # Авторизация

        driver.find_element(*TestLocators.BUTTON_PERS_ACCOUNT).click()
        WebDriverWait(driver, 7).until(expected_conditions.presence_of_element_located(TestLocators.BUTTON_PROFILE))
        
        button_profile = driver.find_element(*TestLocators.BUTTON_PROFILE)
        assert driver.current_url == TestUrls.url_profile   and button_profile.text == 'Профиль'

    def test_transition_in_constructor(self, login): # Переход из ЛК в Конструктор

        driver = login

        driver.find_element(*TestLocators.BUTTON_PERS_ACCOUNT).click()

        WebDriverWait(driver, 7).until(expected_conditions.presence_of_element_located(TestLocators.BUTTON_PROFILE))
        driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR).click()

        place_order = driver.find_element(*TestLocators.BUTTON_PLACE_ORDER)
        assert driver.current_url == TestUrls.url_main_paige and place_order.text == 'Оформить заказ'

    def test_transition_in_logotip(self, login): # Переход из ЛК на логотоп СтелларБургер 

        driver = login

        driver.find_element(*TestLocators.BUTTON_PERS_ACCOUNT).click()

        WebDriverWait(driver, 7).until(expected_conditions.presence_of_element_located(TestLocators.BUTTON_PROFILE))
        driver.find_element(*TestLocators.LOGOTIP).click()

        pack_burger = driver.find_element(*TestLocators.TEXT_PACK_BURGER)
        assert driver.current_url == TestUrls.url_main_paige and pack_burger.text == 'Соберите бургер'
