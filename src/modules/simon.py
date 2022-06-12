from art import tprint
from colorama import Fore, Style


def on_the_subject_of_simon_says():
    print(Fore.BLUE)
    tprint("Simon Says")
    print(Style.RESET_ALL)

    flash_list = []
    input_list = []
    sn_has_vowel = input("Does the serial number contain a vowel? [Y/N]: ").lower()
    strike_num = int(input("Enter the number of strikes [0, 1, 2]: "))
    # Input validation for strikes
    while strike_num > 2 or strike_num < 0:
        strike_num = int(input("Invalid input, Enter the number of strikes [0, 1, 2]: "))

    if sn_has_vowel == "y":
        if strike_num == 0:
            for i in range(4):
                if i > 0:
                    flash = input(
                        "What colour on the module is flashing next?: "
                    ).lower()
                else:
                    flash = input("What colour on the module is flashing: ").lower()
                while (
                    flash != "red"
                    and flash != "blue"
                    and flash != "green"
                    and flash != "yellow"
                ):
                    if i > 0:
                        flash = input(
                            "Invalid input, What colour on the module is flashing next?: "
                        ).lower()
                    else:
                        flash = input(
                            "Invalid input, What colour on the module is flashing: "
                        ).lower()
                flash_list.append(flash)
                if flash == "red":
                    input_list.append("Blue")
                elif flash == "blue":
                    input_list.append("Red")
                elif flash == "green":
                    input_list.append("Yellow")
                elif flash == "yellow":
                    input_list.append("Green")
                print(Fore.CYAN)
                print("\n Press the colours in this order:", *input_list, sep=" ")
                print(Style.RESET_ALL)

        elif strike_num == 1:
            for i in range(4):
                if i > 0:
                    flash = input(
                        "What colour on the module is flashing next?: "
                    ).lower()
                else:
                    flash = input("What colour on the module is flashing: ").lower()
                while (
                    flash != "red"
                    and flash != "blue"
                    and flash != "green"
                    and flash != "yellow"
                ):
                    if i > 0:
                        flash = input(
                            "Invalid input, What colour on the module is flashing next?: "
                        ).lower()
                    else:
                        flash = input(
                            "Invalid input, What colour on the module is flashing: "
                        ).lower()
                flash_list.append(flash)
                if flash == "red":
                    input_list.append("Yellow")
                elif flash == "blue":
                    input_list.append("Green")
                elif flash == "green":
                    input_list.append("Blue")
                elif flash == "yellow":
                    input_list.append("Red")
                print(Fore.CYAN)
                print("\n Press the colours in this order:", *input_list, sep=" ")
                print(Style.RESET_ALL)

        elif strike_num == 2:
            for i in range(4):
                if i > 0:
                    flash = input(
                        "What colour on the module is flashing next?: "
                    ).lower()
                else:
                    flash = input("What colour on the module is flashing: ").lower()
                while (
                    flash != "red"
                    and flash != "blue"
                    and flash != "green"
                    and flash != "yellow"
                ):
                    if i > 0:
                        flash = input(
                            "Invalid input, What colour on the module is flashing next?: "
                        ).lower()
                    else:
                        flash = input(
                            "Invalid input, What colour on the module is flashing: "
                        ).lower()
                flash_list.append(flash)
                if flash == "red":
                    input_list.append("Green")
                elif flash == "blue":
                    input_list.append("Red")
                elif flash == "green":
                    input_list.append("Yellow")
                elif flash == "yellow":
                    input_list.append("Blue")
                print(Fore.CYAN)
                print("\n Press the colours in this order:", *input_list, sep=" ")
                print(Style.RESET_ALL)

    elif sn_has_vowel == "n":
        if strike_num == 0:
            for i in range(4):
                if i > 0:
                    flash = input(
                        "What colour on the module is flashing next?: "
                    ).lower()
                else:
                    flash = input("What colour on the module is flashing: ").lower()
                while (
                    flash != "red"
                    and flash != "blue"
                    and flash != "green"
                    and flash != "yellow"
                ):
                    if i > 0:
                        flash = input(
                            "Invalid input, What colour on the module is flashing next?: "
                        ).lower()
                    else:
                        flash = input(
                            "Invalid input, What colour on the module is flashing: "
                        ).lower()
                flash_list.append(flash)
                if flash == "red":
                    input_list.append("Blue")
                elif flash == "blue":
                    input_list.append("Yellow")
                elif flash == "green":
                    input_list.append("Green")
                elif flash == "yellow":
                    input_list.append("Red")
                print(Fore.CYAN)
                print("\n Press the colours in this order:", *input_list, sep=" ")
                print(Style.RESET_ALL)

        elif strike_num == 1:
            for i in range(4):
                if i > 0:
                    flash = input(
                        "What colour on the module is flashing next?: "
                    ).lower()
                else:
                    flash = input("What colour on the module is flashing: ").lower()
                while (
                    flash != "red"
                    and flash != "blue"
                    and flash != "green"
                    and flash != "yellow"
                ):
                    if i > 0:
                        flash = input(
                            "Invalid input, What colour on the module is flashing next?: "
                        ).lower()
                    else:
                        flash = input(
                            "Invalid input, What colour on the module is flashing: "
                        ).lower()
                flash_list.append(flash)
                if flash == "red":
                    input_list.append("Red")
                elif flash == "blue":
                    input_list.append("Blue")
                elif flash == "green":
                    input_list.append("Yellow")
                elif flash == "yellow":
                    input_list.append("Green")
                print(Fore.CYAN)
                print("\n Press the colours in this order:", *input_list, sep=" ")
                print(Style.RESET_ALL)

        elif strike_num == 2:
            for i in range(4):
                if i > 0:
                    flash = input(
                        "What colour on the module is flashing next?: "
                    ).lower()
                else:
                    flash = input("What colour on the module is flashing: ").lower()
                while (
                    flash != "red"
                    and flash != "blue"
                    and flash != "green"
                    and flash != "yellow"
                ):
                    if i > 0:
                        flash = input(
                            "Invalid input, What colour on the module is flashing next?: "
                        ).lower()
                    else:
                        flash = input(
                            "Invalid input, What colour on the module is flashing: "
                        ).lower()
                flash_list.append(flash)
                if flash == "red":
                    input_list.append("Yellow")
                elif flash == "blue":
                    input_list.append("Green")
                elif flash == "green":
                    input_list.append("Blue")
                elif flash == "yellow":
                    input_list.append("Red")
                print(Fore.CYAN)
                print("\n Press the colours in this order:", *input_list, sep=" ")
                print(Style.RESET_ALL)

    from main import continue_program

    continue_program()
