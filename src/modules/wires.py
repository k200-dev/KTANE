from art import tprint
from colorama import Fore, Style


def on_the_subject_of_wires():
    print(Fore.BLUE)
    tprint("Wires.")
    print(Style.RESET_ALL)
    num_of_wires = int(input("Enter the number of wires: "))
    while num_of_wires < 3 or num_of_wires > 6:
        print("\n[-] Invalid number of wires entered.\n")
        num_of_wires = int(input("Enter the number of wires: "))

    if num_of_wires == 3:
        num_of_red_wires = int(input("Enter the number of red wires: [0 = None] "))
        num_of_blue_wires = int(input("Enter the number of blue wires: [0 = None] "))
        last_white_wire = input("Is the last wire white? [Y/N] ").lower()

        if num_of_red_wires == 0:
            print(Fore.CYAN)
            print("\n Cut the second wire.")
            print(Style.RESET_ALL)
        elif last_white_wire == "y":
            print(Fore.CYAN)
            print("\n Cut the last wire.")
            print(Style.RESET_ALL)
        elif num_of_blue_wires > 1:
            print(Fore.CYAN)
            print("\n Cut the last blue wire.")
            print(Style.RESET_ALL)
        else:
            print(Fore.CYAN)
            print("\n Cut the last wire.")
            print(Style.RESET_ALL)

    elif num_of_wires == 4:
        num_of_red_wires = int(input("Enter the number of red wires: [0 = None] "))
        num_of_blue_wires = int(input("Enter the number of blue wires: [0 = None] "))
        num_of_yellow_wires = int(
            input("Enter the number of yellow wires: [0 = None] ")
        )
        sn_odd = input(
            "Is the last digit of the serial number odd? [Y/N] "
        ).lower()
        last_yellow_wire = input("Is the last wire yellow? [Y/N] ").lower()

        if num_of_red_wires > 1 and sn_odd == "y":
            print(Fore.CYAN)
            print("\n Cut the last red wire.")
            print(Style.RESET_ALL)
        elif last_yellow_wire == "y" and num_of_red_wires == 0:
            print(Fore.CYAN)
            print("\n Cut the first wire")
            print(Style.RESET_ALL)
        elif num_of_blue_wires == 1:
            print(Fore.CYAN)
            print("\n Cut the first wire.")
            print(Style.RESET_ALL)
        elif num_of_yellow_wires > 1:
            print(Fore.CYAN)
            print("\n Cut the last wire.")
            print(Style.RESET_ALL)
        else:
            print(Fore.CYAN)
            print("\n Cut the second wire.")
            print(Style.RESET_ALL)

    if num_of_wires == 5:
        last_black_wire = input("Is the last wire black? [Y/N] ").lower()
        sn_odd = input(
            "Is the last digit of the serial number odd? [Y/N] "
        ).lower()
        num_of_red_wires = int(input("Enter the number of red wires: [0 = None] "))
        num_of_yellow_wires = int(
            input("Enter the number of yellow wires: [0 = None] ")
        )
        num_of_black_wires = int(input("Enter the number of black wires: [0 = None] "))

        if last_black_wire == "y" and sn_odd == "y":
            print(Fore.CYAN)
            print("\n Cut the fourth wire.")
            print(Style.RESET_ALL)
        elif num_of_red_wires == 1 and num_of_yellow_wires > 1:
            print(Fore.CYAN)
            print("\n Cut the first wire.")
            print(Style.RESET_ALL)
        elif num_of_black_wires == 0:
            print(Fore.CYAN)
            print("\n Cut the second wire.")
            print(Style.RESET_ALL)
        else:
            print(Fore.CYAN)
            print("\n Cut the first wire.")
            print(Style.RESET_ALL)

    if num_of_wires == 6:
        num_of_yellow_wires = int(
            input("Enter the number of yellow wires: [0 = None] ")
        )
        sn_odd = input(
            "Is the last digit of the serial number odd? [Y/N] "
        ).lower()
        num_of_yellow_wires = int(
            input("Enter the number of yellow wires: [0 = None] ")
        )
        num_of_white_wires = int(input("Enter the number of white wires: [0 = None] "))
        num_of_red_wires = int(input("Enter the number of red wires: [0 = None] "))

        if num_of_yellow_wires == 0 and sn_odd == "y":
            print(Fore.CYAN)
            print("\n Cut the third wire.")
            print(Style.RESET_ALL)
        elif num_of_yellow_wires == 1 and num_of_white_wires > 1:
            print(Fore.CYAN)
            print("\n Cut the fourth wire.")
            print(Style.RESET_ALL)
        elif num_of_red_wires == 0:
            print(Fore.CYAN)
            print("\n Cut the last wire.")
            print(Style.RESET_ALL)
        else:
            print(Fore.CYAN)
            print("\n Cut the fourth wire.")
            print(Style.RESET_ALL)

    from main import continue_program

    continue_program()
