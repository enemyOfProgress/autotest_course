# Открыть страницу
# Посчитать сумму заданных чисел
# Выбрать в выпадающем списке значение, равное расчитанной сумме
# Нажать кнопку "Submit"

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from autotest_course.calculate import calc

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/selects1.html")

num_1 = driver.find_element(By.ID, "num1")
num_2 = driver.find_element(By.ID, "num2")


x = str(calc(int(num_1.text), int(num_2.text)))
print(x)

dropdown_list = Select(driver.find_element(By.ID, "dropdown"))
dropdown_list.select_by_value(x)

submit_button = driver.find_element(By.CLASS_NAME, "btn.btn-default")
submit_button.click()
time.sleep(5)





