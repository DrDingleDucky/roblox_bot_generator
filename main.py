import os
import random
import re
import secrets
import string
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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


def credentials_validation_checker(driver):
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


def sign_up(driver):
    try:
        sign_up = driver.find_element(
            By.XPATH, '//*[@id="signup-button"]')
        sign_up.click()

        return True
    except:
        return False


def error_validation_checker(driver):
    try:
        if driver.find_element(By.XPATH, '//*[@id="GeneralErrorText"]').text == "Sorry! An unknown error occurred. Please try again later.":
            print("FUCK! The IP address you are using has been flagged. This error will go away after about 45 minutes. You can use proxies to bypass this error.")
            return False
        else:
            return True
    except:
        return True


def add_friend(driver, friend_request):
    search_element = driver.find_element(
        By.XPATH, '//*[@id="navbar-search-input"]')
    search_element.click()
    search_element.send_keys(friend_request)
    search_element.send_keys(Keys.ARROW_DOWN)
    search_element.send_keys(Keys.ENTER)

    try:
        add_friend = driver.find_element(
            By.XPATH, '/html/body/div[3]/main/div[2]/div[2]/div/div/div/ul/li/div/ng-include/div[1]/button')
        add_friend.click()

        print("Friend Request Sent")
    except:
        print("Unknown Friend")


def fill_info(driver):
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

    return f"Name: {username} | Password: {password}"


def main():
    while True:
        command = input("> ").lower()

        if command == "new":
            file_name = input("File Name > ")

            if len(file_name) > 5 and file_name[-4:] == ".txt" and not bool(re.search(r"\s", file_name)):
                open(os.path.join("account_pools", file_name), "w+")
            else:
                print("Bad File Name example: file_name.txt")

        elif command == "list":
            print(os.listdir(os.path.join("account_pools")))

        elif command == "add":
            if len(os.listdir(os.path.join("account_pools"))) <= 0:
                print("There must be at least one account pool to add to.")
            else:
                number_of_accounts = input("Number Of Accounts > ")

                try:
                    number_of_accounts = int(number_of_accounts)

                    friend_request = input("Friend Request > ")
                    file_name = input("Name Of File > ")

                    for file in os.listdir(os.path.join("account_pools")):
                        if file != file_name:
                            print("File Not Found")
                        else:
                            for _ in range(number_of_accounts):
                                # The location of your driver.
                                PATH = os.path.join(
                                    "driver", "chromedriver.exe")

                                options = Options()
                                options.add_argument("log-level=3")
                                options.add_experimental_option(
                                    'excludeSwitches', ['enable-logging'])
                                options.add_experimental_option("detach", True)
                                options.add_argument("--incognito")

                                service = Service(executable_path=PATH)
                                driver = webdriver.Chrome(
                                    service=service, options=options)

                                # Gets the website.
                                driver.get("https://roblox.com")
                                # The maximum amount of time selenium will wait for an element to load.
                                driver.implicitly_wait(3)

                                while True:
                                    account_info = fill_info(driver)

                                    time.sleep(0.5)

                                    if credentials_validation_checker(driver):
                                        print("Good Credentials")
                                        break
                                    else:
                                        print("Bad Credentials, Retrying...")

                                time.sleep(0.5)

                                sign_up(driver)

                                time.sleep(0.5)

                                if error_validation_checker(driver):
                                    print(
                                        "SUCCESSFUL, There was no unknown error")

                                    print("Verifying...")

                                    while driver.current_url != "https://www.roblox.com/home?nu=true":
                                        time.sleep(0.1)

                                    print("Account Created")

                                    with open(os.path.join("account_pools", file_name), "a") as accounts:
                                        accounts.write(f"{account_info}\n")

                                    if friend_request != "" and not bool(re.search(r"\s", friend_request)):
                                        add_friend(driver, friend_request)

                                    print(account_info)

                                else:
                                    print(
                                        "There was an unknown error. Retry in 45 minutes.")

                                print("------------------------------")

                                time.sleep(0.5)

                                driver.quit()

                except:
                    print("The number of accounts is invalid.")

        elif command == "help":
            print("""
'new' - create a new account pool
'list' - list all account pools
'add' - add accounts to an account pool
'lanch' - lanch a account pool
'quit' quit the program
""")

        elif command == "quit":
            print("Quitting Program...")
            break

        else:
            print(f"'{command}' is not recognized. Type 'help' to see commands.")

        time.sleep(0.1)

    print("Done")


if __name__ == "__main__":
    main()
