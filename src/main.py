from colorama import Fore, Style
from modules.wires import on_the_subject_of_wires
from modules.button import on_the_subject_of_the_button
from modules.simon import on_the_subject_of_simon_says
from modules.memory import on_the_subject_of_memory


def continue_program():
    print(Fore.GREEN)
    carryOnInput = input("\n[+] Do you want to do another module? [Y/N]: ").lower()
    print(Style.RESET_ALL)
    if carryOnInput == "y":
        menu(True)
    else:
        quit()


def menu(carryOn):
    total = 1
    modules = ["Wires", "Button", "Simon Says", "Memory"]

    while carryOn is True:
        print("[0] Exit")
        for x in modules:
            # Print the name and respective number of the module in the menu
            print(f"[{total}] {x}")
            total += 1

        total = 1
        print(Fore.GREEN)
        moduleInput = int(input("\n[+] Select a module: "))
        print(Style.RESET_ALL)

        if moduleInput == 0:
            quit()
        elif moduleInput == 1:
            on_the_subject_of_wires()
        elif moduleInput == 2:
            on_the_subject_of_the_button()
        elif moduleInput == 3:
            on_the_subject_of_simon_says()
        elif moduleInput == 4:
            on_the_subject_of_memory()


if __name__ == "__main__":
    menu(True)
