import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

PATH = os.path.join("driver", "chromedriver.exe")

options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=C:\\Users\\gd240\\AppData\\Local\\Google\\Chrome\\User Data\\")
options.add_argument("--disable-blink-features=AutomationControlled")


service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.roblox.com/")
