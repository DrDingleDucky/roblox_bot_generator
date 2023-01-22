import os
import random
import secrets
import string
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# The location of your driver.
PATH = os.path.join("Driver", "chromedriver.exe")

options = Options()
options.add_argument("log-level=3")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("detach", True)
# options.add_extension(os.path.join("Solver", "ext.crx"))

service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://roblox.com")  # Gets the website.
driver.implicitly_wait(5)  # Waiting for the website to fully load.


def random_month():
    return random.choice(["J", "F", "M", "A", "MM", "JJ", "JJJ", "AA", "S", "O", "N", "D"])


def random_day():
    return random.choice(["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"])


def random_year():
    return random.choice(["2000", "2001", "2002", "2003", "2004", "2005"])


def random_username():
    return "".join(random.choice(string.digits + string.ascii_letters) for _ in range(20))


def random_password():
    return secrets.token_urlsafe(26)


def random_gender():
    return random.choice(["FemaleButton", "MaleButton"])


def validation_checker():
    try:
        sign_up = driver.find_element(
            By.XPATH, '//*[@id="signup-button"]')
        sign_up.click()

        return True
    except:
        return False
    # try:
    #     if driver.find_element(By.XPATH, "//p[@id='signup-usernameInputValidation']").text == "This username is already in use.":
    #         print("This username is already in use.")
    #         return False
    #     else:
    #         pass
    # except:
    #     pass

    # try:
    #     if driver.find_element(By.XPATH, "//p[@id='signup-usernameInputValidation']").text == "Username not appropriate for Roblox.":
    #         print("Username not appropriate for Roblox.")
    #         return False
    #     else:
    #         pass
    # except:
    #     pass

    # try:
    #     if driver.find_element(By.XPATH, "//p[@id='signup-usernameInputValidation']").text == "Username might contain private information.":
    #         print("Username might contain private information.")
    #         return False
    #     else:
    #         pass
    # except:
    #     pass

    # return True


def fill_info():
    month_element = driver.find_element(
        By.XPATH, "//select[@id='MonthDropdown']")
    month_element.click()
    month = random_month()
    month_element.send_keys(month)

    day_element = driver.find_element(
        By.XPATH, "//select[@id='DayDropdown']")
    day_element.click()
    day = random_day()
    day_element.send_keys(day)

    year_element = driver.find_element(
        By.XPATH, "//select[@id='YearDropdown']")
    year_element.click()
    year = random_year()
    year_element.send_keys(year)

    username_element = driver.find_element(
        By.XPATH, "//input[@id='signup-username']")
    username_element.clear()
    username_element.click()
    username = random_username()
    username_element.send_keys(username)

    password_element = driver.find_element(
        By.XPATH, "//input[@id='signup-password']")
    password_element.clear()
    password_element.click()
    password = random_password()
    password_element.send_keys(password)

    gender = driver.find_element(
        By.XPATH, f"//*[@id='{random_gender()}']")
    gender.click()


def main_loop():
    while True:
        fill_info()

        time.sleep(0.5)

        if validation_checker():
            print("Good Credentials")
            break
        else:
            print("Bad Credentials")

    time.sleep(0.5)

    try:
        if driver.find_element(By.XPATH, '//*[@id="GeneralErrorText"]').text == "Sorry! An unknown error occurred. Please try again later.":
            print("FUCK! The IP address you are using has been flagged. This error will go away after about 45 minutes. You can use proxies to bypass this error.")
        else:
            print("Successful")
    except:
        print("Successful")


def main():
    main_loop()


if __name__ == "__main__":
    main()
