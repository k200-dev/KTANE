from art import tprint
from colorama import Fore, Style


def on_the_subject_of_memory():
    print(Fore.BLUE)
    tprint("Memory")
    print(Style.RESET_ALL)

    ## STAGE 1 ##
    stage_one_display_num = int(input("Enter the number on the display: "))
    while stage_one_display_num < 1 or stage_one_display_num > 4:
        stage_one_display_num = int(
            input("Invalid input, Enter the number on the display [1, 2, 3, 4]: ")
        )

    if stage_one_display_num == 1 or stage_one_display_num == 2:
        print(Fore.CYAN)
        print("\n Press the button in the second position. ")
        print(Style.RESET_ALL)
        stage_one_label = int(input("Enter the label on the button you just pressed: "))
        stage_one_pos = 2
    elif stage_one_display_num == 3:
        print(Fore.CYAN)
        print("\n Press the button in the third position. ")
        print(Style.RESET_ALL)
        stage_one_label = int(input("Enter the label on the button you just pressed: "))
        stage_one_pos = 3
    elif stage_one_display_num == 4:
        print(Fore.CYAN)
        print("\n Press the button in the fourth position. ")
        print(Style.RESET_ALL)
        stage_one_label = int(input("Enter the label on the button you just pressed: "))
        stage_one_pos = 4

    ## STAGE 2 ##
    stage_two_display_num = int(input("Enter the number on the display: "))
    while stage_two_display_num < 1 or stage_two_display_num > 4:
        stage_two_display_num = int(
            input("Invalid input, Enter the number on the display [1, 2, 3, 4]: ")
        )

    if stage_two_display_num == 1:
        print(Fore.CYAN)
        print("\n Press the button labeled 4. ")
        print(Style.RESET_ALL)
        stage_two_pos = int(input("Enter the position of the button you just pressed: "))
        stage_two_label = 4
    elif stage_two_display_num == 2 or stage_two_display_num == 4:
        print(Fore.CYAN)
        print(f"\n Press the button in position {stage_one_pos}. ")
        print(Style.RESET_ALL)
        stage_two_label = int(input("Enter the label on the button you just pressed: "))
        stage_two_pos = stage_one_pos
    elif stage_two_display_num == 3:
        print(Fore.CYAN)
        print("\n Press the button in position 1. ")
        print(Style.RESET_ALL)
        stage_two_label = int(input("Enter the label on the button you just pressed: "))
        stage_two_pos = 1

    ## STAGE 3 ##
    stage_three_display_num = int(input("Enter the number on the display: "))
    while stage_three_display_num < 1 or stage_three_display_num > 4:
        stage_three_display_num = int(
            input("Invalid input, Enter the number on the display [1, 2, 3, 4]: ")
        )

    if stage_three_display_num == 1:
        print(Fore.CYAN)
        print(f"\n Press the button labeled {stage_two_label}. ")
        print(Style.RESET_ALL)
        stage_three_label = stage_two_label
    elif stage_three_display_num == 2:
        print(Fore.CYAN)
        print(f"\n Press the button labeled {stage_one_label}")
        print(Style.RESET_ALL)
        stage_three_label = stage_one_label
    elif stage_three_display_num == 3:
        print("\n Press the button in the third position")
        stage_three_label = int(input("Enter the label on the button you just pressed: "))
    elif stage_three_display_num == 4:
        print(Fore.CYAN)
        print("\n Press the button labeled 4. ")
        print(Style.RESET_ALL)
        stage_three_label = 4

    ## STAGE 4 ##
    stage_four_display_num = int(input("Enter the number on the display: "))
    while stage_four_display_num < 1 or stage_four_display_num > 4:
        stage_four_display_num = int(
            input("Invalid input, Enter the number on the display [1, 2, 3, 4]: ")
        )

    if stage_four_display_num == 1:
        print(Fore.CYAN)
        print(f"\n Press the button in position {stage_one_pos}. ")
        print(Style.RESET_ALL)
        stage_four_label = int(input("Enter the label on the button you just pressed: "))
    elif stage_four_display_num == 2:
        print(Fore.CYAN)
        print("\n Press the button in position 1. ")
        print(Style.RESET_ALL)
        stage_four_label = int(input("Enter the label on the button you just pressed: "))
    elif stage_four_display_num == 3 or stage_four_display_num == 4:
        print(Fore.CYAN)
        print(f"\n Press the button in position {stage_two_pos}. ")
        print(Style.RESET_ALL)
        stage_four_label = int(input("Enter the label on the button you just pressed: "))

    ## STAGE 5 ##
    stage_five_display_num = int(input("Enter the number on the display: "))
    while stage_five_display_num < 1 or stage_five_display_num > 4:
        stage_five_display_num = int(
            input("\n Invalid input, Enter the number on the display [1, 2, 3, 4]: ")
        )

    if stage_five_display_num == 1:
        print(Fore.CYAN)
        print(f"\n Press the button labeled {stage_one_label}. ")
        print(Style.RESET_ALL)
    elif stage_five_display_num == 2:
        print(Fore.CYAN)
        print(f"\n Press the button labeles {stage_two_label}")
        print(Style.RESET_ALL)
    elif stage_five_display_num == 3:
        print(Fore.CYAN)
        print(f"Press the button labeles {stage_four_label}")
        print(Style.RESET_ALL)
    elif stage_five_display_num == 4:
        print(Fore.CYAN)
        print(f"Press the button labeled {stage_three_label}")
        print(Style.RESET_ALL)

    from main import continue_program

    continue_program()
