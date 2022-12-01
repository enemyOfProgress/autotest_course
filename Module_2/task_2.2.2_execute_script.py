# Открыть страницу
# Считать данные для переменной х
# Посчитать функцию от х
# Проскролить страницу вниз
# Ввести ответ в текстовое поле
# Отметить чекбокс i'm the robot
# Отметить radio button robots rule
# Нажать кнопку submit

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from autotest_course.functions import calc

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/execute_script.html")

x = browser.find_element(By.ID, "input_value")

answer_field = browser.find_element(By.ID, "answer")
answer_field.send_keys(calc(int(x.text)))

submit_button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)

robot_check = browser.find_element(By.ID, "robotCheckbox")
robot_check.click()

robots_rule = browser.find_element(By.ID, "robotsRule")
robots_rule.click()
time.sleep(5)
