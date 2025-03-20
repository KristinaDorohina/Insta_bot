# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium_stealth import stealth
#
# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# #options.add_argument("--headless")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# driver = webdriver.Chrome(options=options)
#
# stealth(driver,
#         languages=["en-US", "en"],
#         vendor="Google Inc.",
#         platform="Win32",
#         webgl_vendor="Intel Inc.",
#         renderer="Intel Iris OpenGL Engine",
#         fix_hairline=True,
#         )
#
# with webdriver.Chrome(options=options) as driver:
#         driver.get('https://visa.vfsglobal.com/blr/ru/pol/login')
#         time.sleep(600)
#         try:
#                 driver.find_element(By.ID, 'username').send_keys('kristina.kozhemiakina@gmail.com')
#                 time.sleep(4)
#                 driver.find_element(By.ID, 'password').send_keys('Rhbcnbyf0410$')
#                 time.sleep(3)
#                 driver.find_element(By.XPATH,'//span[@class="mat-button-wrapper"]').click()
#                 time.sleep(2)
#         except:
#                 driver.implicitly_wait(60)




