import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

# # Фикстура, которая открывает браузер для каждого теста в классе.
# # Команда yield указывает, что браузер надо закрыть после выполнения теста.
# @pytest.fixture()
# def browser():
#     print("\nstart browser for test")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser")
#     browser.quit()


class TestMainPage1():
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
