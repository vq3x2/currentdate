import base64
import requests
import os
from colorama import Fore
import time


owner = "vq3x2"
rep = "nova"
date_txt = "date.txt"
ver_txt = "version.txt"

date_url = f"https://api.github.com/repos/{owner}/{rep}/contents/{date_txt}"
ver_url = f"https://api.github.com/repos/{owner}/{rep}/contents/{ver_txt}"

headers = {"Accept": "application/vnd.github.v3+json"}


date_response = requests.get(date_url, headers=headers)
ver_response = requests.get(ver_url, headers=headers)

if date_response.status_code == 200:
    file_content = date_response.json()["content"]

    date_en = base64.b64decode(file_content).decode("utf-8")
else:
    #print(f"Fehler beim Abrufen der Datei. Statuscode: {response.status_code}")
    pass

if ver_response.status_code == 200:
    file_content2 = ver_response.json()["content"]

    ver_en = base64.b64decode(file_content2).decode("utf-8")
else:
    #print(f"Fehler beim Abrufen der Datei. Statuscode: {response.status_code}")
    pass


ver_en = ver_en.strip()

#################################################################################



def ver_exists(ver_path):
    return os.path.isfile(ver_path)

ver_path = "./version./setup.txt"



def code_exists(code_path):
    return os.path.isfile(code_path)

code_path = "./Codes./setup.txt"

if ver_exists(ver_path) and code_exists(code_path):
    #print(f"setup.txt = True")

    setup_banner = f"""
{Fore.YELLOW}[{Fore.YELLOW}1{Fore.YELLOW}] {Fore.RED}Clear Invalid Codes.txt
{Fore.YELLOW}[{Fore.YELLOW}2{Fore.YELLOW}] {Fore.RED}Clear Valid Codes.txt
{Fore.YELLOW}[{Fore.YELLOW}3{Fore.YELLOW}] {Fore.LIGHTRED_EX}Download newest version
{Fore.YELLOW}[{Fore.YELLOW}4{Fore.YELLOW}] {Fore.LIGHTRED_EX}Close Setup"""

    print(setup_banner)
    print()
    setup_menu = True
    while setup_menu != "4":

        setup_menu = input(f"{Fore.YELLOW}Choice: {Fore.RED}")
        if setup_menu == "1":
            print()
            print(f"{Fore.YELLOW}[~] Note: {Fore.LIGHTBLACK_EX}Open Invalid Codes.txt")
            with open("./Codes./Invalid Codes.txt", "w") as clear_invalid:
                time.sleep(0.2)
                print(f"{Fore.YELLOW}[~] Note: {Fore.LIGHTBLACK_EX}Clearing Invalid Codes.txt")
                clear_invalid.write("")
                clear_invalid.close()
                time.sleep(0.3)
                print(f"{Fore.YELLOW}[~] Note: {Fore.GREEN}Sucsessfully cleared Invalid Codes.txt")

                time.sleep(1)
                os.system("cls")
                print(setup_banner)
                print()

        if setup_menu == "2":
            print()
            print(f"{Fore.YELLOW}[~] Note: {Fore.LIGHTBLACK_EX}Open Valid Codes.txt")
            with open("./Codes./Valid Codes.txt", "w") as clear_valid:
                time.sleep(0.2)
                print(f"{Fore.YELLOW}[~] Note: {Fore.LIGHTBLACK_EX}Clearing Valid Codes.txt")
                clear_valid.write("")
                clear_valid.close()
                time.sleep(0.3)
                print(f"{Fore.YELLOW}[~] Note: {Fore.GREEN}Sucsessfully cleared Valid Codes.txt")

                time.sleep(1)
                os.system("cls")
                print(setup_banner)
                print()

        if setup_menu == "3":
            with open("./version./version.txt", "r") as version:
                vertxt = version.read()
                version.close()
            if vertxt == ver_en:
                print()
                print(f"{Fore.YELLOW}[~] Note: {Fore.RED}No Update found!")
                time.sleep(1.5)
                os.system("cls")
                print(setup_banner)
                print()
            else:
                print()
                print(f"{Fore.GREEN}[~] Success: {Fore.LIGHTBLACK_EX}Update {ver_en} found!")
                qin = input(f"Do you want to install Release {ver_en}? [YES/NO]: ")
                if qin.lower() == "yes":
                    print("ok")
                else:
                    print()
                    print(f"{Fore.YELLOW}[~] Note: {Fore.RED}Installing the update was canceled!")
                    time.sleep(1)
                    os.system("cls")
                    print(setup_banner)
                    print()
        

else:
    #print(f"Das Dokument {file_path} existiert noch nicht.")

    print(f"{Fore.YELLOW}[~] Note: {Fore.LIGHTBLACK_EX}This won't take much time")
    print()
    time.sleep(0.9)
    print(f"{Fore.YELLOW}[~] Note: {Fore.LIGHTBLACK_EX}Creating relevant documents...")



    code_folder = './Codes'

    try:
        os.mkdir(code_folder)
        print(f'The Folder {code_folder} was sucsessfully created.')
        time.sleep(1)
    except FileExistsError:
        print(f'The Folder {code_folder} already exists.')
        time.sleep(1)
    except Exception as e:
        print(f'Error while trying to create Folder: {e}')

    print(f"{Fore.YELLOW}[~] Note: {Fore.LIGHTBLACK_EX}Creating Invalid Codes.txt...")

    with open("./Codes./Invalid Codes.txt", "w") as invalid:
        invalid.close()

    time.sleep(0.5)
    print(f"{Fore.YELLOW}[~] Note: {Fore.LIGHTBLACK_EX}Creating Valid Codes.txt...")

    with open("./Codes./Valid Codes.txt", "w") as valid:
        valid.close()

    time.sleep(0.4)
    print(f"{Fore.YELLOW}[~] Note: {Fore.LIGHTBLACK_EX}Creating setup.txt...")
    with open("./Codes./setup.txt", "w") as setup1:
        setup1.write("Do not delete this file, otherwhise you have to run the setup again.")
        setup1.close()

    time.sleep(0.5)





    version_folder = './version'

    try:
        os.mkdir(version_folder)
        print(f'The Folder {version_folder} was sucsessfully created.')
        time.sleep(1)
    except FileExistsError:
        print(f'The Folder {version_folder} already exists.')
        time.sleep(1)
    except Exception as e:
        print(f'Error while trying to create Folder: {e}')


    print(f"{Fore.YELLOW}[~] Note: {Fore.LIGHTBLACK_EX}Creating date.txt...")

    with open("./version./date.txt", "w") as date:
        date.write(date_en)
        date.close()

    time.sleep(0.5)
    print(f"{Fore.YELLOW}[~] Note: {Fore.LIGHTBLACK_EX}Creating version.txt...")
    with open("./version./version.txt", "w") as version:
        version.write(ver_en)
        version.close()

    time.sleep(0.4)
    print(f"{Fore.YELLOW}[~] Note: {Fore.LIGHTBLACK_EX}Creating setup.txt...")
    with open("./version./setup.txt", "w") as setup:
        setup.write("Do not delete this file, otherwhise you have to run the setup again.")
        setup.close()

    time.sleep(0.8)

    print()
    input(f"{Fore.BLUE}[!] Important: {Fore.LIGHTBLACK_EX}You can run the Setup again to configure files or download the newest version!")
    input(f"{Fore.GREEN}[~] Success: {Fore.LIGHTBLACK_EX}Successfully set up Nova! You can now run the Program")
