from art import tprint
from colorama import Fore, Style


def OntheSubjectofSimonSays():
    print(Fore.BLUE)
    tprint("Simon Says")
    print(Style.RESET_ALL)

    flashList = []
    inputList = []
    snHasVowel = input("Does the serial number contain a vowel? [Y/N]: ").lower()
    strikeNo = int(input("Enter the number of strikes [0, 1, 2]: "))
    # Input validation for strikes
    while strikeNo > 2 or strikeNo < 0:
        strikeNo = int(input("Invalid input, Enter the number of strikes [0, 1, 2]: "))

    if snHasVowel == "y":
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
