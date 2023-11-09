from selenium.webdriver.common.by import By
from selenium import webdriver


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_url")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    BUTTON_ADD = (By.XPATH,'//*[@id="add_to_basket_form"]/button')
    POP_UP_CART = (By.ID, "messages")
    PRICE_ON_PAGE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    PRICE_ON_POP_UP = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    NAME_ON_PAGE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    NAME_ON_POP_UP = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]')

class CartPageLocators():
    GOODS_IN_CART = (By.ID, "basket_formset")
    BUTTON_GO_TO_CART = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')