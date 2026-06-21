import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

class TestSuite:
    FIRST_NAME          = (By.ID, "firstName")
    LAST_NAME           = (By.ID, "lastName")
    EMAIL               = (By.ID, "userEmail")
    GENDER_MALE         = (By.ID, "gender-radio-1")
    GENDER_FEMALE       = (By.ID, "gender-radio-2")
    GENDER_OTHER        = (By.ID, "gender-radio-3")
    MOBILE_NUMBER       = (By.ID, "userNumber")
    DATE_OF_BIRTH       = (By.ID, "dateOfBirthInput")
    SUBJECTS            = (By.ID, "subjectsInput")
    HOBBIES_SPORTS      = (By.ID, "hobbies-checkbox-1")
    HOBBIES_READING     = (By.ID, "hobbies-checkbox-2")
    HOBBIES_MUSIC       = (By.ID, "hobbies-checkbox-3")
    PICTURE             = (By.ID, "uploadPicture")
    CURRENT_ADDRESS     = (By.ID, "currentAddress")
    STATE               = (By.ID, "state")
    CITY                = (By.ID, "city")
    SUBMIT_BUTTON       = (By.ID, "submit")
    RESULT_TABLE        = (By.ID, "resultBody")
    CLOSE_RESULT_TABLE  = (By.ID, "closeModal")
    ERROR               = (By.ID, "formError")

    def __init__(self):
        self.url = "https://qa-guru.github.io/one-page-form/automation-practice-form.html"
        self.driver = webdriver.Chrome()
        self.fluent_wait = WebDriverWait(
            self.driver,
            timeout=10,
            poll_frequency=0.5,
            ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]
        )

    def set_up(self):
        driver = self.driver
        driver.get(self.url)
        driver.maximize_window()
        driver.implicitly_wait(5)
        time.sleep(1)

    def teardown(self):
        self.driver.quit()

    def enter_first_name(self, value: str):
        field = self.driver.find_element(*self.FIRST_NAME)
        field.send_keys(value)

    def enter_last_name(self, value: str):
        field = self.driver.find_element(*self.LAST_NAME)
        field.send_keys(value)

    def enter_email(self, value: str):
        field = self.driver.find_element(*self.EMAIL)
        field.send_keys(value)

    def select_gender(self, gender=None):
        if gender == "Male":
            self.driver.find_element(*self.GENDER_MALE).click()
        if gender == "Female":
            self.driver.find_element(*self.GENDER_FEMALE).click()
        if gender == "Other":
            self.driver.find_element(*self.GENDER_OTHER).click()

    def enter_mobile_number(self, value):
        field = self.driver.find_element(*self.MOBILE_NUMBER)
        field.send_keys(value)

    def select_date_of_birth(self, day: str, month: str, year: str):
        field = self.driver.find_element(*self.DATE_OF_BIRTH)
        field.click()

        select_month = Select(self.driver.find_element(By.CSS_SELECTOR, "select.react-datepicker__month-select"))
        select_month.select_by_value(month)
        select_year = Select(self.driver.find_element(By.CSS_SELECTOR, "select.react-datepicker__year-select"))
        select_year.select_by_value(year)

        span = f"span[data-day='{day}']"
        select_day = self.driver.find_element(By.CSS_SELECTOR, span)
        select_day.click()

    def select_subjects(self, value):
        subjects = self.driver.find_element(*self.SUBJECTS)
        email = self.driver.find_element(*self.EMAIL)

        for element in value:
            email.click()
            subjects.click()
            xpath = f"//div[@class='subjects-auto-complete__option' and text()='{element}']"
            self.fluent_wait.until(ec.visibility_of_element_located((By.XPATH, xpath))).click()

    def select_hobbies(self, hobbies):
        for element in hobbies:
            if element == "Sports":
                self.driver.find_element(*self.HOBBIES_SPORTS).click()
            if element == "Reading":
                self.driver.find_element(*self.HOBBIES_READING).click()
            if element == "Music":
                self.driver.find_element(*self.HOBBIES_MUSIC).click()

    def input_picture(self, path):
        picture = self.driver.find_element(*self.PICTURE)
        picture.send_keys(path)

    def enter_current_address(self, value):
        field = self.driver.find_element(*self.CURRENT_ADDRESS)
        field.send_keys(value)

    def select_state(self, state):
        field_state = self.driver.find_element(*self.STATE)
        field_state.click()
        path_state = f"//div[text()='{state}']"
        select_state = self.driver.find_element(By.XPATH, path_state)
        self.driver.execute_script("arguments[0].scrollIntoView();", select_state)
        select_state.click()

    def select_city(self, city):
        field_city = self.driver.find_element(*self.CITY)
        field_city.click()
        path_city = f"//div[text()='{city}']"
        select_city = self.driver.find_element(By.XPATH, path_city)
        self.driver.execute_script("arguments[0].scrollIntoView();", select_city)
        select_city.click()

    def close_modal(self):
        modal = self.fluent_wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Close']")))
        modal.click()

    def scroll_to_the_end(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_submit(self):
        submit_button = self.fluent_wait.until(ec.element_to_be_clickable(self.SUBMIT_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()

    def check_error(self):
        error = self.driver.find_element(*self.ERROR)
        return error

    def find_result_table(self):
        result_table = self.fluent_wait.until(ec.visibility_of_element_located(self.RESULT_TABLE))
        return result_table

    def close_result_table(self):
        button = self.driver.find_element(*self.CLOSE_RESULT_TABLE)
        button.click()

def positive_check():
    test            = None
    first_name      = "Alex"
    last_name       = "Smit"
    email           = "qwerty@mail.ru"
    gender          = "Other"
    phone_number    = "9876543211"
    month           = "2"
    year            = "1988"
    day             = "13"
    date            = day + " Mar " + year
    subjects        = ["Maths", "English", "History"]
    hobbies         = ["Sports", "Music"]
    path            = "/Users/e.khomiakov/Desktop/file.BVkAlq.png"
    current_address = "450 Park Avenue, Apt 3A, New York, NY 10022"
    state           = "Uttar Pradesh"
    city            = "Lucknow"

    try:
        test = TestSuite()
        test.set_up()
        test.close_modal()
        test.enter_first_name(first_name)
        test.enter_last_name(last_name)
        test.enter_email(email)
        test.select_gender(gender)
        test.enter_mobile_number(phone_number)
        test.select_date_of_birth(day, month, year)
        test.select_subjects(subjects)
        test.select_hobbies(hobbies)
        test.input_picture(path)
        test.enter_current_address(current_address)
        test.select_state(state)
        test.select_city(city)
        test.click_submit()
        error = test.check_error()
        assert not error.text, f"{error.text} - Ошибка ввода, проверь обязательные поля!"
        result_table = test.find_result_table()
        print(result_table.text)
        assert result_table.is_displayed()
        assert first_name in result_table.text, f"Введенное значение '{first_name}' не найдено в Модальном окне"
        assert last_name in result_table.text, f"Введенное значение '{last_name}' не найдено в Модальном окне"
        assert email in result_table.text, f"Введенное значение '{last_name}' не найдено в Модальном окне"
        assert gender in result_table.text, f"Введенное значение '{gender}' не найдено в Модальном окне"
        assert phone_number in result_table.text, f"Введенное значение '{email}' не найдено в Модальном окне"
        assert date in result_table.text, f"Введенное значение '{date}' не найдено в Модальном окне"
        for value in subjects:
            assert value in result_table.text, f"Введенное значение '{value}' не найдено в Модальном окне"
        for value in hobbies:
            assert value in result_table.text, f"Введенное значение '{value}' не найдено в Модальном окне"
        assert "Sports" in result_table.text, f"Введенное значение 'Sports' не найдено в Модальном окне"
        assert current_address in result_table.text, f"Введенное значение '{current_address}' не найдено в Модальном окне"
        assert state in result_table.text, f"Введенное значение '{state}' не найдено в Модальном окне"
        assert city in result_table.text, f"Введенное значение '{city}' не найдено в Модальном окне"
        test.close_result_table()
        print("Тест успешно пройден!")

    except AssertionError as error:
        print(f"Тест не пройден!: {error}")
        raise

    finally:
        if test:
            test.teardown()

positive_check()
