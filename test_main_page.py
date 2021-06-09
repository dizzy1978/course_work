# pytest -v --tb=line --language=en test_main_page.py # Выводим только одну строку из лога каждого упавшего теста.
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.skip
def test_login_url_contains_login(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()

@pytest.mark.skip
def test_login_form_is_present(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()

@pytest.mark.skip
def test_register_form_is_present(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.check_empty_basket_main()
    page.should_not_be_success_message()


