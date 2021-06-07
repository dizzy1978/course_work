# pytest -v --tb=line --language=en test_main_page.py # Выводим только одну строку из лога каждого упавшего теста.

link = "http://selenium1py.pythonanywhere.com/"

def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()

def test_guest_can_go_to_login_page(browser):
   browser.get(link)
   go_to_login_page(browser)


# Было:
#def test_guest_can_go_to_login_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/"
#    browser.get(link)
#    login_link = browser.find_element_by_css_selector("#login_link")
#    login_link.click()

# Список методов PO, ассоциированных с одной страницей в отдельном классе
def test_add_to_cart(browser):
    page = ProductPage(url="", browser)   # инициализируем объект Page Object
    page.open()                           # открываем страницу в браузере
    page.should_be_add_to_cart_button()   # проверяем что есть кнопка добавления в корзину
    page.add_product_to_cart()            # жмем кнопку добавить в корзину
    page.should_be_success_message()      # проверяем что есть сообщение с нужным текстом