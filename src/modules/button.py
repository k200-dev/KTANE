from art import tprint
from colorama import Fore, Style


def on_the_subject_of_the_button():

    # Helper function for on_the_subject_of_the_button
    def button_lit_strip():
        print(
            "Hold the button down and observe the lit coloured strip on the right of the button"
        )
        lit_strip = input("Enter the colour of the strip: ").lower()
        if lit_strip == "blue":
            print(Fore.CYAN)
            print(
                "\n Release the button when the countdown timer has a 4 in any position"
            )
            print(Style.RESET_ALL)
        elif lit_strip == "white":
            print(Fore.CYAN)
            print(
                "\n Release the button when the countdown timer has a 1 in any position"
            )
            print(Style.RESET_ALL)
        elif lit_strip == "yellow":
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

    print(Fore.BLUE)
    tprint("Button")
    print(Style.RESET_ALL)

    button_text = ""
    button_colour = ""
    button_has_text = ""
    bomb_has_batteries = ""
    battery_num = 0

    button_colour = input("Enter the colour of the button: ").lower()
    while (
        button_colour != "blue"
        and button_colour != "red"
        and button_colour != "white"
        and button_colour != "yellow"
        and button_colour != "black"
    ):
        button_colour = input("Invalid input, Enter the colour of the button: ").lower()
    button_has_text = input("Does the button have text on it? [Y/N]: ").lower()
    while button_has_text != "y" and button_has_text != "n" and button_has_text != "":
        button_has_text = input(
            "Invalid input, Does the button have text on it? [Y/N]: "
        ).lower()
    if button_has_text == "y":
        button_text = input("Enter the text on the button: ").lower()
        while (
            button_text != "abort"
            and button_text != "detonate"
            and button_text != "hold"
            and button_text != "press"
        ):
            button_text = input("Invalid input, Enter the text on the button: ").lower()
    bomb_has_batteries = input("Does the bomb have batteries on it? [Y/N]: ").lower()
    while (
        bomb_has_batteries != "y"
        and bomb_has_batteries != "n"
        and bomb_has_batteries != ""
    ):
        bomb_has_batteries = input(
            "Invalid input, Does the button have text on it? [Y/N]: "
        ).lower()
    if bomb_has_batteries == "y":
        battery_num = int(input("Enter the number of batteries on the bomb: "))

    if button_colour == "blue":
        if button_text == "abort" and button_colour == "blue":
            button_lit_strip()
            return
        elif battery_num > 1 and button_text == "detonate":
            print(Fore.CYAN)
            print("\n Press and immediately release the button")
            print(Style.RESET_ALL)
            return
        elif battery_num > 2:
            lit_indicator = input("Is there a lit indicator with label FRK? [Y/N]: ")
            if lit_indicator == "y":
                print(Fore.CYAN)
                print("\n Press and immediately release the button")
                print(Style.RESET_ALL)
                return
            else:
                pass
        button_lit_strip()
        return

    if button_colour == "white":
        lit_indicator = input(
            "Is there a lit indicator with label CAR? [Y/N]: "
        ).lower()
        while lit_indicator != "y" and lit_indicator != "n":
            lit_indicator = input(
                "Invalid input, Is there a lit indicator with label CAR? [Y/N]: "
            ).lower()
        if lit_indicator == "y":
            button_lit_strip()
        # Code block to deal with batteries on the bomb
        elif battery_num > 1 and button_text == "detonate":
            print(Fore.CYAN)
            print("\n Press and immediately release the button")
            print(Style.RESET_ALL)
            return
        elif battery_num > 2:
            lit_indicator = input("Is there a lit indicator with label FRK? [Y/N]: ")
            while lit_indicator != "y" and lit_indicator != "n":
                lit_indicator = input(
                    "Invalid input, Is there a lit indicator with label FRK? [Y/N]: "
                ).lower()
            if lit_indicator == "y":
                print(Fore.CYAN)
                print("\n Press and immediately release the button")
                print(Style.RESET_ALL)
                return
            else:
                pass
        button_lit_strip()
        return

    if button_colour == "yellow":
        button_lit_strip()
        return

    if button_colour == "red" and button_text == "hold":
        print(Fore.CYAN)
        print("\n Press and immediately release the button")
        print(Style.RESET_ALL)

    elif button_colour == "red":
        # Code block to deal with batteries on the bomb
        if battery_num > 1 and button_text == "detonate":
            print(Fore.CYAN)
            print("\n Press and immediately release the button")
            print(Style.RESET_ALL)
            return
        elif battery_num > 2:
            lit_indicator = input("Is there a lit indicator with label FRK? [Y/N]: ")
            while lit_indicator != "y" and lit_indicator != "n":
                lit_indicator = input(
                    "Invalid input, Is there a lit indicator with label FRK? [Y/N]: "
                ).lower()
            if lit_indicator == "y":
                print(Fore.CYAN)
                print("\n Press and immediately release the button")
                print(Style.RESET_ALL)
                return
            else:
                pass
        button_lit_strip()
        return

    # Catch all statement for batteries
    if (
        button_colour == "blue"
        or button_colour == "white"
        or button_colour == "yellow"
        or button_colour == "red"
    ):
        if bomb_has_batteries == "y" and battery_num > 1 and button_text == "detonate":
            print(Fore.CYAN)
            print("Press and immediately release the button")
            print(Style.RESET_ALL)
            return
        elif bomb_has_batteries == "y" and battery_num > 2:
            lit_indicator = input(
                "Is there a lit indicator with label FRK? [Y/N]: "
            ).lower()
            while lit_indicator != "y" and lit_indicator != "n":
                lit_indicator = input(
                    "Invalid input, Is there a lit indicator with label FRK? [Y/N]: "
                ).lower()
            if lit_indicator == "y":
                button_lit_strip()
                return
        else:
            button_lit_strip()
            return

    from main import continue_program

    continue_program()
