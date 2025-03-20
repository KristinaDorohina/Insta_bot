import os.path
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from auth_data import *
import time
import random
import requests


class InstaBot():

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome()

    def close_browser(self):
        self.browser.close()
        self.browser.quit()

    def login(self):
        browser = self.browser
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

    def like_foto_by_hashtag(self, hashtag):
        browser = self.browser
        browser.get(f'https://www.instagram.com/explore/search/keyword/?q=%23{hashtag}')
        time.sleep(5)

        #for i in range(1, 4):
        #    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #    time.sleep(random.randrange(3, 5))

        hrefs = browser.find_elements('tag name', 'a')
        posts_urls = [item.get_attribute('href') for item in hrefs if '/p/' in item.get_attribute("href")]
        print(len(posts_urls))
        for url in posts_urls[:18]:
            try:
                browser.get(url)
                time.sleep(3)
                # browser.find_element(By.XPATH, "//svg[@aria-label='Нравится']").click()
                # time.sleep(3)
                browser.find_element(By.XPATH, "//div[@class='x1ypdohk']").click()
                time.sleep(3)
                browser.find_element(By.XPATH, "//div[@class='x1i10hfl x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x6s0dn4 xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x1ypdohk x78zum5 xl56j7k x1y1aw1k x1sxyh0 xwib8y2 xurb0ha xcdnw81']").click()
                time.sleep(5)
                #time.sleep(random.randrange(80,100))
            except Exception as ex:
                print(ex)
                self.close_browser()

    def xpath_exist(self, url):
        browser = self.browser
        try:
            browser.find_element(By.XPATH, url)
            exist = True
        except NoSuchElementException:
            exist = False
        return exist


    def put_exactly_likes(self, userpost):
        browser = self.browser
        browser.get(userpost)
        time.sleep(2)

        wrong_userpage = "/html/body/div[1]/section/mean/div/h"
        if self.xpath_exist(wrong_userpage):
            print('Такой страницы не существует')
            self.close_browser()
        else:
            print('Пост найден. Ставим лайк!')
            time.sleep(3)

            browser.find_element(By.XPATH, "//div[@class='x1ypdohk']").click()
            time.sleep(random.randrange(1, 3))
            browser.find_element(By.XPATH,
                                 "//div[@class='x1i10hfl x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x6s0dn4 xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x1ypdohk x78zum5 xl56j7k x1y1aw1k x1sxyh0 xwib8y2 xurb0ha xcdnw81']").click()

            print(f'Лайк на пост: {userpost} поставлен!')
            time.sleep(random.randrange(50, 80))
            self.close_browser()

    def get_all_posts_url(self, userpage):

        browser = self.browser
        browser.get(userpage)
        time.sleep(4)

        wrong_userpage = "/html/body/div[1]/section/mean/div/h"
        if self.xpath_exist(wrong_userpage):
            print('Такого пользователя не существует')
            self.close_browser()
        else:
            print('Пользователь найден. Ставим лайк!')
            time.sleep(3)

            posts_count = int(browser.find_element(By.XPATH,
                                                   "//span[@class='html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs']").text)
            loops_count = int(posts_count / 12)
            print(loops_count)

            posts_urls = []
            for i in range(0, loops_count):
                hrefs = browser.find_elements(By.TAG_NAME, 'a')
                hrefs = [item.get_attribute('href') for item in hrefs if '/p' in item.get_attribute('href')]
                for href in hrefs:
                    posts_urls.append(href)

                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(7)

            file_name = userpage.split('/')[-2]

            with open(f'{file_name}.txt', 'a', encoding='utf-8') as file:
                for posts_url in posts_urls:
                    file.write(posts_url + '\n')

            with open(f'{file_name}.txt', 'a', encoding='utf-8') as file:
                for posts_url in posts_urls:
                    file.write(posts_url + '\n')

            set_posts_urls = set(posts_urls)
            set_posts_urls = list(set_posts_urls)

            with open(f'{file_name}_set.txt', 'a', encoding='utf-8-sig') as file:
                for post_url in set_posts_urls:
                    file.write(post_url + '\n')



    def put_many_likes(self, userpage):
        browser = self.browser
        self.get_all_posts_url(userpage)
        file_name = userpage.split('/')[-2]
        time.sleep(4)
        browser.get(userpage)
        time.sleep(4)


        with open(f'{file_name}_set.txt', 'r', encoding='utf-8') as file:
            urls_list = file.readlines()

            for post_url in urls_list[1:7]:
                try:
                    browser.get(post_url)
                    time.sleep(random.randrange(4, 8))
                    browser.find_element(By.XPATH, "//div[@class='x1ypdohk']").click()
                    time.sleep(random.randrange(1,3))
                    browser.find_element(By.XPATH,
                                         "//div[@class='x1i10hfl x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x6s0dn4 xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x1ypdohk x78zum5 xl56j7k x1y1aw1k x1sxyh0 xwib8y2 xurb0ha xcdnw81']").click()
                    time.sleep(random.randrange(80,100))

                except Exception as ex:
                    print(ex)
                    self.close_browser()

        self.close_browser()

    def download_content_userpage(self, userpage):
        browser = self.browser
        self.get_all_posts_url(userpage)
        file_name = userpage.split('/')[-2]
        time.sleep(4)
        browser.get(userpage)
        time.sleep(4)

        if os.path.exists(f'{file_name}'):
            print('Папка уже существует')
        else:
            os.mkdir(file_name)

        src_img_video_url = []

        with open(f'{file_name}_set.txt', 'r', encoding='utf-8') as file:
            urls_list = file.readlines()

            for post_url in urls_list[1:7]:
                try:
                    browser.get(post_url)
                    time.sleep(random.randrange(4, 8))

                    img_src = '/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[1]/div/div/div/div[1]/img'
                    video_src = '/html/body/div[5]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[1]/div/div/div/div/div/div/div/video'
                    post_id = post_url.split('/')[-2]
                    if self.xpath_exist(img_src):
                        img_src_url = browser.find_element(By.XPATH, img_src).get_attribute('src')
                        src_img_video_url.append(img_src_url)

                        get_req = requests.get(img_src_url)
                        with open(f'{file_name}/{file_name}_{post_id}_img.png', 'wb', encoding='utf-8') as img_file:
                            img_file.write(get_req.content)


                    elif self.xpath_exist(video_src):
                        vid_src_url = browser.find_element(By.XPATH, video_src).get_attribute('src')
                        src_img_video_url.append(vid_src_url)

                        get_vid = requests.get(vid_src_url, stream=True)
                        with open(f'{file_name}/{file_name}_{post_id}_vid.mp4', 'wb', encoding='utf-8') as vid_file:
                            for chunk in get_vid.iter_content(chunk_size = 1024 * 1024):
                                if chunk:
                                    vid_file.write(chunk)

                    else:
                        print("Oooops!")
                        src_img_video_url.append(f'Пост {post_url} нет ссылки')

                except Exception as ex:
                    print(ex)
                    self.close_browser()

        self.close_browser()
        with open(f'{file_name}/{file_name}_src_img_video_url.txt', 'a', encoding='utf-8') as file:
            for i in src_img_video_url:
                file.write(i + '\n')

    def get_all_follows(self,userpage):
        browser = self.browser
        browser.get(userpage)
        time.sleep(4)
        file_name = userpage.split('/')[-2]
        if os.path.exists(f'{file_name}'):
            print(f'Папка {file_name} уже существует')
        else:
            print(f'Создаем папку пользователя {file_name}')
            os.mkdir(file_name)

        wrong_userpage = "/html/body/div[1]/section/mean/div/h"
        if self.xpath_exist(wrong_userpage):
            print(f'Такого пользователя {file_name} не существует')
            self.close_browser()
        else:
            print(f'Пользователь {file_name} найден. Скачиваем подписчиков')
            time.sleep(3)

            follows_btn = browser.find_element(By.XPATH,
                                                   "//span[@class='html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs']")
            follows_btn_text = follows_btn.text
            followers_count = int(follows_btn_text.split(' ')[0])
            print(f'Количество подписчиков {followers_count}')
            time.sleep(2)

            loops_count = int(followers_count/12)
            print(f'Количество итераций: {loops_count}')
            time.sleep(4)
            
            follows_btn.click()


my_bot = InstaBot(username, password)
my_bot.login()
#my_bot.get_all_follows('https://www.instagram.com/kris.dorohina/?next=%2F')
my_bot.like_foto_by_hashtag('cafeminsk')