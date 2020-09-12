from selenium import webdriver
from getpass import getpass
import time

username = input("Username: ")
password= getpass()
url = input("URL: ")
browser = webdriver.Firefox(executable_path='/home/caner/geckodriver')
browser.get(url)
time.sleep(5)

user = browser.find_element_by_name("username")
passw = browser.find_element_by_name("password")

user.send_keys(username)
passw.send_keys(password)
login = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[3]/button/div")
login.click()
time.sleep(5)
notNow = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
notNow.click()

SCROLL_PAUSE_TIME = 1

last_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(SCROLL_PAUSE_TIME)

    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

posts = []
links = browser.find_elements_by_tag_name('a')

for link in links:
    post = link.get_attribute('href')
    if '/p/' in posts:
        posts.append(post)


        