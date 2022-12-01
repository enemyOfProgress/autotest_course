import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
button.click()

alert = browser.switch_to.alert
alert.accept()

x = browser.find_element(By.ID, "input_value")
value = x.text


def calc(x_value):
    return str(math.log(abs(12 * math.sin(int(x_value)))))


result = calc(value)
input_answer = browser.find_element(By.ID, "answer")
input_answer.send_keys(result)
submit_button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
submit_button.click()
time.sleep(10)
