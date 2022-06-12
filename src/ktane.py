from art import tprint
import time
import colorama
from colorama import Fore, Style

colorama.init()

print(Fore.RED)
tprint("KTANE")
print(Style.RESET_ALL)
time.sleep(1)

moduleArrays = ["Wires", "Button", "Simon Says", "Memory"]
total = 1
carryOn = True
positiveTotal = 0

# Checks that the user still wants to do more modules
while carryOn is True:
    print("[0] Exit")
    for x in moduleArrays:
        # Print the name and respective number of the module in the menu
        print(f"[{total}] {x}")
        total += 1

    total = 1
    print(Fore.GREEN)
    moduleInput = int(input("\n[+] Select a module: "))
    print(Style.RESET_ALL)

    from modules.wires import OnTheSubjectOfWires
    from modules.button import OntheSubjectofTheButton
    from modules.simon import OntheSubjectofSimonSays
    from modules.memory import OntheSubjectofMemory

    if moduleInput == 0:
        quit()
    elif moduleInput == 1:
        OnTheSubjectOfWires()
    elif moduleInput == 2:
        OntheSubjectofTheButton()
    elif moduleInput == 3:
        OntheSubjectofSimonSays()
    elif moduleInput == 4:
        OntheSubjectofMemory()
