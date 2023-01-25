import os
import re

string = "new file_name.txt"

while True:
    command = input("> ").lower()

    if command == "new":
        file_name = input("File Name > ")
        if len(file_name) > 5 and file_name[-4:] == ".txt" and not bool(re.search(r"\s", file_name)):
            open(os.path.join("account_pools", file_name), "w+")
        else:
            print("Bad Name")
    elif command[0:6] == "create":
        pass
    elif command == "list":
        print("LISTED POOLS")
    elif command == "lanch":
        print("Lanched")
    elif command == "help":
        print("Help")
    elif command == "quit":
        print("Quit")
        break
    else:
        print(f"'{command}' is not recognized. Type 'help' to see commands.")


# import re
# string = "new file_name.txt"

# while True:
#     command = input("> ").lower()

#     if command == "new":
#         if len(command) == 3 or len(command) == 4:
#             print("new file_name.txt")
#         elif bool(re.search(r"\s", command[4:])):
#             print("File name can't contain spaces")
#         elif command[-4:] != ".txt":
#             print('File must end with ".txt"')
#         else:
#             print(f'NEW FILE CREATED "{command[4:]}"')
#     elif command[0:6] == "create":
#         if len(command) == 6 or len(command) == 7:
#             print("create number_of_bots file_name.txt")
#         elif command[7] != "1":
#             print("bad number (1 - 9")
#         elif bool(re.search(r"\s", command[8:])):
#             print("File name can't contain spaces")
#         elif command[-4:] != ".txt":
#             print('File must end with ".txt"')
#         else:
#             print(f'CREATING {command[7]} ACCOUNTS IN "{command[9:]}"')
#     elif command == "list":
#         print("LISTED POOLS")
#     elif command == "lanch":
#         print("Lanched")
#     elif command == "help":
#         print("Help")
#     elif command == "quit":
#         print("Quit")
#         break
#     else:
#         print(f"'{command}' is not recognized. Type 'help' to see commands.")
