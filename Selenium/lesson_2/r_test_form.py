import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def set_up_test(driver):
    # 2. Открытие страницы
    driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
    driver.maximize_window()
    time.sleep(5)  # Пауза, чтобы визуально заметить открытие


def tear_down_test(driver):
    # 5. Закрытие браузера в любом случае
    driver.quit()

#full_name_locator = "userName"
full_name_locator = (By.ID, "userName")
email_locator = "userEmail"
submit_button_locator = "submit"
result_box_locator = "output"

def test01():
    print("Рефакторинг - итерация 1!")

    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        set_up_test(driver)

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        #full_name_field = driver.find_element(By.ID, full_name_locator)
        full_name_field = driver.find_element(*full_name_locator)
        #web_elements = driver.find_elements(By.XPATH, "someXPath")

        full_name_field.send_keys("Иван Иванов")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, email_locator)
        email_field.send_keys("ivan@example.com")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, submit_button_locator)
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки
        
        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, result_box_locator)
        
        # Проверяем, что в блоке результата появился введенный текст
        assert "Иван Иванов" in result_box.text
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        tear_down_test(driver)

def test02():
    print("Рефакторинг - итерация 1!")

    # 1. Запуск браузера Chrome
    driver = webdriver.Chrome()

    try:
        set_up_test(driver)

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        #full_name_field = driver.find_element(By.ID, full_name_locator)
        full_name_field = driver.find_element(*full_name_locator)

        full_name_field.send_keys("")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, email_locator)
        email_field.send_keys("ivanexample.com")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, submit_button_locator)
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки
        
        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, result_box_locator)
        
        # Проверяем, что в блоке результата появился введенный текст
        assert "ivanexample.com" in result_box.text
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        tear_down_test(driver)

test01()
test02()
