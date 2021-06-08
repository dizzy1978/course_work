# pytest -v --tb=line --language=en test_product_page.py # Выводим только одну строку из лога каждого упавшего теста.
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.control_added_label()
    page.control_added_price()




