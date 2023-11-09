from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
from .locators import CartPageLocators

class CartPage(BasePage):
    def is_not_element_present(self):
        super().is_not_element_present(*CartPageLocators.GOODS_IN_CART), \
            "Goods in cart is presented, but should not be"
        



    
        