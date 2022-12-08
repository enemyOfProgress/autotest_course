import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Parametrize передает в переменную каждое новое значение для теста.
@pytest.mark.parametrize('lesson', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_authorize_stepik(browser, lesson):
    start_browser(browser, lesson)
    click_login(browser)
    fill_login_form(browser)
    click_form_login_button(browser)
    time.sleep(15)
    input_answer(browser)
    click_submit_button(browser)
    is_answer_correct(browser)


def start_browser(browser, lesson):
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.get(link)
    browser.implicitly_wait(20)


def click_login(browser):
    login_button = browser.find_element(By.ID, "ember33")
    login_button.click()


def fill_login_form(browser):
    email_filed = browser.find_element(By.ID, "id_login_email")
    email_filed.send_keys("vorobiov.bohdan@gmail.com")
    password_field = browser.find_element(By.ID, "id_login_password")
    password_field.send_keys("p4$$F0rK3k")


def click_form_login_button(browser):
    accept_login_button = browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader")
    accept_login_button.click()


def input_answer(browser):
    answer = math.log(int(time.time()))
    answer_field = browser.find_element(By.CSS_SELECTOR, "textarea")
    answer_field.send_keys(str(answer))


def click_submit_button(browser):
    submit_button = WebDriverWait(browser, 7).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    submit_button.click()


def is_answer_correct(browser):
    text_in_hint = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.CLASS_NAME, "smart-hints__hint")))
    print(text_in_hint.text)
    assert text_in_hint.text == "Correct!", "There isn't correct!"
