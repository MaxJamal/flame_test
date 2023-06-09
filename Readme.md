# Тестовое задание на должность "QA Engineer" в команду flame.ru

Объект тестирования: https://auth.dev-team-flame.ru/signin

# Коротко о задании:

1. Тест кейсы и чек листы могут носить свободный характер. Формат и оформление тест кейсов на ваше усмотрение.
2. Нам важен результат. Но также мы способны оценить и ваше чувство прекрасного :)
3. Первый уровень => обязательный уровень выполнения домашнего задания.
4. Остальные уровни выполняются сугубо по желанию, но каждый последующий дает +10 очков крутизны))

## Первый уровень

Кейс 1.Составить чек-лист для проверки основных элементов на странице (https://auth.dev-team-flame.ru/signin).

Кейс 2.Написать тестовый сценарий для навигационного меню сайта (https://auth.dev-team-flame.ru/signin) (открытие вкладок, проверка URL и т.д)

Кейс 3.Составить краткий план для регресса страницы (https://auth.dev-team-flame.ru/signin)

Кейс 4.Составить полный список тест-кейсов по странице

## Второй уровень
Кейс 5.
1) Реализуйте функцию проверки пароля на соответствие заданным требованиям. Функция принимает 2 аргумента: адрес почты и пароль. Используйте язык программирования, которым владеете лучше всего.

- Пароль должен содержать не менее 8 символов;
- Пароль должен содержать хотя бы одну заглавную букву;
- Пароль должен содержать хотя бы одну строчную букву;
- Пароль должен содержать хотя бы одну цифру;
- Пароль должен содержать хотя бы один специальный символ из перечисленных: !, @, #, $;
- Пароль не должен содержать подстроку, совпадающую с частью имени пользователя. Например, если логин пользователя "johndoe@gmail.com", то пароль "johndoe123" недопустим;

2) Реализуйте автоматизированный тест для функции, разработанной в первом пункте.

BONUS: если вы обладаете навыками автоматизации можете выполнить Кейс 4 частично в виде авто-тестов.

# Выполнение задания:

Примененные мною методы при выполнении тестового задания:

Для разработки тест-кейсов использованы методы "черного ящика", функционального тестирование, UX тестирование. 

Использованы техники тест дизайна : диаграмма состояний и переходов, граничные значения.

Разработка проекта автотестирования выполнена по паттерну PageObject. 

Для разработки автотестов применялись библиотеки pytest, pytest-selenium. Использовались фикстуры, фикстуры параметризации, явные и неявные ожидания драйвером, различные способы описания локаторов (XPATH, CLASS_NAME). 

Проект разработан для операционной системы macOS и ей подобных.

Для установки виртуального окружения в терминале вызвать команду: pip install -r /requirements.txt

## Структура проекта:

### Основная директория "flame" содержит:
README.md - содержит информацию о тестовом задании и проекте.

Flame.xlsx - выполенные кейсы тестового задания (Кейсы 1-4).

requirements.txt - файл с описанием тестового окружения (установить: pip install -r /requirements.txt ).

### В корневом каталоге проекта содержатся:

Директория app:
password.py - функция проверки пароля (Кейс 5. п.1).

Директория driver:
chromedriver.exe -Драйвер для управления браузером Chrome.

Директория pages:
auth_page.py - описание атрибутов и методов работы со страницей авторизации проекта.

base_page.py - описание атрибутов и методов работы с базовой страницей.

config.py - описание значений элементов страниц и переменных.

locators.py - описание локаторов проекта.

Директория tests:
conftest.py - описание фикстур для проекта.

pytest.ini - файл конфигурации Pytest.

test_password.py - тесты на функцию проверки пароля (Кейс 5. п.2).

test_auth_page.py - тесты страницы авторизации проекта (BONUS).

# Запуск тестов производится из терминала следующими командами:
1. Тесты по разработанной функции по проверке пароля password.py: python3 -m pytest -v tests/test_password.py
2. Для BONUS тестов страницы авторизации с ипользованием Selenium: python3 -m pytest -v --driver Chrome --driver-path /driver/chromedriver tests/test_auth_page.py

Тесты страницы авторизации с ипользованием Selenium запускаются в отображаемом графическом режиме chromedriver. 

Для включения драйвера в фоновом режиме, в файле conftest.py расскоментировать параметр опций драйвера ("--headless")
