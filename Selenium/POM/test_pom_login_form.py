from selenium import webdriver
from pom_login_form import LoginForm

# Позитивные проверки
def normal_input():
    test_1 = None
    driver = webdriver.Chrome()
    login = "user1"
    password = "password1"
    welcome_message = f"Welcome, {login}!"

    try:
        test_1 = LoginForm(driver)
        test_1.set_up()\
            .fill_form(login, password) \
            .click_submit()
        error = test_1.get_error_message()
        assert not error.text, f"{error.text}"
        message = test_1.check_auth().text
        assert welcome_message in message, f"Сообщение '{message}' отличается от ожидаемого!"
        print("Тест успешно пройден!")

    except AssertionError as error:
        print(f"Тест не пройден!\n{error}")
        raise

    finally:
        if test_1:
            test_1.teardown()

# normal_input()

def input_after_error():
    test_2 = None
    driver = webdriver.Chrome()
    login1 = "incorrect_login"
    password1 = "incorrect_password"
    login2 = "user1"
    password2 = "password1"
    welcome_message = f"Welcome, {login2}!"

    try:
        test_2 = LoginForm(driver)
        test_2.set_up()\
            .fill_form(login1, password1) \
            .click_submit() \
            .clear_form(login=True, password=True) \
            .fill_form(login2, password2) \
            .click_submit()
        error = test_2.get_error_message()
        assert not error.text, f"{error.text}"
        message = test_2.check_auth().text
        assert welcome_message in message, f"Сообщение '{message}' отличается от ожидаемого!"
        print("Тест успешно пройден!")

    except AssertionError as error:
        print(f"Тест не пройден!\n{error}")
        raise

    finally:
        if test_2:
            test_2.teardown()

# input_after_error()

# Негативные проверки
def input_incorrect_login():
    test_3 = None
    driver = webdriver.Chrome()
    login = "u"
    password = "password1"

    try:
        test_3 = LoginForm(driver)
        test_3.set_up() \
            .fill_form(login, password) \
            .click_submit()
        error = test_3.get_error_message()
        assert error.text, "Ошибка не отработала, возможно была успешная авторизация"
        print(f"Тест успешно пройден!,\nТекст ошибки: '{error.text}'")

    except AssertionError as error:
        print(f"Тест не пройден!\n{error}")
        raise

    finally:
        if test_3:
            test_3.teardown()

input_incorrect_login()
