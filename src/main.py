from colorama import Fore, Style
from art import tprint
from os import system, name
from modules.wires import on_the_subject_of_wires
from modules.button import on_the_subject_of_the_button
from modules.simon import on_the_subject_of_simon_says
from modules.memory import on_the_subject_of_memory


def menu():
    total = 1
    modules = ["Wires", "Button", "Simon Says", "Memory"]

    while True:
        tprint("KTANE")
        print("[0] Exit")
        for x in modules:
            # Print the name and respective number of the module in the menu
            print(f"[{total}] {x}")
            total += 1

        total = 1
        print(Fore.GREEN)
        module_input = int(input("\n[+] Select a module: "))
        print(Style.RESET_ALL)

        if module_input == 0:
            quit()
        elif module_input == 1:
            on_the_subject_of_wires()
        elif module_input == 2:
            on_the_subject_of_the_button()
        elif module_input == 3:
            on_the_subject_of_simon_says()
        elif module_input == 4:
            on_the_subject_of_memory()


if __name__ == "__main__":
    menu()
