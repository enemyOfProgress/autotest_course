import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


# # Фикстура, которая выполняется один раз в рамках класса.
# # Например, в данном случае, браузер запуститься один раз и в нем будут произведены все тесты из класса.
# @pytest.fixture(scope="class")
# def browser():
#     print("\nstart browser for test")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser")
#     browser.quit()


class TestMainPage1():
    def test_guest_should_see_login_link(self, browser):
        print("start test1")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("end test1")

    def test_guest_should_see_basket_link_on_main_page(self, browser):
        print("start test2")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("end test2")
