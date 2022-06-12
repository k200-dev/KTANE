# Imports
from art import tprint
import time
import colorama
from colorama import Fore, Style

colorama.init()

# Print the program introduction
print(Fore.RED)
tprint("KTANE")
print(Style.RESET_ALL)
time.sleep(1)

# Define all the needed variables
moduleArrays = ["Wires", "Button", "Simon Says", "Memory"]
total = 1
carryOn = True
positiveTotal = 0

# Checks that the user still wants to do more modules
while carryOn is True:
    # Print the first list item
    print("[0] Exit")
    # Loop for the all the modules in the module array
    for x in moduleArrays:
        # Print the name and respective number of the module in the menu
        print(f"[{total}] {x}")
        # Add to the total to keep the selection numbers correct
        total += 1

    # Resets total
    total = 1
    # Gets the module the user wants
    print(Fore.GREEN)
    moduleInput = int(input("\n[+] Select a module: "))
    print(Style.RESET_ALL)

    from modules.wires import OnTheSubjectOfWires
    from modules.button import OntheSubjectofTheButton
    from modules.simon import OntheSubjectofSimonSays
    from modules.memory import OntheSubjectofMemory

    # Check for the module the user wants to run
    if moduleInput == 0:
        # Quit if module is 0
        quit()
    elif moduleInput == 1:
        OnTheSubjectOfWires()
    elif moduleInput == 2:
        OntheSubjectofTheButton()
    elif moduleInput == 3:
        OntheSubjectofSimonSays()
    elif moduleInput == 4:
        OntheSubjectofMemory()
