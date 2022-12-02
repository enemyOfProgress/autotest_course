import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()


def fill_registration_field():
    first_name_filed = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group .form-control.first")
    first_name_filed.send_keys("Ivan")
    last_name_field = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group .form-control.second")
    last_name_field.send_keys("Ivanov")
    email_field = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group .form-control.third")
    email_field.send_keys("test@gmail.com")


def submit_button_click():
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


def check_successfully_registration():
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert welcome_text == "Congratulations! You have successfully registered!", "Should be absolute value of a number"


def test_registration_form_1():
    link = "http://suninjuly.github.io/registration1.html"
    browser.get(link)
    fill_registration_field()
    submit_button_click()
    time.sleep(5)
    check_successfully_registration()


def test_registration_form_2():
    link = "http://suninjuly.github.io/registration2.html"
    browser.get(link)
    fill_registration_field()
    submit_button_click()
    time.sleep(5)
    check_successfully_registration()


if __name__ == "__main__":
    pytest.main()
