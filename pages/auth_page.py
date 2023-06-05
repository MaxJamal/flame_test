import re
from pages.base_page import BasePage
from pages.locators import *
from pages.config import Config


class AuthPage(BasePage):
    """Создаем класс страницы авторизации """
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = Config.BASE_URL or "https://auth.dev-team-flame.ru/signin"
        driver.get(url)
    #создаем нужные элементы
        self.login = driver.find_element(*AuthLocators.AUTH_LOGIN)
        self.password = driver.find_element(*AuthLocators.AUTH_PASS)
        self.btn_submit = driver.find_element(*AuthLocators.AUTH_BTN)
        self.btn_res = driver.find_element(*AuthLocators.RES_BTN)
        self.btn_reg = driver.find_element(*AuthLocators.REG_BTN)
        self.privacy = driver.find_element(*AuthLocators.PRIVACY_POLICY)
        self.user_agree = driver.find_element(*AuthLocators.USER_AGREE)

    def enter_login(self, value):
        """Ввести данные в поле логина"""
        self.login.send_keys(value)

    def enter_pass(self, value):
        """Ввести пароль"""
        self.password.send_keys(value)

    def btn_click(self):
        """Нажать на кнопку "Войти" """
        self.btn_submit.click()

    def get_name_of_elem_auth(self):
        """ Получаем названия всех элементов в форме авторизации "Привет!" """
        title = self.find_element(AuthLocators.AUTH_TITLE)
        fields = self.find_elements(AuthLocators.FIELDS)
        fields = ''.join([x.text for x in fields])
        fields_names = re.sub(r"([А-Я])", r" \1", fields).split()
        elements = fields_names + [title.text, self.btn_res.text, self.btn_submit.text, self.btn_reg.text]
        return elements

    def go_to_privacy_policy(self):
        """Ознакомиться с политикой конфиденциальности на странице авторизации"""
        self.privacy.click()

    def go_to_user_agreement(self):
        """Ознакомиться с пользовательским соглашением на странице авторизации"""
        self.user_agree.click()
