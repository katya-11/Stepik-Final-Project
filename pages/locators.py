from selenium.webdriver.common.by import By


#class MainPageLocators():
    #LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_FORM_EMAIL_FIELD = (By.CSS_SELECTOR, "#login_form  [type = 'email']")
    LOGIN_FORM_PW_FIELD = (By.CSS_SELECTOR, "#login_form  [type = 'password']")
    LOGIN_FORM_SUBMIT_BTN = (By.CSS_SELECTOR, "#login_form  [name = 'login_submit']")
    LOGIN_FORM_FORGOT_PW_LINK = (By.CSS_SELECTOR, "#login_form  [href]")

    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL_FIELD = (By.CSS_SELECTOR, "#register_form  [type = 'email']")
    REGISTER_FORM_PW_FIELD = (By.CSS_SELECTOR, "#register_form #id_registration-password1")
    REGISTER_FORM_CONFIRM_PW_FIELD = (By.CSS_SELECTOR, "#register_form #id_registration-password2")
    REGISTER_FORM_REGISTER_BTN = (By.CSS_SELECTOR, "#register_form [name = 'registration_submit']")

class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".product_main [value ='Add to basket']")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    INFO_MSG_ADD_TO_CART = (By.CSS_SELECTOR, "#messages .alert-success strong")
    INFO_MSG_CART_TOTAL = (By.CSS_SELECTOR, "#messages .alert-info")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_BASKET_BTN = (By.CSS_SELECTOR, ".basket-mini .btn-default[href]")



class BasketPageLocators:
    LINK_MSG_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p [href]")
    BASKET_IS_NOT_EMPTY = (By.CSS_SELECTOR, "#basket_totals")


