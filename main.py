from selenium import webdriver
from getpass import getpass
import time
import urllib.request as urllib
import os
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = False
webdriver_path = "./geckodriver"
download_url = "media?size=l"
def next_picture(): 
    nex = browser.find_element_by_class_name("_65Bje") 
    return nex
def progressBar(iterable, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    total = len(iterable)

    def printProgressBar (iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Initial Call
    printProgressBar(0)
    # Update Progress Bar
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    # Print New Line on Complete
    print("\nDone") 
    browser.quit()  

username = input("Username: ")
password= getpass()
profile = input("Profile: ")
count = input("Number of Pictures(from last): ")
browser = webdriver.Firefox(options=options, executable_path=webdriver_path)
browser.get("https://www.instagram.com/{}".format(profile))
print("Page Loading...")
time.sleep(5)

pic = browser.find_element_by_class_name("_9AhH0")    
pic.click() 
time.sleep(5)

user = browser.find_element_by_name("username")
passw = browser.find_element_by_name("password")

user.send_keys(username)
passw.send_keys(password)

login = browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/div[2]/div/div/div[1]/div/form/div[1]/div[3]")
login.click()
time.sleep(5)
print("Login...")

notNow = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
notNow.click()
time.sleep(3)
print("Downloading...")

pic = browser.find_element_by_class_name("_9AhH0")    
pic.click() 

i=0
items = list(range(0, int(count)))
profile_path = os.path.join("./", profile)  
os.mkdir(profile_path) 
for item in progressBar(items, prefix = 'Progress:', suffix = 'Complete', length = int(count)-1):
    post =browser.current_url + download_url
    work_path=os.path.join(profile_path,'{}.jpg'.format(i))
    urllib.urlretrieve(post,work_path)
    i+=1
    next_picture().click()
    time.sleep(0.1)