import os
import random
import secrets
import string
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def random_month():
    return random.choice(["J", "F", "M", "A", "MM", "JJ", "JJJ", "AA", "S", "O", "N", "D"])


def random_day():
    return random.choice(["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"])


def random_year():
    return random.choice(["2000", "2001", "2002", "2003", "2004", "2005"])


def random_username():
    return "".join(random.choice(string.digits + string.ascii_letters) for _ in range(20))


def random_password():
    return secrets.token_urlsafe(26)


def random_gender():
    return random.choice(["FemaleButton", "MaleButton"])


def credentials_validation(driver):
    try:
        if driver.find_element(By.XPATH, '//*[@id="signup-BirthdayInputValidation"]').text == "Invalid birthday.":
            print("error: invalid birthday")
            return False
        else:
            pass
    except:
        pass

    try:
        if driver.find_element(By.XPATH, '//p[@id="signup-usernameInputValidation"]').text == "This username is already in use.":
            print("error: this username is already in use")
            return False
        else:
            pass
    except:
        pass

    try:
        if driver.find_element(By.XPATH, '//p[@id="signup-usernameInputValidation"]').text == "Username not appropriate for Roblox.":
            print("error: username not appropriate for roblox")
            return False
        else:
            pass
    except:
        pass

    try:
        if driver.find_element(By.XPATH, '//p[@id="signup-usernameInputValidation"]').text == "Username might contain private information.":
            print("error: username might contain private information")
            return False
        else:
            pass
    except:
        pass

    return True


def error_validation(driver):
    try:
        if driver.find_element(By.XPATH, '//*[@id="GeneralErrorText"]').text == "Sorry! An unknown error occurred. Please try again later.":
            print("error: An unknown error occurred")
            return False
        else:
            return True
    except:
        return True


def number_validation(number):
    try:
        int(number)
        return False
    except:
        return True


def file_validation(file_name):
    if not file_name.endswith(".txt"):
        print("error: file name dosent end in '.txt'")
        return False
    elif any(char in file_name for char in ["/", "\\", "?", "%", "*", ":", "|", "\"", "<", ">"]):
        print("error: file name contains forbidden characters")
        return False
    elif os.path.exists(os.path.join("account_pools", file_name)):
        print("error: file already exists")
        return False
    else:
        return True


def file_search(file_name):
    for file in os.listdir(os.path.join("account_pools")):
        if file == file_name:
            return True

    return False


def sign_up(driver):
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


def log_in(driver, username, password):
    username_element = driver.find_element(
        By.XPATH, '//*[@id="login-username"]')
    username_element.click()
    username_element.send_keys(username)

    password_element = driver.find_element(
        By.XPATH, '//*[@id="login-password"]')
    password_element.click()
    password_element.send_keys(password)

    log_in_element = driver.find_element(
        By.XPATH, '//*[@id="cross-device-login-button"]')
    log_in_element.click()


def main():
    while True:
        command = input("type 'help' for commands: -> ").lower()

        if command[0:3] == "new":
            parameters = [string for string in command.split(
                " ") if string != ""]

            if len(parameters) != 2:
                print("error: invalid parameters")
            else:
                file_name = parameters[1]

                if file_validation(file_name):
                    open(os.path.join("account_pools", file_name), "w").close()

        elif command[0:3] == "gen":
            parameters = [string for string in command.split(
                " ") if string != ""]

            if len(parameters) != 3:
                print("error: invalid parameters.")
            else:
                number_of_accounts = parameters[1]
                file_name = parameters[2]

                if number_validation(number_of_accounts):
                    print("error: invalid number of accounts")
                elif not file_search(file_name):
                    print("error: file not found")
                else:
                    print("-----------------------------")

                    for _ in range(int(number_of_accounts)):
                        PATH = os.path.join("driver", "chromedriver.exe")

                        options = Options()
                        options.add_argument("log-level=3")
                        options.add_experimental_option("detach", True)
                        options.add_argument(
                            "--disable-blink-features=AutomationControlled")

                        service = Service(executable_path=PATH)
                        driver = webdriver.Chrome(
                            service=service, options=options)

                        driver.get("https://roblox.com")
                        driver.implicitly_wait(5)

                        while True:
                            account_info = sign_up(driver)

                            time.sleep(0.8)

                            if credentials_validation(driver):
                                break

                        time.sleep(0.8)

                        sign_up_element = driver.find_element(
                            By.XPATH, '//*[@id="signup-button"]')
                        sign_up_element.click()

                        time.sleep(0.8)

                        if not error_validation(driver):
                            break

                        while driver.current_url != "https://www.roblox.com/home?nu=true":
                            time.sleep(1)

                        with open(os.path.join("account_pools", file_name), "a") as accounts:
                            accounts.write(f"{account_info}\n")

                        print("account created")
                        print(account_info)
                        print("-----------------------------")

                        driver.quit()

        elif command[0:5] == "lanch":
            parameters = [string for string in command.split(
                " ") if string != ""]

            if len(parameters) != 2:
                print("error: unknow pramaters")
            else:
                file_name = parameters[1]

                if not file_search(file_name):
                    print("error: file not found")
                else:
                    with open(os.path.join("account_pools", file_name), "r") as file:
                        lines = file.readlines()

                    for line in lines:
                        PATH = os.path.join(
                            "driver", "chromedriver.exe")

                        options = Options()
                        options.add_argument("log-level=3")
                        options.add_experimental_option("detach", True)
                        options.add_argument(
                            "--disable-blink-features=AutomationControlled")

                        service = Service(executable_path=PATH)
                        driver = webdriver.Chrome(
                            service=service, options=options)

                        driver.get("https://www.roblox.com/login")
                        driver.implicitly_wait(5)

                        log_in(driver, line[6:26], line[39:])

        elif command == "help":
            print("'new file.txt' - create a new file to store accounts")
            print("'gen 1 file.txt' - generate accounts and store them in a file")
            print("'lanch file.txt' - lanch all accounts in a fileg")
            print("'quit' - quit the program")

        elif command == "quit":
            print("quitting program")
            break

        else:
            print(f"'{command}' is not recognized")


if __name__ == "__main__":
    main()
