from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import TestLocators


                                                 # Тесты раздел Конструктор
class TestChapterConstructor:
    def test_constructor_in_sauces(self, login): # Конструктор переход в Соусы

        driver = login                           # Авторизация

        driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR).click()
        driver.find_element(*TestLocators.BUTTON_SAUCES).click()

        sauce = driver.find_element(*TestLocators.TEXT_SAUCES)
        assert sauce.text == 'Соусы'

    def test_constructor_in_toppings(self, login): # Конструктор переход в Начинки

        driver = login

        driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR).click()
        driver.find_element(*TestLocators.BUTTON_TOPPINGS).click()
        
        toppings = driver.find_element(*TestLocators.TEXT_TOPPINGS)
        assert toppings.text == 'Начинки'

    def test_constructor_in_rolls(self, login): # Конструктор переход в Булки

        driver = login

        driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR).click()
        driver.find_element(*TestLocators.BUTTON_TOPPINGS).click()
        driver.find_element(*TestLocators.BUTTON_ROLLS).click()

        rolls = driver.find_element(*TestLocators.TEXT_ROLLS)
        assert rolls.text == 'Булки'
