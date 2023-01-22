import os
import random
import secrets
import string
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import user_options

# The location of your driver.
PATH = os.path.join("Driver", "chromedriver.exe")

options = Options()
options.add_argument("log-level=3")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("detach", True)

if user_options.auto_solve_capta:
    options.add_extension(os.path.join("solver", "solver.crx"))

service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://roblox.com")  # Gets the website.
# The maximum amount of time selenium will wait for an element to load.
driver.implicitly_wait(2)


def random_month():
    # return random.choice(["F", "A"])
    return random.choice(["J", "F", "M", "A", "MM", "JJ", "JJJ", "AA", "S", "O", "N", "D"])


def random_day():
    # return random.choice(["30", "31"])
    return random.choice(["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"])


def random_year():
    return random.choice(["2000", "2001", "2002", "2003", "2004", "2005"])


def random_username():
    # return random.choice(["OGlek00AgfmNLyPoJBkc", "mKFuC6E8Hht44LiYVXpO", "0dCl0VBFuQcGgDlbEr8x"])
    return "".join(random.choice(string.digits + string.ascii_letters) for _ in range(20))


def random_password():
    return secrets.token_urlsafe(26)


def random_gender():
    return random.choice(["FemaleButton", "MaleButton"])


def credentials_validation_checker():
    try:
        if driver.find_element(By.XPATH, '//*[@id="signup-BirthdayInputValidation"]').text == "Invalid birthday.":
            print("This username is already in use.")
            return False
        else:
            pass
    except:
        pass

    try:
        if driver.find_element(By.XPATH, '//p[@id="signup-usernameInputValidation"]').text == "This username is already in use.":
            print("This username is already in use.")
            return False
        else:
            pass
    except:
        pass

    try:
        if driver.find_element(By.XPATH, '//p[@id="signup-usernameInputValidation"]').text == "Username not appropriate for Roblox.":
            print("Username not appropriate for Roblox.")
            return False
        else:
            pass
    except:
        pass

    try:
        if driver.find_element(By.XPATH, '//p[@id="signup-usernameInputValidation"]').text == "Username might contain private information.":
            print("Username might contain private information.")
            return False
        else:
            pass
    except:
        pass

    return True


def sign_up():
    try:
        sign_up = driver.find_element(
            By.XPATH, '//*[@id="signup-button"]')
        sign_up.click()

        return True
    except:
        return False


def error_validation_checker():
    try:
        if driver.find_element(By.XPATH, '//*[@id="GeneralErrorText"]').text == "Sorry! An unknown error occurred. Please try again later.":
            print("FUCK! The IP address you are using has been flagged. This error will go away after about 45 minutes. You can use proxies to bypass this error.")
            return False
        else:
            return True
    except:
        return True


def add_friend():
    search_element = driver.find_element(
        By.XPATH, '//*[@id="navbar-search-input"]')
    search_element.click()
    search_element.send_keys(user_options.friend_request)
    search_element.send_keys(Keys.ARROW_DOWN)
    search_element.send_keys(Keys.ENTER)

    try:
        add_friend = driver.find_element(
            By.XPATH, '/html/body/div[3]/main/div[2]/div[2]/div/div/div/ul/li/div/ng-include/div[1]/button')
        add_friend.click()
    except:
        print("Friend Not Found")


def fill_info():
    month_element = driver.find_element(
        By.XPATH, '//select[@id="MonthDropdown"]')
    month_element.click()
    month = random_month()
    month_element.send_keys(month)

    day_element = driver.find_element(
        By.XPATH, '//select[@id="DayDropdown"]')
    day_element.click()
    day = random_day()
    day_element.send_keys(day)

    year_element = driver.find_element(
        By.XPATH, '//select[@id="YearDropdown"]')
    year_element.click()
    year = random_year()
    year_element.send_keys(year)

    username_element = driver.find_element(
        By.XPATH, '//input[@id="signup-username"]')
    username_element.clear()
    username_element.click()
    username = random_username()
    username_element.send_keys(username)

    password_element = driver.find_element(
        By.XPATH, '//input[@id="signup-password"]')
    password_element.clear()
    password_element.click()
    password = random_password()
    password_element.send_keys(password)

    gender = driver.find_element(
        By.XPATH, f'//*[@id="{random_gender()}"]')
    gender.click()

    return f"{username}:{password}\n"


def main():
    for _ in range(user_options.number_of_accounts):
        while True:
            account_info = fill_info()

            time.sleep(0.5)

            if credentials_validation_checker():
                print("Good Credentials")
                break
            else:
                print("Bad Credentials, Retrying...")

        time.sleep(0.5)

        sign_up()

        time.sleep(0.5)

        if error_validation_checker():
            print("SUCCESSFUL, There was no unknown error")
        else:
            print("FUCK, There was an unknown error. Retry in 45 minutes.")
            break

        print("Verifying...")

        while driver.current_url != "https://www.roblox.com/home?nu=true":
            time.sleep(1)

        print("WE'RE IN BITCH, AHHAHAHAHAHAHA")

        with open(os.path.join("accounts", "accounts.txt"), "a") as accounts:
            accounts.write(account_info)

        with open(os.path.join("accounts", "cookies.txt"), "a") as cookies:
            cookies.write(driver.get_cookie(".ROBLOSECURITY")["value"])

        add_friend()

    print("Done")


if __name__ == "__main__":
    main()
