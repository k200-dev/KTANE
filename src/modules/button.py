from art import tprint
from colorama import Fore, Style


def OntheSubjectofTheButton():

    # Helper function for onTheSubjectOfButtons
    def buttonLitStrip():
        print(
            "Hold the button down and observe the lit coloured strip on the right of the button"
        )
        litStrip = input("Enter the colour of the strip: ").lower()
        if litStrip == "blue":
            print(Fore.CYAN)
            print(
                "\n Release the button when the countdown timer has a 4 in any position"
            )
            print(Style.RESET_ALL)
        elif litStrip == "white":
            print(Fore.CYAN)
            print(
                "\n Release the button when the countdown timer has a 1 in any position"
            )
            print(Style.RESET_ALL)
        elif litStrip == "yellow":
            print(Fore.CYAN)
            print(
                "\n Release the button when the countdown timer has a 5 in any position"
            )
            print(Style.RESET_ALL)
        else:
            print(Fore.CYAN)
            print(
                "\n Release the button when the countdown timer has a 1 in any position"
            )
            print(Style.RESET_ALL)

    # Use art module to print ascii text of button
    print(Fore.BLUE)
    tprint("Button")
    print(Style.RESET_ALL)

    buttonText = ""
    buttonColour = ""
    buttonHasText = ""
    bombHasBatteries = ""
    batteryNo = 0

    # Gathering inputs to act on in the main process
    buttonColour = input("Enter the colour of the button: ").lower()
    while (
        buttonColour != "blue"
        and buttonColour != "red"
        and buttonColour != "white"
        and buttonColour != "yellow"
        and buttonColour != "black"
    ):
        buttonColour = input("Invalid input, Enter the colour of the button: ").lower()
    buttonHasText = input("Does the button have text on it? [Y/N]: ").lower()
    while buttonHasText != "y" and buttonHasText != "n" and buttonHasText != "":
        buttonHasText = input(
            "Invalid input, Does the button have text on it? [Y/N]: "
        ).lower()
    if buttonHasText == "y":
        buttonText = input("Enter the text on the button: ").lower()
        while (
            buttonText != "abort"
            and buttonText != "detonate"
            and buttonText != "hold"
            and buttonText != "press"
        ):
            buttonText = input("Invalid input, Enter the text on the button: ").lower()
    bombHasBatteries = input("Does the bomb have batteries on it? [Y/N]: ").lower()
    while (
        bombHasBatteries != "y" and bombHasBatteries != "n" and bombHasBatteries != ""
    ):
        bombHasBatteries = input(
            "Invalid input, Does the button have text on it? [Y/N]: "
        ).lower()
    if bombHasBatteries == "y":
        batteryNo = int(input("Enter the number of batteries on the bomb: "))

    # Code to run if the button is blue
    if buttonColour == "blue":
        # Code to run if the button is blue and says "abort"
        if buttonText == "abort" and buttonColour == "blue":
            buttonLitStrip()
            return
        # Code block to deal with batteries on the bomb
        elif batteryNo > 1 and buttonText == "detonate":
            print(Fore.CYAN)
            print("\n Press and immediately release the button")
            print(Style.RESET_ALL)
            return
        elif batteryNo > 2:
            litIndicator = input("Is there a lit indicator with label FRK? [Y/N]: ")
            if litIndicator == "y":
                print(Fore.CYAN)
                print("\n Press and immediately release the button")
                print(Style.RESET_ALL)
                return
            else:
                pass
        buttonLitStrip()
        return

    # Code to run if the button is white
    if buttonColour == "white":
        litIndicator = input("Is there a lit indicator with label CAR? [Y/N]: ").lower()
        while litIndicator != "y" and litIndicator != "n":
            litIndicator = input(
                "Invalid input, Is there a lit indicator with label CAR? [Y/N]: "
            ).lower()
        if litIndicator == "y":
            buttonLitStrip()
        # Code block to deal with batteries on the bomb
        elif batteryNo > 1 and buttonText == "detonate":
            print(Fore.CYAN)
            print("\n Press and immediately release the button")
            print(Style.RESET_ALL)
            return
        elif batteryNo > 2:
            litIndicator = input("Is there a lit indicator with label FRK? [Y/N]: ")
            while litIndicator != "y" and litIndicator != "n":
                litIndicator = input(
                    "Invalid input, Is there a lit indicator with label FRK? [Y/N]: "
                ).lower()
            if litIndicator == "y":
                print(Fore.CYAN)
                print("\n Press and immediately release the button")
                print(Style.RESET_ALL)
                return
            else:
                pass
        buttonLitStrip()
        return

    # Code to run if the button is yellow
    if buttonColour == "yellow":
        buttonLitStrip()
        return

    # Code to run if the button is red and has the text "hold"
    if buttonColour == "red" and buttonText == "hold":
        print(Fore.CYAN)
        print("\n Press and immediately release the button")
        print(Style.RESET_ALL)

    # Code to run if the button is only red
    elif buttonColour == "red":
        # Code block to deal with batteries on the bomb
        if batteryNo > 1 and buttonText == "detonate":
            print(Fore.CYAN)
            print("\n Press and immediately release the button")
            print(Style.RESET_ALL)
            return
        elif batteryNo > 2:
            litIndicator = input("Is there a lit indicator with label FRK? [Y/N]: ")
            while litIndicator != "y" and litIndicator != "n":
                litIndicator = input(
                    "Invalid input, Is there a lit indicator with label FRK? [Y/N]: "
                ).lower()
            if litIndicator == "y":
                print(Fore.CYAN)
                print("\n Press and immediately release the button")
                print(Style.RESET_ALL)
                return
            else:
                pass
        buttonLitStrip()
        return

    # Catch all statement for batteries
    if (
        buttonColour == "blue"
        or buttonColour == "white"
        or buttonColour == "yellow"
        or buttonColour == "red"
    ):
        if bombHasBatteries == "y" and batteryNo > 1 and buttonText == "detonate":
            print(Fore.CYAN)
            print("Press and immediately release the button")
            print(Style.RESET_ALL)
            return
        elif bombHasBatteries == "y" and batteryNo > 2:
            litIndicator = input(
                "Is there a lit indicator with label FRK? [Y/N]: "
            ).lower()
            while litIndicator != "y" and litIndicator != "n":
                litIndicator = input(
                    "Invalid input, Is there a lit indicator with label FRK? [Y/N]: "
                ).lower()
            if litIndicator == "y":
                buttonLitStrip()
                return
        else:
            buttonLitStrip()
            return

    # Run the continue program function to check if they want to do another module
    from carryon import Continue

    Continue()
