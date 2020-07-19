from .pages.productt_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(driver, link) 
    page.open()
    page.add_product_to_the_cart()
    page.solve_quiz_and_get_code()
    page.should_be_info_msg()
    page.should_be_name_in_info_message()
    page.should_be_info_message_cart()
    page.should_be_correct_price()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_the_cart_few(driver,link):
    url = f"{link}"
    page = ProductPage(driver, url) 
    page.open()
    page.add_product_to_the_cart()
    page.solve_quiz_and_get_code()
    page.should_be_info_msg()
    page.should_be_name_in_info_message()
    page.should_be_info_message_cart()
    page.should_be_correct_price()


@pytest.mark.xfail(reason="success message exist while it should be displayed on the page")
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(driver, link)
    page.open()
    page.add_product_to_the_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(driver, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="success message is not disappeared")
def test_message_disappeared_after_adding_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(driver, link)
    page.open()
    page.add_product_to_the_cart()
    page.should_disappear_success_message()
    

def test_guest_should_see_login_link_on_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, link)
    page.open()
    page.should_be_login_link() 


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = LoginPage(driver, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(driver, link)
    product_page.open()
    product_page.go_to_the_cart()
    basket_page = BasketPage(driver, driver.current_url)
    basket_page.should_be_info_msg_empty_page()
    basket_page.should_not_be_added_items()


@pytest.mark.authorized_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page = LoginPage(driver, link)
        page.open()
        page.register_new_user(email='', password='')
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, driver):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(driver, link)
        page.open()
        page.should_not_be_success_message()
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, driver):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(driver, link)
        page.open()
        page.add_product_to_the_cart()
        page.should_be_info_msg()
        page.should_be_name_in_info_message()
        page.should_be_info_message_cart()
        page.should_be_correct_price()