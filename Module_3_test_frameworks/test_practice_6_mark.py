import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    # Добавляем маркировку, чтобы можно было запустить нужный тест через консоль:
    # pytest -m smoke test_practice_6_mark.py
    # Также можно запускать инверсию pytest -m "not smoke" test_practice_6_mark.py
    # В данном случае запустятся те тесты, которые не промаркированы, как smoke.
    # Также можно использовать ИЛИ pytest -m "smoke or regression" test_practice_6_mark.py
    # Также можно использовать И pytest -m "smoke and win10" test_practice_6_mark.py
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")