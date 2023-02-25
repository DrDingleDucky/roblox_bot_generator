import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

PATH = os.path.join("driver", "chromedriver.exe")

options = Options()
options.add_experimental_option("detach", True)

service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://roblox.com")
