from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import requests
import time
from datetime import datetime
import pytz

def currenttime():
    tz_IN = pytz.timezone('Asia/Kolkata') 
    datetime_In = datetime.now(tz_IN)
    current = datetime_In.strftime("%I:%M:%S")
    return current

def log(logtext):
    f = open("out.txt", "a+")
    print(f"\n{currenttime()} : {logtext}\n")
    f.write(f"\n{currenttime()} : {logtext}\n")
    f.close()

def start():
    while True:
        try:
            response = requests.get(URL)
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
            log("Browser started")
            driver.get(URL)
            content = driver.page_source
            log("Content Fetched")
            log(f"Response code {response.status_code}")
            log(f"Response time {response.elapsed}")
            soup = BeautifulSoup(content,features="lxml")
            for element in soup.findAll(attrs={searchtype: NAME}):
                log("Searching for the given string in results")
                if STRING in element:
                    log(element)
                    log("Found")
            log("Search completed")                              
            driver.close()
            log("Initializing script again in 5 mins")
            time.sleep(300)
        except:
               time.sleep(15)
               log("Script failed restarting now!")
               start()



#STRING = """Multi
#                 lined string"""
STRING = "Enter your string here!" # Comment this line and user line 51, 52 for multi-lined string
URL = input("Enter the URL to be searched : ")
MODE = input("String should be searched in Class or ID? 1 - Class, 2- ID : ")
NAME = input("Enter the class or ID name : ")
if (MODE == "1"):
    searchtype = "class"
elif(MODE =="2"):
    searchtype = "ID"
else:
    exit(log("Invalid Options"))
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-browser-side-navigation')
print("\nFull script has been initialized\n")
start() 
