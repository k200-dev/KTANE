from colorama import Fore, Style


def Continue():
    print(Fore.GREEN)
    carryOnInput = input("\n[+] Do you want to do another module? [Y/N]: ").lower()
    print(Style.RESET_ALL)
    # If they don't want to carry on change the carry on variable to false so the loop is exited
    if carryOnInput != "y":
        global carryOn
        carryOn = False