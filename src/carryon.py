from colorama import Fore, Style


def Continue():
    print(Fore.GREEN)
    carryOnInput = input("\n[+] Do you want to do another module? [Y/N]: ").lower()
    print(Style.RESET_ALL)
    if carryOnInput != "y":
        global carryOn
        carryOn = False
