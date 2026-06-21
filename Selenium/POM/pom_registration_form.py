from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

class RegistrationForm:
    URL                 = "https://qa-guru.github.io/one-page-form/automation-practice-form.html"
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

    def __init__(self, driver):
        self.driver = driver
        self.fluent_wait = WebDriverWait(
            self.driver,
            timeout=10,
            poll_frequency=0.5,
            ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]
        )

    def set_up(self):
        driver = self.driver
        driver.get(self.URL)
        driver.maximize_window()
        driver.implicitly_wait(5)
        return self

    def teardown(self):
        self.driver.quit()

    def fill_form(self, first_name=None, last_name=None, email=None, mobile_number=None, current_address=None):
        if first_name is not None:
            self.driver.find_element(*self.FIRST_NAME) \
                .send_keys(first_name)
        if last_name is not None:
            self.driver.find_element(*self.LAST_NAME) \
                .send_keys(last_name)
        if email is not None:
            self.driver.find_element(*self.EMAIL) \
                .send_keys(email)
        if mobile_number is not None:
            self.driver.find_element(*self.MOBILE_NUMBER) \
                .send_keys(mobile_number)
        if current_address is not None:
            self.driver.find_element(*self.CURRENT_ADDRESS) \
                .send_keys(current_address)
        return self

    def select_gender(self, gender=None):
        if gender == "Male":
            self.driver.find_element(*self.GENDER_MALE) \
                .click()
        if gender == "Female":
            self.driver.find_element(*self.GENDER_FEMALE) \
                .click()
        if gender == "Other":
            self.driver.find_element(*self.GENDER_OTHER) \
                .click()
        return self

    def select_date_of_birth(self, day: str, month: str, year: str):
        self.driver.find_element(*self.DATE_OF_BIRTH) \
            .click()

        select_month = Select(self.driver.find_element(By.CSS_SELECTOR, "select.react-datepicker__month-select"))
        select_month.select_by_value(month)
        select_year = Select(self.driver.find_element(By.CSS_SELECTOR, "select.react-datepicker__year-select"))
        select_year.select_by_value(year)

        span = f"span[data-day='{day}']"
        self.driver.find_element(By.CSS_SELECTOR, span) \
            .click()
        return self

    def select_subjects(self, value):
        subjects = self.driver.find_element(*self.SUBJECTS)
        email = self.driver.find_element(*self.EMAIL)

        for element in value:
            email.click()  # Кликаем по почте
            subjects.click()
            xpath = f"//div[@class='subjects-auto-complete__option' and text()='{element}']"
            self.fluent_wait.until(ec.visibility_of_element_located((By.XPATH, xpath))) \
                .click()
        return self

    def select_hobbies(self, hobbies):
        for element in hobbies:
            if element == "Sports":
                self.driver.find_element(*self.HOBBIES_SPORTS).click()
            if element == "Reading":
                self.driver.find_element(*self.HOBBIES_READING).click()
            if element == "Music":
                self.driver.find_element(*self.HOBBIES_MUSIC).click()
        return self

    def input_picture(self, path):
        self.driver.find_element(*self.PICTURE) \
            .send_keys(path)
        return self

    def select_options(self, locator, option, scroll=True):
        field = self.driver.find_element(*locator)
        field.click()
        path = f"//div[text()='{option}']"
        select_option = self.driver.find_element(By.XPATH, path)
        if scroll:
            self.driver.execute_script("arguments[0].scrollIntoView();", select_option)
        select_option.click()
        return self

    def select_state(self, state):
        return self.select_options(self.STATE, state)

    def select_city(self, city):
        return self.select_options(self.CITY, city)

    def close_modal(self):
        self.fluent_wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Close']"))) \
            .click()
        return self

    def scroll_to_the_end(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return self

    def click_submit(self):
        submit_button = self.fluent_wait.until(ec.element_to_be_clickable(self.SUBMIT_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()
        return self

    def check_error(self):
        error = self.driver.find_element(*self.ERROR)
        return error

    def find_result_table(self):
        result_table = self.fluent_wait.until(ec.visibility_of_element_located(self.RESULT_TABLE))
        return result_table

    def close_result_table(self):
        self.driver.find_element(*self.CLOSE_RESULT_TABLE) \
            .click()