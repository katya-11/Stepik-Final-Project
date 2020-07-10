from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators ():
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

