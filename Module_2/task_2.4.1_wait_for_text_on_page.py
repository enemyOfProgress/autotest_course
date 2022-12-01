Открыть страницу
Дождаться, когда цена будет $100
Нажать на кнопку book


import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from autotest_course.calculate import calc

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
browser.implicitly_wait(5)

price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
book_button = browser.find_element(By.ID, "book")
book_button.click()

input_value = browser.find_element(By.ID, "input_value")
answer_field = browser.find_element(By.ID, "answer")
answer_field.send_keys(calc(input_value.text))

submit_button = browser.find_element(By.ID, "solve")
submit_button.click()
time.sleep(10)
