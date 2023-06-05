import pytest
from pages.auth_page import AuthPage
from pages.config import Config
from pages.locators import *

@pytest.mark.auth
def test_check_elem_auth_form(chrome_browser):
    """Проверяем что в форме "Авторизация присутствуют основные элементы"""
    page = AuthPage(chrome_browser)
    assert page.get_name_of_elem_auth() == Config.REQ_ELEMENTS_AUTH_FORM

@pytest.mark.auth
def test_auth_with_valid_data(chrome_browser):
    """Авторизация с позитивными валидными значениями""" # Предпологаю эндпоинт /my_account
    page = AuthPage(chrome_browser)
    page.enter_login(Config.VALID_LOGIN)
    page.enter_pass(Config.VALID_PASSWORD)
    page.btn_click()
    assert page.get_relative_link() == "/my_account", "Пользователь с позитивными валидными данными не авторизован!"

@pytest.mark.auth
def test_go_to_registration_page(chrome_browser):
    """Проверяем возможность перехода на страницу регистрации со страницы авторизации"""
    page = AuthPage(chrome_browser)
    page.go_to_reg_page()
    assert page.get_relative_link() == "/signup"

@pytest.mark.auth
def test_go_to_reset_password_page(chrome_browser):
    """Проверяем возможность перехода на страницу восстановления пароля со страницы авторизации"""
    page = AuthPage(chrome_browser)
    page.go_to_reset_password_page()
    assert page.get_relative_link() == "/restore"

@pytest.mark.auth
def test_go_back_to_auth_page_with_use_logo(chrome_browser):
    """Проверяем возможность возврата на страницу авторизации со страницы восстановления пароля
    с помощью логотипа в верхнем левом углу"""
    page = AuthPage(chrome_browser)
    page.go_to_reset_password_page()
    page.click_logo()
    assert page.get_relative_link() == "/signin"

@pytest.mark.auth
def test_read_privacy_policy(chrome_browser):
    """Проверяем возможность перехода на страницу ознакомления с политикой конфиденциальности со страницы авторизации"""
    page = AuthPage(chrome_browser)
    page.go_to_privacy_policy()
    assert page.get_relative_link() == "/policy", "ссылка не работает" # Предпологаю, что переходим в следующий эндпоинт

@pytest.mark.auth
def test_read_user_agreement(chrome_browser):
    """Проверяем возможность перехода на страницу ознакомления с пользовательским соглашением со страницы авторизации"""
    page = AuthPage(chrome_browser)
    page.go_to_user_agreement()
    assert page.get_relative_link() == "/policy", "ссылка не работает" # Предпологаю, что переходим в следующий эндпоинт
