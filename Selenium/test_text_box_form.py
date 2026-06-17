import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestSuite:

    FULL_NAME_LOCATOR           = (By.ID, "userName")
    EMAIL_LOCATOR               = (By.ID, "userEmail")
    CURRENT_ADDRESS_LOCATOR     = (By.ID, "currentAddress")
    PERMANENT_ADDRESS_LOCATOR   = (By.ID, "permanentAddress")
    SUBMIT_BUTTON_LOCATOR       = (By.ID, "submit")
    RESULT_BOX_LOCATOR          = (By.ID, "output")

    def __init__(self):
        self.url = "https://qa-guru.github.io/one-page-form/text-box.html"
        self.driver = webdriver.Chrome()
        self.result_line_name = {
            "full_name":            "Name:",
            "Email":                "Email:",
            "current_address":      "Current Address :",
            "permanent_address":    "Permananet Address :"
        }

    def set_up(self):
        driver = self.driver
        driver.get(self.url)
        driver.maximize_window()
        time.sleep(1)

    def teardown(self):
        self.driver.quit()

    def enter_full_name(self, full_name: str):
        field = self.driver.find_element(*self.FULL_NAME_LOCATOR)
        field.send_keys(full_name)

    def enter_email(self, email: str):
        field = self.driver.find_element(*self.EMAIL_LOCATOR)
        field.send_keys(email)

    def enter_current_address(self, address: str):
        field = self.driver.find_element(*self.CURRENT_ADDRESS_LOCATOR)
        field.send_keys(address)

    def enter_permanent_address(self, address: str):
        field = self.driver.find_element(*self.PERMANENT_ADDRESS_LOCATOR)
        field.send_keys(address)

    def click_submit(self):
        submit_button = self.driver.find_element(*self.SUBMIT_BUTTON_LOCATOR)
        submit_button.click()
        time.sleep(2)

    def search_result_box(self):
        result_box = self.driver.find_element(*self.RESULT_BOX_LOCATOR)
        assert result_box.text, "Блок пуст, форма не отправилась?"
        return result_box

    def get_string(self, result_box, line_name):
        buffer = result_box.text.split("\n")
        current_line = None  # для проверки
        for line in buffer:
            if line.startswith(self.result_line_name[line_name]):
                current_line = line
                break

        assert current_line is not None, f"В блоке нет строки с {line_name}"
        current_value = current_line.split(":", 1)[1].strip()
        # print(current_value + "\n")
        return current_value

def check_for_empty_input():
    test_variable = None
    try:
        test_variable = TestSuite()
        test_variable.set_up()
        test_variable.enter_full_name("")
        test_variable.enter_email("")
        test_variable.enter_current_address("")
        test_variable.enter_permanent_address("")
        test_variable.click_submit()
        result_box = test_variable.search_result_box()
        current_line = test_variable.get_string(result_box,"full_name")
        assert current_line == "", f"В full_name ожидалась пустая строка, но получено: '{current_line}'"
        current_line = test_variable.get_string(result_box, "Email")
        assert current_line == "", f"В Email ожидалась пустая строка, но получено: '{current_line}'"
        current_line = test_variable.get_string(result_box, "current_address")
        assert current_line == "", f"В current_address ожидалась пустая строка, но получено: '{current_line}'"
        current_line = test_variable.get_string(result_box, "permanent_address")
        assert current_line == "", f"В permanent_address ожидалась пустая строка, но получено: '{current_line}'"
        print("Тест успешно пройден!")

    except AssertionError as error:
        print(f"Тест не пройден!: {error}")
        raise

    finally:
        if test_variable:
            test_variable.teardown()

def fill_in_all_fields():
    test_variable = None
    try:
        test_variable = TestSuite()
        test_variable.set_up()
        test_variable.enter_full_name("Jack Vorobei")
        test_variable.enter_email("Vorobei@mail.ru")
        test_variable.enter_current_address("California")
        test_variable.enter_permanent_address("USA")
        test_variable.click_submit()
        result_box = test_variable.search_result_box()
        current_line = test_variable.get_string(result_box,"full_name")
        assert current_line == "Jack Vorobei", f"В full_name ожидалось - 'Jack Vorobei', но получено: '{current_line}'"
        current_line = test_variable.get_string(result_box, "Email")
        assert current_line == "Vorobei@mail.ru", f"В Email ожидалось - 'Vorobei@mail.ru', но получено: '{current_line}'"
        current_line = test_variable.get_string(result_box, "current_address")
        assert current_line == "California", f"В current_address ожидалось - 'California', но получено: '{current_line}'"
        current_line = test_variable.get_string(result_box, "permanent_address")
        assert current_line == "USA", f"В permanent_address ожидалось - 'USA', но получено: '{current_line}'"
        print("Тест успешно пройден!")

    except AssertionError as error:
        print(f"Тест не пройден!: {error}")
        raise

    finally:
        if test_variable:
            test_variable.teardown()

# fill_in_all_fields()
check_for_empty_input()
