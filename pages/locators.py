from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators ():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form1")
    LOGIN_FORM_EMAIL_FIELD = (By.CSS_SELECTOR, "#login_form1  [type = 'email']")
    LOGIN_FORM_PW_FIELD = (By.CSS_SELECTOR, "#login_form1  [type = 'password']")
    LOGIN_FORM_SUBMIT_BTN = (By.CSS_SELECTOR, "#login_form1  [name = 'login_submit']")
    LOGIN_FORM_FORGOT_PW_LINK = (By.CSS_SELECTOR, "#login_form1  [href]")

    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form1")
    REGISTER_FORM_EMAIL_FIELD = (By.CSS_SELECTOR, "#register_form1  [type = 'email']")
    REGISTER_FORM_PW_FIELD = (By.CSS_SELECTOR, "#register_form1 #id_registration-password1")
    REGISTER_FORM_CONFIRM_PW_FIELD = (By.CSS_SELECTOR, "#register_form1 #id_registration-password2")
    REGISTER_FORM_REGISTER_BTN = (By.CSS_SELECTOR, "#register_form1 [name = 'registration_submit']")

