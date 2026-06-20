from selenium import webdriver
from pom_registration_form import RegistrationForm

def positive_check():
    test            = None
    driver          = webdriver.Chrome()
    first_name      = "Alex"
    last_name       = "Smit"
    email           = "qwerty@mail.ru"
    gender          = "Male"
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
        test = RegistrationForm(driver)
        test.set_up() \
            .close_modal() \
            .fill_form(first_name, last_name, email, phone_number, current_address) \
            .select_gender(gender) \
            .select_date_of_birth(day, month, year) \
            .select_subjects(subjects) \
            .select_hobbies(sports=True) \
            .input_picture(path) \
            .select_state_and_city(state, city) \
            .click_submit()
        error = test.check_error()
        assert not error.text, f"{error.text}, Ошибка ввода, проверь обязательные поля!"
        result_table = test.find_result_table()
        assert result_table.is_displayed()
        assert first_name in result_table.text, f"Введенное значение '{first_name}' не найдено в Модальном окне"
        assert last_name in result_table.text, f"Введенное значение '{last_name}' не найдено в Модальном окне"
        assert email in result_table.text, f"Введенное значение '{last_name}' не найдено в Модальном окне"
        assert gender in result_table.text, f"Введенное значение '{gender}' не найдено в Модальном окне"
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