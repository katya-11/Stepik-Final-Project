from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, driver):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(driver, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()


    def test_guest_should_see_login_link(self, driver):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(driver, link)
        page.open()
        page.should_be_login_link()


def test_login_form(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(driver, link)
    page.open()
    page.go_to_login_page()
    login_form = LoginPage(driver, driver.current_url)
    login_form.should_be_login_form()


def test_register_form(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(driver, link)
    page.open()
    page.go_to_login_page()
    register_form = LoginPage(driver, driver.current_url)
    register_form.should_be_register_form()


def test_guest_cant_see_product_in_basket_opened_from_main_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    basket = BasketPage(driver, link)
    basket.open()
    basket.go_to_the_cart()
    basket.should_be_info_msg_empty_page()
    basket.should_not_be_added_items()

