from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():
    # Класс, который запускает браузер для теста
    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite...")
        self.browser = webdriver.Chrome()

    # Класс, который закрывает браузер после теста
    @classmethod
    def teardown_class(self):
        print("quit browser for test suite...")

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self):
        print("star browser for test")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

