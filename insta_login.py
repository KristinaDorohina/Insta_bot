
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from auth_data import username, password, username_kris, password_kris, username_beauty, password_beauty
import time
import random



def hashtag_search(username, password, hashtag):
    browser = webdriver.Chrome()

    try:
        browser.get('https://www.instagram.com/')
        time.sleep(random.randrange(3, 5))

        username_input = browser.find_element('name', 'username')
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(2)

        password_input = browser.find_element('name', 'password')
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(10)

        try:
            browser.get(f'https://www.instagram.com/explore/search/keyword/?q=%23{hashtag}')
            time.sleep(5)

            # for i in range(1, 3):
            #     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            #     time.sleep(random.randrange(3,5))

            hrefs = browser.find_elements('tag name', 'a')
            posts_urls = [item.get_attribute('href') for item in hrefs if '/p/' in item.get_attribute("href")]
            for url in posts_urls:
                browser.get(url)
                like_button = browser.find_element(By.XPATH, "//span[@class='xp7jhwk']/div[@class='x1ypdohk']/div[@class='x1i10hfl x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x6s0dn4 xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x1ypdohk x78zum5 xl56j7k x1y1aw1k x1sxyh0 xwib8y2 xurb0ha xcdnw81']") #   /svg[@class='x1lliihq x1n2onr6 xyb1xck']")
                #"//span[@class='xp7jhwk']/div[@class='x1ypdohk']/div[@class='x1i10hfl x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x6s0dn4 xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x1ypdohk x78zum5 xl56j7k x1y1aw1k x1sxyh0 xwib8y2 xurb0ha xcdnw81']")
                like_button.click()
                #like_button.send_keys(Keys.ENTER)


                time.sleep(random.randrange(8,10))

            browser.close()
            browser.quit()

        except Exception as ex:
            print(ex)
            browser.close()
            browser.quit()

    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()

hashtag_search(username_beauty, password_beauty, 'кафеминск')
