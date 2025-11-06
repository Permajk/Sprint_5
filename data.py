import random



class TestPersonData:
    user_name = 'Alex'
    login = 'Aleksey_Rogozhnikov_32@yandex.ru'
    password = '000000'


class TestUrls:
    # Основная страница
    url_main_paige = "https://stellarburgers.education-services.ru/"

    # Ссылка на страницу входа
    url_login = "https://stellarburgers.education-services.ru/login"

    # Ссылка страницы  Профиля
    url_profile = "https://stellarburgers.education-services.ru/account/profile"

    # Ссылка на страницу регистрации
    url_register = "https://stellarburgers.education-services.ru/register"

    # Ссылка на страницу забыл пароль
    url_forgot_password = "https://stellarburgers.education-services.ru/forgot-password"


class TestRandomUser:
    user_name = 'Alex'
    login = f'Alex_Rogozhnikov_32_{random.randint(100, 999)}@yandex.ru'
    password = f'{random.randint(100000, 999999)}'
    

class TestRandomIncorrectPassword:
    user_name = 'Alex'
    login = 'Aleksey_Rogozhnikov_32@yandex.ru'
    password = f'{random.randint(10000, 99999)}'   