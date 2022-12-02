import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_registration_form_1():
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name_filed = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group .form-control.first")
    first_name_filed.send_keys("Ivan")

    last_name_field = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group .form-control.second")
    last_name_field.send_keys("Ivanov")

    email_field = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group .form-control.third")
    email_field.send_keys("test@gmail.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    time.sleep(5)

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert welcome_text == "Congratulations! You have successfully registered!", "Should be absolute value of a number"


def test_registration_form_2():
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name_filed = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group .form-control.first")
    first_name_filed.send_keys("Ivan")

    last_name_field = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group .form-control.second")
    last_name_field.send_keys("Ivanov")

    email_field = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group .form-control.third")
    email_field.send_keys("test@gmail.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    time.sleep(5)

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert welcome_text == "Congratulations! You have successfully registered!", "Should be absolute value of a number"


if __name__ == "__main__":
    pytest.main()
