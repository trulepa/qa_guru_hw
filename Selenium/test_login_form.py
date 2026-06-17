import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestSuite:
    LOGIN_LOCATOR           = (By.ID, "login-input")
    PASSWORD_LOCATOR        = (By.ID, "password-input")
    SUBMIT_BUTTON_LOCATOR   = (By.ID, "submit-button")
    ERROR_MESSAGE_LOCATOR   = (By.CSS_SELECTOR, "#error-message")

    def __init__(self):
        self.url = "https://qa-guru.github.io/one-page-form/login.html"
        self.driver = webdriver.Chrome()

    def set_up(self):
        driver = self.driver
        driver.get(self.url)
        driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def enter_login(self, login: str):
        field = self.driver.find_element(*self.LOGIN_LOCATOR)
        field.send_keys(login)

    def enter_password(self, password: str):
        field = self.driver.find_element(*self.PASSWORD_LOCATOR)
        field.send_keys(password)

    def click_submit(self):
        submit_button = self.driver.find_element(*self.SUBMIT_BUTTON_LOCATOR)
        submit_button.click()
        # time.sleep(2)

    def check_error_message(self):
        error = self.driver.find_element(*self.ERROR_MESSAGE_LOCATOR)
        return error.text

    def clear_login(self):
        field = self.driver.find_element(*self.LOGIN_LOCATOR)
        field.click()  # Фокусируемся на поле
        field.send_keys(Keys.COMMAND + "a")
        field.send_keys(Keys.DELETE)

    def clear_password(self):
        field = self.driver.find_element(*self.PASSWORD_LOCATOR)
        field.click()  # Фокусируемся на поле
        field.send_keys(Keys.COMMAND + "a")
        field.send_keys(Keys.DELETE)


def re_enter():
    test          = None
    login_1       = "qw"
    password_1    = "qwq"
    login_2       = "qaguru@qa.guru"
    password_2    = "qaguru"

    try:
        test = TestSuite()
        test.set_up()
        test.enter_login(login_1)
        test.enter_password(password_1)
        test.click_submit()
        test.clear_login()
        test.enter_login(login_2)
        test.clear_password()
        test.enter_password(password_2)
        test.click_submit()
        error = test.check_error_message()
        assert "Login" not in error, "Проверь логин (и пароль)" # "Login must be at least 3 characters" / "Login and password are required (minimum 3 and 6 characters)"
        assert "Password" not in error, "Проверь пароль" # "Password must be at least 6 characters"
        assert "Wrong" not in error, "Проверь логин и пароль" # "Wrong login or password"
        print("Тест успешно пройден!")

    except AssertionError as error:
        print(f"Тест не пройден!: {error}")
        raise

    finally:
        if test:
            test.teardown()


re_enter()