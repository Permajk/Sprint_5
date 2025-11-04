from selenium.webdriver.common.by import By


class TestLocators:
    # Локаторы Личный кабинет, Вход
    BUTTON_PERS_ACCOUNT = By.XPATH, "//p[text()='Личный Кабинет']" # Кнопка Личный кабинет
    EMAIL = By.XPATH, "//label[text()='Email']/following-sibling::input" # Емейл
    PASSWORD = By.XPATH, "//input[@name='Пароль']" # Пароль
    BUTTON_LOGIN = By.XPATH, "//button[text()='Войти']" # Кнопка Войти
    BUTTON_EXIT = By.XPATH, "//button[@type = 'button']" # Кнопка Выйти

    # Локаторы Регистрация
    TEXT_REGISTER = By.XPATH, "//a[text()='Зарегистрироваться']" # Текст Зарегистрироваться
    NAME = By.XPATH, "//label[text()='Имя']/following-sibling::input" # Имя
    EMAIL = By.XPATH, "//label[text()='Email']/following-sibling::input" # Емейл
    PASSWORD = By.XPATH, "//input[@name='Пароль']" # Пароль
    BUTTON_REGISTER = By.XPATH, "//button[text()='Зарегистрироваться']" # Кнопка Зарегистрироваться
    INCORRECT_PASSWORD = By.XPATH, "//p[text() = 'Некорректный пароль']" # Некорректный пароль
    
    # Локаторы Войти в форме Регистрации
    TEXT_LOGIN = By.XPATH, "//a[text()='Войти']" # Текст Войти
    EMAIL = By.XPATH, "//label[text()='Email']/following-sibling::input" # Емейл
    PASSWORD = By.XPATH, "//input[@name='Пароль']" # Пароль
    BUTTON_LOGIN = By.XPATH, "//button[text()='Войти']" # Кнопка Войти
    
    # Локаторы Восстановить пароль в форме Входа
    TEXT_RECOVER_PASSWORD = By.XPATH, "//a[text()='Восстановить пароль']" # Текст Восстановить пароль
    EMAIL = By.XPATH, "//label[text()='Email']/following-sibling::input" # Емейл
    BUTTON_RESTORE = By.XPATH, "//button[text()='Восстановить']" # Кнопка Восстановить
    
    # Локароры Восстановление пароля в форме Восстановить
    NEW_PASSWORD = By.XPATH, "//input[@name='Введите новый пароль']" # Новый Пароль
    ENTER_THE_CODE = By.XPATH, "//label[text()='Введите код из письма']/following-sibling::input" # Введите код из письма
    BUTTON_SAVE = By.XPATH, "//button[text()='Сохранить']" # Кнопка Сохранить

    # Локаторы Войти в аккаунт, Вход
    BUTTON_LOGIN_IN_ACCOUNT = By.XPATH, "//button[text()='Войти в аккаунт']" # Кнопка Войти в аккаунт
    EMAIL = By.XPATH, "//label[text()='Email']/following-sibling::input" # Емейл
    PASSWORD = By.XPATH, "//input[@name='Пароль']" # Пароль
    BUTTON_LOGIN = By.XPATH, "//button[text()='Войти']" # Кнопка Войти
    
    # Локаторы Конструктор
    BUTTON_CONSTRUCTOR = By.XPATH, "//p[text()='Конструктор']" # Кнопка Конструктор
    ACTIVE_CONSTRUCTOR = By.XPATH, "//div[@class ='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']" # Активный раздел Конструктора
    BUTTON_ROLLS = By.XPATH, "//span[text()='Булки']" # Кнопка Булки
    TEXT_ROLLS = By.XPATH, "//h2[text()='Булки']" # Текст Булки
    BUTTON_SAUCES = By.XPATH, "//span[text()='Соусы']" # Кнопка Соусы
    TEXT_SAUCES = By.XPATH, "//h2[text()='Соусы']" # Текст Соусы
    BUTTON_TOPPINGS = By.XPATH, "//span[text()='Начинки']" # Кнопка Начинки
    TEXT_TOPPINGS = By.XPATH, "//h2[text()='Начинки']" # Текст Начинки

    BUTTON_PLACE_ORDER = By.XPATH, "//button[text()='Оформить заказ']" # Кнопка Оформить заказ
    LOGOTIP = By.CSS_SELECTOR, "svg[fill='none']" # Логотип Стеллар Бургер
    BUTTON_PROFILE = By.XPATH, "//a[text()='Профиль']"# Кнопка Профиль в Личном кабинете
    TEXT_PACK_BURGER = By.XPATH, "//h1[text()='Соберите бургер']" # Текст Собери Бургер
    
