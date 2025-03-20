
# ОТКРЫВАЕМ ХРОМ С РАСШИРЕНИЕМ

# import time
# from selenium import webdriver
#
# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_extension('coordinates.crx')
#
# with webdriver.Chrome(options=options_chrome) as browser:
#     url = 'https://stepik.org/course/104774'
#     browser.get(url)
#     time.sleep(15)


#ОТКРЫВАЕМ ХРОМ В ФОНОВОМ РЕЖИМЕ
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# # Создание объекта ChromeOptions для дополнительных настроек браузера
# options_chrome = webdriver.ChromeOptions()
#
# # Добавление аргумента '--headless' для запуска браузера в фоновом режиме
# options_chrome.add_argument('--headless')
#
# # Инициализация драйвера Chrome с указанными опциями
# # Использование менеджера контекста 'with' для автоматического закрытия браузера после выполнения кода
# with webdriver.Chrome(options=options_chrome) as browser:
#     url = 'https://stepik.org/course/104774'
#     browser.get(url)
#
#     # Ищем элемент по тегу 'a' (ссылку)
#     a = browser.find_element(By.TAG_NAME, 'a')
#
#     # Выводим атрибут 'href' найденного элемента (URL ссылки)
#     print(a.get_attribute('href'))



# ДОБАВЛЕНИЯ ПРОФИЛЯ В ХРОМ
# import time
# from selenium import webdriver
#
# # Задаем опции для Chrome
# options_chrome = webdriver.ChromeOptions()
# # Указываем путь к профилю пользователя
# options_chrome.add_argument('user-data-dir=C:\\Users\\krist\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1')
#
# # Инициализируем драйвер с указанными опциями
# with webdriver.Chrome(options=options_chrome) as browser:
#     url = 'https://yandex.ru/'
#     browser.get(url)  # Открываем страницу
#     time.sleep(10)  # Даем время на загрузку страницы
#

# ОПРЕДЕЛИТЬ СВОЙ ПРОКСИ
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# url = 'https://2ip.ru/'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     time.sleep(5)
#     print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
#     time.sleep(5)


#ОТКРЫТЬ САЙТ С ПРОКСИ
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# proxy_list = ['8.210.83.33:80', '199.60.103.28:80',
# '103.151.246.38:10001', '199.60.103.228:80',
# '199.60.103.228:80', '199.60.103.28:80', ]
#
# for PROXY in proxy_list:
#     try:
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument('--proxy-server=%s' % PROXY)
#         url = 'https://2ip.ru/'
#
#         with webdriver.Chrome(options=chrome_options) as browser:
#             browser.get(url)
#             print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
#
#             browser.set_page_load_timeout(5)
#
#             proxy_list.remove(PROXY)
#     except Exception as _ex:
#         print(f"Превышен timeout ожидания для - {PROXY}")
#         continue
#
# import time
# from selenium.webdriver.common.by import By
# from selenium-wire import webdriver
#
# options = {'proxy': {
#     'http': "socks5://D2Frs6:75JjrW@194.28.210.39:9867",
#     'https': "socks5://D2Frs6:75JjrW@194.28.210.39:9867",
#     }}
#
# url = 'https://2ip.ru/'
#
# with webdriver.Chrome(seleniumwire_options=options) as browser:
#     browser.get(url)
#     print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
#     time.sleep(5)


#COOKIES
# import time
# from pprint import pprint
# from selenium import webdriver
#
# cookie_dict = {
#     'name': 'any_name_cookie',    # Любое имя для cookie
#     'value': 'any_value_cookie',  # Любое значение для cookie
#     'expiry': 2_000_000_000,      # Время жизни cookie в секундах
#     'path': '/',                  # Директория на сервере дял которой будут доступны cookie
#     'domain': 'parsinger.ru',     # Информация о домене и поддомене для которых доступны cookie
#     'secure': True,  # or False   # Сигнал браузера о том что передать cookie только по защищённому HTTPS
#     'httpOnly': True,  # or False # Ограничивает достук к cookie по средствам API
#     'sameSite': 'Strict',  # or lax or none # Ограничение на передачу cookie между сайтами
# }
#
# with webdriver.Chrome() as webdriver:
#     webdriver.get('https://parsinger.ru/methods/4/index.html')
#     webdriver.add_cookie(cookie_dict)
#     pprint(webdriver.get_cookies())
#     time.sleep(100)

import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get(r"https://parsinger.ru/selenium/5.7/3/index.html")

    list_input = []      # Инициализируем пустой список для хранения обработанных элементов ввода
    while True:          # Начинаем бесконечный цикл

        # Ищем все элементы input на веб-странице и добавляем их в список input_tags
        input_tags = [x for x in browser.find_elements(By.TAG_NAME, 'input')]

        # Обходим каждый элемент input в списке
        for tag_input in input_tags:
            # Проверяем, не обрабатывали ли мы уже этот элемент ранее
            if tag_input not in list_input:
                tag_input.send_keys(Keys.DOWN)     # Отправляем клавишу "Вниз"
                browser.execute_script("return arguments[0].scrollIntoView(true);", tag_input)
                tag_input.click()                  # Кликаем на элемент
                time.sleep(.3)
                list_input.append(tag_input)       # Добавляем элемент в список обработанных элементов






