from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_button_add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD), "Button add to cart is not presented"


    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        button.click()
    
    def should_be_pop_up_cart(self):
        assert self.browser.find_element(*ProductPageLocators.POP_UP_CART), "Pop up cart is not presented"

    def check_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_ON_PAGE)
        cost = self.browser.find_element(*ProductPageLocators.PRICE_ON_POP_UP)
        assert price.text == cost.text, f"Price on pop up {ProductPageLocators.PRICE_ON_POP_UP} insteed {ProductPageLocators.PRICE_ON_PAGE}"
    
    def check_name(self):
        nameOP = self.browser.find_element(*ProductPageLocators.NAME_ON_PAGE)
        nameOM = self.browser.find_element(*ProductPageLocators.NAME_ON_POP_UP)
        assert nameOM.text == nameOP.text, f"Name of book {ProductPageLocators.NAME_ON_POP_UP} insteed {ProductPageLocators.NAME_ON_PAGE}"

    def is_not_element_present(self):
        super().is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
        
    def should__not_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disapeared, but should be"



     