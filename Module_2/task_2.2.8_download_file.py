# Открыть страницу
# Заполнить поля: имя, фамилия, мел
# Загрузить файл
# Нажать кнопку submit

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

first_name = browser.find_element(By.NAME, "firstname")
first_name.send_keys("Ivanov")
last_name = browser.find_element(By.NAME, "lastname")
last_name.send_keys("Ivan")
email = browser.find_element(By.NAME, "email")
email.send_keys("test@gmail.com")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, '../../Module_2_selenium_methods/module_2.2/practice_2.5.py')

choose_file = browser.find_element(By.ID, "file")
choose_file.send_keys(file_path)
time.sleep(5)