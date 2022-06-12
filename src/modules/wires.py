from art import tprint
from colorama import Fore, Style


def OnTheSubjectOfWires():
    print(Fore.BLUE)
    tprint("Wires.")
    print(Style.RESET_ALL)
    numberOfWires = int(input("Enter the number of wires: "))
    while numberOfWires < 3 or numberOfWires > 6:
        print("\n[-] Invalid number of wires entered.\n")
        numberOfWires = int(input("Enter the number of wires: "))

    if numberOfWires == 3:
        numberOfRedWires = int(input("Enter the number of red wires: [0 = None] "))
        numberOfBlueWires = int(input("Enter the number of blue wires: [0 = None] "))
        lastWhiteWire = input("Is the last wire white? [Y/N] ").lower()

        if numberOfRedWires == 0:
            print(Fore.CYAN)
            print("\n Cut the second wire.")
            print(Style.RESET_ALL)
        elif lastWhiteWire == "y":
            print(Fore.CYAN)
            print("\n Cut the last wire.")
            print(Style.RESET_ALL)
        elif numberOfBlueWires > 1:
            print(Fore.CYAN)
            print("\n Cut the last blue wire.")
            print(Style.RESET_ALL)
        else:
            print(Fore.CYAN)
            print("\n Cut the last wire.")
            print(Style.RESET_ALL)

    elif numberOfWires == 4:
        numberOfRedWires = int(input("Enter the number of red wires: [0 = None] "))
        numberOfBlueWires = int(input("Enter the number of blue wires: [0 = None] "))
        numberOfYellowWires = int(
            input("Enter the number of yellow wires: [0 = None] ")
        )
        serialNumberOdd = input(
            "Is the last digit of the serial number odd? [Y/N] "
        ).lower()
        lastYellowWire = input("Is the last wire yellow? [Y/N] ").lower()

        if numberOfRedWires > 1 and serialNumberOdd == "y":
            print(Fore.CYAN)
            print("\n Cut the last red wire.")
            print(Style.RESET_ALL)
        elif lastYellowWire == "y" and numberOfRedWires == 0:
            print(Fore.CYAN)
            print("\n Cut the first wire")
            print(Style.RESET_ALL)
        elif numberOfBlueWires == 1:
            print(Fore.CYAN)
            print("\n Cut the first wire.")
            print(Style.RESET_ALL)
        elif numberOfYellowWires > 1:
            print(Fore.CYAN)
            print("\n Cut the last wire.")
            print(Style.RESET_ALL)
        else:
            print(Fore.CYAN)
            print("\n Cut the second wire.")
            print(Style.RESET_ALL)

    if numberOfWires == 5:
        lastBlackWire = input("Is the last wire black? [Y/N] ").lower()
        serialNumberOdd = input(
            "Is the last digit of the serial number odd? [Y/N] "
        ).lower()
        numberOfRedWires = int(input("Enter the number of red wires: [0 = None] "))
        numberOfYellowWires = int(
            input("Enter the number of yellow wires: [0 = None] ")
        )
        numberOfBlackWires = int(input("Enter the number of black wires: [0 = None] "))

        if lastBlackWire == "y" and serialNumberOdd == "y":
            print(Fore.CYAN)
            print("\n Cut the fourth wire.")
            print(Style.RESET_ALL)
        elif numberOfRedWires == 1 and numberOfYellowWires > 1:
            print(Fore.CYAN)
            print("\n Cut the first wire.")
            print(Style.RESET_ALL)
        elif numberOfBlackWires == 0:
            print(Fore.CYAN)
            print("\n Cut the second wire.")
            print(Style.RESET_ALL)
        else:
            print(Fore.CYAN)
            print("\n Cut the first wire.")
            print(Style.RESET_ALL)

    if numberOfWires == 6:
        numberOfYellowWires = int(
            input("Enter the number of yellow wires: [0 = None] ")
        )
        serialNumberOdd = input(
            "Is the last digit of the serial number odd? [Y/N] "
        ).lower()
        numberOfYellowWires = int(
            input("Enter the number of yellow wires: [0 = None] ")
        )
        numberOfWhiteWires = int(input("Enter the number of white wires: [0 = None] "))
        numberOfRedWires = int(input("Enter the number of red wires: [0 = None] "))

        if numberOfYellowWires == 0 and serialNumberOdd == "y":
            print(Fore.CYAN)
            print("\n Cut the third wire.")
            print(Style.RESET_ALL)
        elif numberOfYellowWires == 1 and numberOfWhiteWires > 1:
            print(Fore.CYAN)
            print("\n Cut the fourth wire.")
            print(Style.RESET_ALL)
        elif numberOfRedWires == 0:
            print(Fore.CYAN)
            print("\n Cut the last wire.")
            print(Style.RESET_ALL)
        else:
            print(Fore.CYAN)
            print("\n Cut the fourth wire.")
            print(Style.RESET_ALL)
        from carryon import Continue

        Continue()
