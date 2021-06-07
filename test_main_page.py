# pytest -v --tb=line --language=en test_main_page.py # Выводим только одну строку из лога каждого упавшего теста.
# from .pages.main_page import MainPage
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"

def test_login_url_contains_login(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()

def test_login_form_is_present(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()

def test_register_form_is_present(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()



#def test_guest_can_go_to_login_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/"
#    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#    page.open()                      # открываем страницу
#    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

#def test_guest_should_see_login_link(browser):
#    link = "http://selenium1py.pythonanywhere.com/"
#    page = MainPage(browser, link)
#    page.open()
#    page.should_be_login_link()







