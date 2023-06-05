from selenium.webdriver.common.by import By


class AuthLocators:
    AUTH_TITLE = (By.XPATH, "//*[@class='_header_1tk9s_2']/h1")  # названия формы авторизации "Привет!"
    AUTH_LOGIN = (By.XPATH, "//*[@type='email']")  # Поле ввода логина
    AUTH_PASS = (By.XPATH, "//*[@type='password']")  # Поле ввода пароля
    AUTH_BTN = (By.XPATH, "//*[@type='submit']")  # Кнопка "Войти" формы авторизации
    LOGO_BTN = (By.XPATH, "//*[@class='_right-block_1k4bv_7']")  # кнопка с Логотипом для возврата на домашнюю страницу /signin
    REG_BTN = (By.XPATH, "//*[@class='_help-btn_1tk9s_13']")  # кнопка "Регистрация" в форме авторизации
    RES_BTN = (By.XPATH, "//*[@class='_forgotPassword_1tk9s_19']") # кнопка "Забыл пароль" в форме авторизации
    FIELDS = (By.XPATH, "//*[@class='label']") # названия полей Email и Пароль тут
    PRIVACY_POLICY = (By.XPATH, "//*[@class='_footer_pg7rs_2']/a[1]") # ссылка на политику конфедициальности в футере
    USER_AGREE = (By.XPATH, "//*[@class='_footer_pg7rs_2']/a[2]") # ссылка на пользовательское соглашение в футере

    AUTH_CONT = (By.CLASS_NAME, "._container_wu16z_2") # контейнер авторизации
