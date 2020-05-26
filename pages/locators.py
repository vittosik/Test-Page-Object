from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini .btn")
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, "div.basket-items")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner p')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators:
    LOGIN_URL = (By.ID, "login_link")
    LOGIN_FORM = (By.CLASS_NAME, 'login_form')
    REGISTER_FORM = (By.CLASS_NAME, 'register_form')
    EMAIL_FIELD = (By.NAME, 'registration-email')
    PASSWORD_FIELD1 = (By.NAME, 'registration-password1')
    PASSWORD_FIELD2 = (By.NAME, 'registration-password2')
    REG_BUTTON = (By.NAME, 'registration_submit')

class ProductPageLocators:
    ADD_TO_BASKET =(By.ID, 'add_to_basket_form')
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")