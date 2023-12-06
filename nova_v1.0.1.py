from colorama import Fore
import time
import os
import requests
import random
import string
import concurrent.futures


# Verwende den relativen Pfad zum Unterordner, um auf die Dateien zuzugreifen
with open(os.path.join("./version./date.txt"), "r") as date:
    date_en = date.read()

with open(os.path.join("./version./version.txt"), "r") as version:
    ver_en = version.readline()

ver_en = ver_en.strip()

# banner = f"""{Fore.LIGHTBLUE_EX}


#                                 ███╗   ██╗ ██████╗ ██╗   ██╗ █████╗ 
#                                 ████╗  ██║██╔═══██╗██║   ██║██╔══██╗
#                                 ██╔██╗ ██║██║   ██║██║   ██║███████║     made by vq3x2
#                                 ██║╚██╗██║██║   ██║╚██╗ ██╔╝██╔══██║     version: {ver_en}                                
#                                 ██║ ╚████║╚██████╔╝ ╚████╔╝ ██║  ██║
#                                 ╚═╝  ╚═══╝ ╚═════╝   ╚═══╝  ╚═╝  ╚═╝
#                                 """

# print(banner)



def banner():
    print(f"{Fore.LIGHTBLUE_EX}")

    print()
    print("                            ███╗   ██╗ ██████╗ ██╗   ██╗ █████╗")
    print("                            ████╗  ██║██╔═══██╗██║   ██║██╔══██╗")
    print("                            ██╔██╗ ██║██║   ██║██║   ██║███████║     made by vq3x2")
    print(f"                            ██║╚██╗██║██║   ██║╚██╗ ██╔╝██╔══██║     version: {ver_en}")                                
    print("                            ██║ ╚████║╚██████╔╝ ╚████╔╝ ██║  ██║")
    print("                            ╚═╝  ╚═══╝ ╚═════╝   ╚═══╝  ╚═╝  ╚═╝")
    print()


banner()

leng = 16
char = string.ascii_letters + string.digits

while True:
    try:
        num = int(input(f"{Fore.MAGENTA}                                        Input: {Fore.CYAN}"))
        print()
        print(f"{Fore.BLUE}[~] Note: {Fore.CYAN}Loading...")
        print()
        time.sleep(0.2)

        count = 0
        t0 = time.time()






        
        def send_request(code):
            link = f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"

            response = requests.get(link)

            if response.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] Found: https://discord.gift/{code} {Fore.WHITE}| {Fore.CYAN}Valid")

                with open("./Codes./Valid Codes.txt", "a+", encoding='utf-8') as valid:
                    valid.write(f"https://discord.gift/{code}" + "\n")

            elif response.status_code == 404:
                print(f"{Fore.BLUE}[~] Note: {Fore.MAGENTA}https://discord.gift/{code} {Fore.WHITE}| {Fore.CYAN}Invalid")

                with open("./Codes./Invalid Codes.txt", "a+", encoding='utf-8') as invalid:
                    invalid.write(f"https://discord.gift/{code}" + "\n")

            elif response.status_code == 429:
                print(f"{Fore.RED}[-] Error: {Fore.YELLOW}Banned from Server {Fore.WHITE}| {Fore.LIGHTRED_EX}Reason:", response.reason)
                # time.sleep(0)
                # count += 1

        codes = ["".join(random.choice(char) for i in range(leng)) for _ in range(num)]

        urls = [f"https://discord.gift/{code}" for code in codes]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(send_request, codes)






        print()
        input(f"{Fore.LIGHTBLACK_EX}Checked {Fore.LIGHTRED_EX}{num-count}/{num} {Fore.LIGHTBLACK_EX}in {Fore.LIGHTRED_EX} {time.time()-t0:.2f} seconds {Fore.WHITE}| {Fore.LIGHTBLACK_EX}All codes saved in txt files")
        os.system("cls")
        banner()

    except ValueError:
        print()
        print(f"{Fore.RED}[-] Error: {Fore.YELLOW}Please input an intiger")
        time.sleep(1)
        os.system("cls")
        banner()
