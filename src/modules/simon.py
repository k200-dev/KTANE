from art import tprint
from colorama import Fore, Style


def OntheSubjectofSimonSays():
    # Use art module to print ascii text of simon says
    print(Fore.BLUE)
    tprint("Simon Says")
    print(Style.RESET_ALL)

    # Getting inputs from user and defining variables
    flashList = []
    inputList = []
    snHasVowel = input("Does the serial number contain a vowel? [Y/N]: ").lower()
    strikeNo = int(input("Enter the number of strikes [0, 1, 2]: "))
    # Input validation for strikes
    while strikeNo > 2 or strikeNo < 0:
        strikeNo = int(input("Invalid input, Enter the number of strikes [0, 1, 2]: "))

    # If the serial number has a vowel
    if snHasVowel == "y":
        # If there are no strikes
        if strikeNo == 0:
            # Repeat four times for number of colour repititions
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
                flashList.append(flash)
                if flash == "red":
                    inputList.append("Blue")
                elif flash == "blue":
                    inputList.append("Red")
                elif flash == "green":
                    inputList.append("Yellow")
                elif flash == "yellow":
                    inputList.append("Green")
                print(Fore.CYAN)
                print("\n Press the colours in this order:", *inputList, sep=" ")
                print(Style.RESET_ALL)

        elif strikeNo == 1:
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
                flashList.append(flash)
                if flash == "red":
                    inputList.append("Yellow")
                elif flash == "blue":
                    inputList.append("Green")
                elif flash == "green":
                    inputList.append("Blue")
                elif flash == "yellow":
                    inputList.append("Red")
                print(Fore.CYAN)
                print("\n Press the colours in this order:", *inputList, sep=" ")
                print(Style.RESET_ALL)

        elif strikeNo == 2:
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
                flashList.append(flash)
                if flash == "red":
                    inputList.append("Green")
                elif flash == "blue":
                    inputList.append("Red")
                elif flash == "green":
                    inputList.append("Yellow")
                elif flash == "yellow":
                    inputList.append("Blue")
                print(Fore.CYAN)
                print("\n Press the colours in this order:", *inputList, sep=" ")
                print(Style.RESET_ALL)

    elif snHasVowel == "n":
        if strikeNo == 0:
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
                flashList.append(flash)
                if flash == "red":
                    inputList.append("Blue")
                elif flash == "blue":
                    inputList.append("Yellow")
                elif flash == "green":
                    inputList.append("Green")
                elif flash == "yellow":
                    inputList.append("Red")
                print(Fore.CYAN)
                print("\n Press the colours in this order:", *inputList, sep=" ")
                print(Style.RESET_ALL)

        elif strikeNo == 1:
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
                flashList.append(flash)
                if flash == "red":
                    inputList.append("Red")
                elif flash == "blue":
                    inputList.append("Blue")
                elif flash == "green":
                    inputList.append("Yellow")
                elif flash == "yellow":
                    inputList.append("Green")
                print(Fore.CYAN)
                print("\n Press the colours in this order:", *inputList, sep=" ")
                print(Style.RESET_ALL)

        elif strikeNo == 2:
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
                flashList.append(flash)
                if flash == "red":
                    inputList.append("Yellow")
                elif flash == "blue":
                    inputList.append("Green")
                elif flash == "green":
                    inputList.append("Blue")
                elif flash == "yellow":
                    inputList.append("Red")
                print(Fore.CYAN)
                print("\n Press the colours in this order:", *inputList, sep=" ")
                print(Style.RESET_ALL)

    from carryon import Continue

    Continue()
