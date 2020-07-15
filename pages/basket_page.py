from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_info_msg_empty_page(self):
        empty_info_msg = self.driver.find_element(*BasketPageLocators.LINK_MSG_EMPTY_BASKET)
        empty_info_url = empty_info_msg.get_attribute('href')
        main_page_url = 'http://selenium1py.pythonanywhere.com/en-gb/'
        assert empty_info_url in main_page_url, "There are no info message and link on empty basket"

    def should_not_be_added_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_NOT_EMPTY), "There are some added items in " \
                                                                                     "the basket. Basket should be " \
                                                                                     "empty "
