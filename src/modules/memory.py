from art import tprint
from colorama import Fore, Style


def OntheSubjectofMemory():
    # Use art module to print ascii text of "Memory"
    print(Fore.BLUE)
    tprint("Memory")
    print(Style.RESET_ALL)

    ## STAGE 1 ##
    stage1DisplayNo = int(input("Enter the number on the display: "))
    while stage1DisplayNo < 1 or stage1DisplayNo > 4:
        stage1DisplayNo = int(
            input("Invalid input, Enter the number on the display [1, 2, 3, 4]: ")
        )

    if stage1DisplayNo == 1 or stage1DisplayNo == 2:
        print(Fore.CYAN)
        print("\n Press the button in the second position. ")
        print(Style.RESET_ALL)
        stage1label = int(input("Enter the label on the button you just pressed: "))
        stage1Pos = 2
    elif stage1DisplayNo == 3:
        print(Fore.CYAN)
        print("\n Press the button in the third position. ")
        print(Style.RESET_ALL)
        stage1label = int(input("Enter the label on the button you just pressed: "))
        stage1Pos = 3
    elif stage1DisplayNo == 4:
        print(Fore.CYAN)
        print("\n Press the button in the fourth position. ")
        print(Style.RESET_ALL)
        stage1label = int(input("Enter the label on the button you just pressed: "))
        stage1Pos = 4

    ## STAGE 2 ##
    stage2DisplayNo = int(input("Enter the number on the display: "))
    while stage2DisplayNo < 1 or stage2DisplayNo > 4:
        stage2DisplayNo = int(
            input("Invalid input, Enter the number on the display [1, 2, 3, 4]: ")
        )

    if stage2DisplayNo == 1:
        print(Fore.CYAN)
        print("\n Press the button labeled 4. ")
        print(Style.RESET_ALL)
        stage2Pos = int(input("Enter the position of the button you just pressed: "))
        stage2label = 4
    elif stage2DisplayNo == 2 or stage2DisplayNo == 4:
        print(Fore.CYAN)
        print(f"\n Press the button in position {stage1Pos}. ")
        print(Style.RESET_ALL)
        stage2label = int(input("Enter the label on the button you just pressed: "))
        stage2Pos = stage1Pos
    elif stage2DisplayNo == 3:
        print(Fore.CYAN)
        print("\n Press the button in position 1. ")
        print(Style.RESET_ALL)
        stage2label = int(input("Enter the label on the button you just pressed: "))
        stage2Pos = 1

    ## STAGE 3 ##
    stage3DisplayNo = int(input("Enter the number on the display: "))
    while stage3DisplayNo < 1 or stage3DisplayNo > 4:
        stage3DisplayNo = int(
            input("Invalid input, Enter the number on the display [1, 2, 3, 4]: ")
        )

    if stage3DisplayNo == 1:
        print(Fore.CYAN)
        print(f"\n Press the button labeled {stage2label}. ")
        print(Style.RESET_ALL)
        stage3label = stage2label
    elif stage3DisplayNo == 2:
        print(Fore.CYAN)
        print(f"\n Press the button labeled {stage1label}")
        print(Style.RESET_ALL)
        stage3label = stage1label
    elif stage3DisplayNo == 3:
        print("\n Press the button in the third position")
        stage3label = int(input("Enter the label on the button you just pressed: "))
    elif stage3DisplayNo == 4:
        print(Fore.CYAN)
        print("\n Press the button labeled 4. ")
        print(Style.RESET_ALL)
        stage3label = 4

    ## STAGE 4 ##
    stage4DisplayNo = int(input("Enter the number on the display: "))
    while stage4DisplayNo < 1 or stage4DisplayNo > 4:
        stage4DisplayNo = int(
            input("Invalid input, Enter the number on the display [1, 2, 3, 4]: ")
        )

    if stage4DisplayNo == 1:
        print(Fore.CYAN)
        print(f"\n Press the button in position {stage1Pos}. ")
        print(Style.RESET_ALL)
        stage4label = int(input("Enter the label on the button you just pressed: "))
    elif stage4DisplayNo == 2:
        print(Fore.CYAN)
        print("\n Press the button in position 1. ")
        print(Style.RESET_ALL)
        stage4label = int(input("Enter the label on the button you just pressed: "))
    elif stage4DisplayNo == 3 or stage4DisplayNo == 4:
        print(Fore.CYAN)
        print(f"\n Press the button in position {stage2Pos}. ")
        print(Style.RESET_ALL)
        stage4label = int(input("Enter the label on the button you just pressed: "))

    ## STAGE 5 ##
    stage5DisplayNo = int(input("Enter the number on the display: "))
    while stage5DisplayNo < 1 or stage5DisplayNo > 4:
        stage5DisplayNo = int(
            input("\n Invalid input, Enter the number on the display [1, 2, 3, 4]: ")
        )

    if stage5DisplayNo == 1:
        print(Fore.CYAN)
        print(f"\n Press the button labeled {stage1label}. ")
        print(Style.RESET_ALL)
    elif stage5DisplayNo == 2:
        print(Fore.CYAN)
        print(f"\n Press the button labeles {stage2label}")
        print(Style.RESET_ALL)
    elif stage5DisplayNo == 3:
        print(Fore.CYAN)
        print(f"Press the button labeles {stage4label}")
        print(Style.RESET_ALL)
    elif stage5DisplayNo == 4:
        print(Fore.CYAN)
        print(f"Press the button labeled {stage3label}")
        print(Style.RESET_ALL)

    from carryon import Continue

    Continue()
