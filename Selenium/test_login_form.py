import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestSuite:
    LOGIN               = (By.ID, "login-input")
    PASSWORD            = (By.ID, "password-input")
    SUBMIT_BUTTON       = (By.ID, "submit-button")
    ERROR_MESSAGE       = (By.CSS_SELECTOR, "#error-message")
    LOGOUT_BUTTON       = (By.ID, "logout-button")
    WELCOME_MESSAGE     = (By.ID, "welcome-message")

    def __init__(self):
        self.url = "https://qa-guru.github.io/one-page-form/login.html"
        self.driver = webdriver.Chrome()

    def set_up(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get(self.url)
        driver.maximize_window()
        return self

    def teardown(self):
        self.driver.quit()

    def fill_form(self, login=None, password=None):
        if login is not None:
            self.driver.find_element(*self.LOGIN).send_keys(login)
        if password is not None:
            self.driver.find_element(*self.PASSWORD).send_keys(password)
        return self

    def clear_form(self, login=False, password=False):
        if login:
            field = self.driver.find_element(*self.LOGIN)
            field.click()
            field.send_keys(Keys.COMMAND + "a")
            field.send_keys(Keys.DELETE)
        if password:
            field = self.driver.find_element(*self.PASSWORD)
            field.click()
            field.send_keys(Keys.COMMAND + "a")
            field.send_keys(Keys.DELETE)
        return self

    def click_submit(self):
        self.driver.find_element(*self.SUBMIT_BUTTON) \
            .click()
        return self

    def click_logout(self):
        self.driver.find_element(*self.LOGOUT_BUTTON).click()
        return self

    def get_error_message(self):
        error = self.driver.find_element(*self.ERROR_MESSAGE)
        return error.text

    def check_auth(self):
        message = self.driver.find_element(*self.WELCOME_MESSAGE)
        return message

def re_enter():
    test          = None
    login_1       = "qw"
    password_1    = "qwq"
    login_2       = "user1"
    password_2    = "password1"

    try:
        test = TestSuite()
        test.set_up() \
            .fill_form(login_1, password_1) \
            .click_submit() \
            .clear_form(True, True) \
            .fill_form(login_2, password_2)\
            .click_submit()
        error = test.get_error_message()
        assert not error, f"{error}"
        auth = test.check_auth()
        assert auth.text, "Авторизация не пройдена!"
        print("Тест успешно пройден!")

    except AssertionError as error:
        print(f"Тест не пройден!: {error}")
        raise

    finally:
        if test:
            test.teardown()

re_enter()