from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, f"Ожидаемая подстрока 'login' не найдена в URL: {LoginPageLocators.LOGIN_URL}"


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)# реализуйте проверку, что есть форма логина

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM)# реализуйте проверку, что есть форма регистрации на странице

    def register_new_user(self, email, password):
        input1 = self.browser.find_element(*LoginPageLocators.INPUT_EMAIL) 
        input1.send_keys(email)
        input2 = self.browser.find_element(*LoginPageLocators.INPUT_PASWORD)
        input2.send_keys(password)
        input3 = self.browser.find_element(*LoginPageLocators.INPUT_REPEAT_PASSWORD)
        input3.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()
