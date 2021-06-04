# Imports
from art import *
import time

# Print the program introduction
tprint("KTANE")
time.sleep(1)

# Define all the needed variables
moduleArrays = ["Wires", "Button"]
total = 1
carryOn = True
positiveTotal = 0

# The function that checks if the user wants to do another module
def continueProgram():
  # Get their answer to doing another module
  carryOnInput = input("\n[+] Do you want to do another module? [Y/N]: ").lower()
  # If they don't want to carry on change the carry on variable to false so the loop is exited
  if carryOnInput != "y":
      global carryOn
      carryOn = False

# Modules
def OntheSubjectofWires():
    tprint("Wires.")
    # Get the number of wires on the module
    numberOfWires = int(input("Enter the number of wires: "))
    # Validate the number of wires on the module to be in possibility
    while numberOfWires < 3 or numberOfWires > 6:
        print("\n[-] Invalid number of wires entered.\n")
        numberOfWires = int(input("Enter the number of wires: "))
    
    # The logic for three wires, explained on the manual
    if numberOfWires == 3:
        # Get all information needed about the three wires
        numberOfRedWires = int(input("Enter the number of red wires: [0 = None] "))
        numberOfBlueWires = int(input("Enter the number of blue wires: [0 = None] "))
        lastWhiteWire = input("Is the last wire white? [Y/N] ").lower()
        
        # Run the checks with the info above
        if numberOfRedWires == 0:
            print("\n Cut the second wire.")
        elif lastWhiteWire == "y":
            print("\n Cut the last wire.")
        elif numberOfBlueWires > 1:
            print("\n Cut the last blue wire.")
        else:
            print("\n Cut the last wire.")

    # Check if the user wants to run another module
    continueProgram()

def OntheSubjectofTheButton():
    tprint("Button.")
    print("[-] This module is a work in progress")
    # Check if the user wants to run another module
    continueProgram()


# Checks that the user still wants to do more modules
while carryOn == True:
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
    moduleInput = int(input("\n[+] Select a module: "))

    # Check for the module the user wants to run
    if moduleInput == 0:
        # Quit if module is 0
        quit()
    elif moduleInput == 1:
        OntheSubjectofWires()
    elif moduleInput == 2:
        OntheSubjectofTheButton()
