# Открыть страницу
# Нажать кнопку
# Перейти на новую вкладку
# На новой странице решить капчу для роботов

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from autotest_course.calculate import calc

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

button = browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary")
button.click()
time.sleep(5)

new_tab = browser.window_handles[1]
browser.switch_to.window(new_tab)

x = browser.find_element(By.ID, "input_value")

answer_field = browser.find_element(By.ID, "answer")
answer_field.send_keys(calc(x.text))

submit_button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
submit_button.click()
time.sleep(10)

