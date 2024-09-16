# import requests
# web_page = requests.get('https://live.skillbox.ru/playlists/code/python/')
# web_page.text
#
# from openpyxl import Workbook
#
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(web_page.text, 'html.parser')
#
# soup.find(class_='playlist-inner-card__link-text').text
# soup.find(class_='playlist-inner-card__link').attrs['href']
# relative_url = soup.find(class_='playlist-inner-card__link').attrs['href']
#
# abs_url = 'https://live.skillbox.ru' + relative_url
#
# abs_url
#
# work_book = Workbook()
# work_sheet = work_book.active
#
# items = soup.find_all(class_='playlist-inner__item')
#
# for elem in items:
#     title = elem.find(class_='playlist-inner-card__link-text').text
#     relative_url = elem.find(class_='playlist-inner-card__link').attrs['href']
#     url = 'https://live.skillbox.ru' + relative_url
#     row = [title, url]
#     print(row)
#     work_sheet.append(row)
#
# work_book.save('Вебинары про Python от Skillbox.xlsx')


from selenium import webdriver as wd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
driver = webdriver.Chrome(options = chrome_options)
driver.get("https://en.wikipedia.org")
driver.find_element(By.ID, "n-randompage").click()
# from bs4 import BeautifulSoup

browser = wd.Chrome()

#

# from bs4 import BeautifulSoup
open_search = browser.driver.find_element("header_search")
open_search.click()

search = browser.find_element("search-modal_input" )
search.send_keys("Git")

# time.sleep(3)
#
# soup = BeautifulSoup(browser.page_source, 'lxml')
# all_publications = \
# soup.find_all('a', {'rel': 'noreferrer noopener'})[1:5]
#  for article all_publications:
# print(article['href'])

