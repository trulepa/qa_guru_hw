import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

class TestSuite:
    FIRST_NAME_LOCATOR          = (By.ID, "firstName")
    LAST_NAME_LOCATOR           = (By.ID, "lastName")
    EMAIL_LOCATOR               = (By.ID, "userEmail")
    GENDER_MALE_LOCATOR         = (By.ID, "gender-radio-1")
    GENDER_FEMALE_LOCATOR       = (By.ID, "gender-radio-2")
    GENDER_OTHER_LOCATOR        = (By.ID, "gender-radio-3")
    MOBILE_NUMBER_LOCATOR       = (By.ID, "userNumber")
    DATE_OF_BIRTH_LOCATOR       = (By.ID, "dateOfBirthInput")
    SUBJECTS_LOCATOR            = (By.ID, "subjectsInput")
    HOBBIES_SPORT_LOCATOR       = (By.ID, "hobbies-checkbox-1")
    HOBBIES_READING_LOCATOR     = (By.ID, "hobbies-checkbox-2")
    HOBBIES_MUSIC_LOCATOR       = (By.ID, "hobbies-checkbox-3")
    PICTURE_LOCATOR             = (By.ID, "uploadPicture")
    CURRENT_ADDRESS_LOCATOR     = (By.ID, "currentAddress")
    STATE_LOCATOR               = (By.ID, "state")
    CITY_LOCATOR                = (By.ID, "city")
    SUBMIT_BUTTON_LOCATOR       = (By.ID, "submit")
    RESULT_TABLE_LOCATOR        = (By.ID, "resultBody")
    CLOSE_RESULT_TABLE_LOCATOR  = (By.ID, "closeModal")
    ERROR_LOCATOR               = (By.ID, "formError")

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
        field = self.driver.find_element(*self.FIRST_NAME_LOCATOR)
        field.send_keys(value)

    def enter_last_name(self, value: str):
        field = self.driver.find_element(*self.LAST_NAME_LOCATOR)
        field.send_keys(value)

    def enter_email(self, value: str):
        field = self.driver.find_element(*self.EMAIL_LOCATOR)
        field.send_keys(value)

    def select_gender_male(self):
        radio = self.driver.find_element(*self.GENDER_MALE_LOCATOR)
        radio.click()

    def select_gender_female(self):
        radio = self.driver.find_element(*self.GENDER_FEMALE_LOCATOR)
        radio.click()

    def select_gender_other(self):
        radio = self.driver.find_element(*self.GENDER_OTHER_LOCATOR)
        radio.click()

    def enter_mobile_number(self, value):
        field = self.driver.find_element(*self.MOBILE_NUMBER_LOCATOR)
        field.send_keys(value)

    def select_date_of_birth(self, day: str, month: str, year: str):
        field = self.driver.find_element(*self.DATE_OF_BIRTH_LOCATOR)
        field.click()

        select_month = Select(self.driver.find_element(By.CSS_SELECTOR, "select.react-datepicker__month-select"))
        select_month.select_by_value(month)
        select_year = Select(self.driver.find_element(By.CSS_SELECTOR, "select.react-datepicker__year-select"))
        select_year.select_by_value(year)

        span = f"span[data-day='{day}']"
        select_day = self.driver.find_element(By.CSS_SELECTOR, span)
        select_day.click()

    def select_subjects(self, value):
        subjects = self.driver.find_element(*self.SUBJECTS_LOCATOR)
        email = self.driver.find_element(*self.EMAIL_LOCATOR)  # Перевести курсор хоть куда для клика - кривая форма "subjects"

        for element in value:
            email.click()  # Кликаем по почте
            subjects.click()
            xpath = f"//div[@class='subjects-auto-complete__option' and text()='{element}']"
            self.fluent_wait.until(EC.visibility_of_element_located((By.XPATH, xpath))).click()
            # self.driver.find_element(By.XPATH, xpath).click()

    def select_hobbies_sport(self):
        self.driver.find_element(*self.HOBBIES_SPORT_LOCATOR).click()

    def select_hobbies_reading(self):
        self.driver.find_element(*self.HOBBIES_READING_LOCATOR).click()

    def select_hobbies_music(self):
        self.driver.find_element(*self.HOBBIES_MUSIC_LOCATOR).click()

    def input_picture(self, path):
        picture = self.driver.find_element(*self.PICTURE_LOCATOR)
        picture.send_keys(path)

    def enter_current_address(self, value):
        field = self.driver.find_element(*self.CURRENT_ADDRESS_LOCATOR)
        field.send_keys(value)

    def select_state_and_city(self, state, city):
        field_state = self.driver.find_element(*self.STATE_LOCATOR)
        field_state.click()
        path_state = f"//div[text()='{state}']"
        select_state = self.driver.find_element(By.XPATH, path_state)
        self.driver.execute_script("arguments[0].scrollIntoView();", select_state)
        select_state.click()

        field_city = self.driver.find_element(*self.CITY_LOCATOR)
        field_city.click()
        path_city = f"//div[text()='{city}']"
        select_city = self.driver.find_element(By.XPATH, path_city)
        self.driver.execute_script("arguments[0].scrollIntoView();", select_city)
        select_city.click()

    def close_modal(self):
        # modal = self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Close']")
        modal = self.fluent_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Close']")))
        modal.click()

    def scroll_to_the_end(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_submit(self):
        # submit_button = self.driver.find_element(*self.SUBMIT_BUTTON_LOCATOR)
        submit_button = self.fluent_wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON_LOCATOR))
        self.driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()

    def check_error(self):
        error = self.driver.find_element(*self.ERROR_LOCATOR)
        return error

    def find_result_table(self):
        # result_table = self.driver.find_element(*self.RESULT_TABLE_LOCATOR)
        result_table = self.fluent_wait.until(EC.visibility_of_element_located(self.RESULT_TABLE_LOCATOR))
        return result_table

    def close_result_table(self):
        button = self.driver.find_element(*self.CLOSE_RESULT_TABLE_LOCATOR)
        button.click()
        # time.sleep(2)


