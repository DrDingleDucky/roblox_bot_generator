from selenium import webdriver
import os

PATH = os.path.join("driver", "msedgedriver.exe")

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Edge(executable_path=PATH, options=options)

driver.get("https://roblox.com")
