# Открыть страницу
# Нажать кнопку
# Принять confirm
# На новой странице решить капчу для роботов

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from autotest_course.calculate import calc

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
button.click()

alert = browser.switch_to.alert
alert.accept()

x = browser.find_element(By.ID, "input_value")
value = x.text

result = calc(value)
input_answer = browser.find_element(By.ID, "answer")
input_answer.send_keys(result)
submit_button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
submit_button.click()
time.sleep(10)
