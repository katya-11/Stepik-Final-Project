from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_the_cart(self):
        add_to_cart_btn = self.driver.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_btn.click()

    def should_be_info_msg(self):
        assert self.is_element_present(*ProductPageLocators.INFO_MSG_ADD_TO_CART),"No 'added to cart' info message"

    def should_be_name_in_info_message(self):
        product_name_value = self.driver.find_element(*ProductPageLocators.PRODUCT_NAME).text
        info_message = self.driver.find_element(*ProductPageLocators.INFO_MSG_ADD_TO_CART).text
        assert product_name_value == info_message,\
            f"Incorrect name of added to the cart product. Expected {product_name_value}, got {info_message}"

    def should_be_info_message_cart(self):
        assert self.is_element_present(*ProductPageLocators.INFO_MSG_CART_TOTAL),"No price info message on the product details page"

    def should_be_correct_price(self):
        product_price_value = self.driver.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        cart_total = self.driver.find_element(*ProductPageLocators.INFO_MSG_CART_TOTAL).text
        assert product_price_value in cart_total,\
            f"The product price is not equal cart total. Expected {product_price_value}, got {cart_total}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
         "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should disappear, but it's not"