def positive_check():
    test            = None
    first_name      = "Alex"
    last_name       = "Smit"
    email           = "qwerty@mail.ru"
    phone_number    = "9876543210"
    month           = "2"
    year            = "1988"
    day             = "13"
    date            = day + " Mar " + year
    subjects        = ["Maths", "English", "History"]
    path            = "/Users/e.khomiakov/Desktop/file.BVkAlq.png"
    current_address = "450 Park Avenue, Apt 3A, New York, NY 10022"
    state           = "Uttar Pradesh"
    city            = "Lucknow"
    state_and_city  = state + " " + city

    try:
        test = TestSuite()
        test.set_up()
        test.close_modal()
        test.enter_first_name(first_name)
        test.enter_last_name(last_name)
        test.enter_email(email)
        test.select_gender_male()
        test.enter_mobile_number(phone_number)
        test.select_date_of_birth(day, month, year)
        test.select_subjects(subjects)
        test.select_hobbies_sport()
        test.input_picture(path)
        test.enter_current_address(current_address)
        # test.scroll_to_the_end()
        test.select_state_and_city(state, city)
        test.click_submit()
        error = test.check_error()
        result_table = test.find_result_table()
        # print(result_table.text)
        assert result_table.is_displayed()
        assert error.text != "Please fill required fields and enter a valid 10-digit mobile number.", "Ошибка ввода, проверь обязательные поля!"
        assert first_name in result_table.text, f"Введенное значение '{first_name}' не найдено в Модальном окне"
        assert last_name in result_table.text, f"Введенное значение '{last_name}' не найдено в Модальном окне"
        assert email in result_table.text, f"Введенное значение '{last_name}' не найдено в Модальном окне"
        assert "Male" in result_table.text, f"Введенное значение 'Male' не найдено в Модальном окне"
        assert phone_number in result_table.text, f"Введенное значение '{email}' не найдено в Модальном окне"
        assert date in result_table.text, f"Введенное значение '{date}' не найдено в Модальном окне"
        for value in subjects:
            assert value in result_table.text, f"Введенное значение '{value}' не найдено в Модальном окне"
        assert "Sports" in result_table.text, f"Введенное значение 'Sports' не найдено в Модальном окне"
        assert current_address in result_table.text, f"Введенное значение '{current_address}' не найдено в Модальном окне"
        assert state_and_city in result_table.text, f"Введенное значение '{state_and_city}' не найдено в Модальном окне"
        test.close_result_table()
        print("Тест успешно пройден!")

    except AssertionError as error:
        print(f"Тест не пройден!: {error}")
        raise

    finally:
        if test:
            test.teardown()


positive_check()
