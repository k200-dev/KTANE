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

    elif numberOfWires == 4:
        # Get all information needed about the four wires
        numberOfRedWires = int(input("Enter the number of red wires: [0 = None] "))
        numberOfBlueWires = int(input("Enter the number of blue wires: [0 = None] "))
        numberOfYellowWires = int(input("Enter the number of yellow wires: [0 = None] "))
        serialNumberOdd = input("Is the last digit of the serial number odd? [Y/N] ").lower()
        lastYellowWire = input("Is the last wire yellow? [Y/N] ").lower()

        if numberOfRedWires > 1 and serialNumberOdd == "y":
            print("\n Cut the last red wire.")
        elif lastYellowWire == "y" and numberOfRedWires == 0:
            print("\n Cut the first wire")
        elif numberOfBlueWires == 1:
            print("\n Cut the first wire.")
        elif numberOfYellowWires > 1:
            print("\n Cut the last wire.")
        else:
            print("\n Cut the second wire.")
    # Check if the user wants to run another module

    if numberOfWires == 5:
        # Get all information needed about the five wires
        lastBlackWire = input("Is the last wire black? [Y/N] ").lower()
        serialNumberOdd = input("Is the last digit of the serial number odd? [Y/N] ").lower()
        numberOfRedWires = int(input("Enter the number of red wires: [0 = None] "))
        numberOfYellowWires = int(input("Enter the number of yellow wires: [0 = None] "))
        numberOfBlackWires = int(input("Enter the number of black wires: [0 = None] "))

        if lastBlackWire == "y" and serialNumberOdd == "y":
            print("\n Cut the fourth wire.")
        elif numberOfRedWires == 1 and numberOfYellowWires > 1:
            print("\n Cut the first wire.")
        elif numberOfBlackWires == 0:
            print("\n Cut the second wire.")
        else:
            print("\n Cut the first wire.")
    
    if numberOfWires == 6:
        # Get all information needed about the six wires
        numberOfYellowWires = int(input("Enter the number of yellow wires: [0 = None] "))
        serialNumberOdd = input("Is the last digit of the serial number odd? [Y/N] ").lower()
        numberOfYellowWires = int(input("Enter the number of yellow wires: [0 = None] "))
        numberOfWhiteWires = int(input("Enter the number of white wires: [0 = None] "))
        numberOfRedWires = int(input("Enter the number of red wires: [0 = None] "))

        if numberOfYellowWires == 0 and serialNumberOdd == "y":
            print("\n Cut the third wire.")
        elif numberOfYellowWires == 1 and numberOfWhiteWires > 1:
            print("\n Cut the fourth wire.")
        elif numberOfRedWires == 0:
            print("\n Cut the last wire.")
        else:
            print("\n Cut the fourth wire.")
    continueProgram()



def OntheSubjectofTheButton():

    # Helper function for onTheSubjectOfButtons
    def buttonLitStrip():
        print("Hold the button down and observe the lit coloured strip on the right of the button")
        litStrip = input("Enter the colour of the strip: ").lower()
        if litStrip == "blue":
            print("Release the button when the countdown timer has a 4 in any position")
        elif litStrip == "white":
            print("Release the button when the countdown timer has a 1 in any position")
        elif litStrip == "yellow":
            print("Release the button when the countdown timer has a 5 in any position")
        else:
            print("Release the button when the countdown timer has a 1 in any position")    


    # Use art module to print ascii text of button
    tprint("Button")


    # Gathering inputs to act on in the main process
    buttonColour = input("Enter the colour of the button: ").lower()
    while buttonColour != "blue" and buttonColour != "red" and buttonColour != "white" and buttonColour != "yellow" and buttonColour != "black":
            buttonColour = input("Invalid input, Enter the colour of the button: ").lower()
    buttonHasText = input("Does the button have text on it? [Y/N]: ").lower()
    while buttonHasText != "y" and buttonHasText != "n":
        buttonHasText = input("Invalid input, Does the button have text on it? [Y/N]: ").lower()
    if buttonHasText == "y":
        buttonText = input("Enter the text on the button: ").lower()
        while buttonText != "abort" and buttonText != "detonate" and buttonText != "hold" and buttonText != "press":
            buttonText = input("Invalid input, Enter the text on the button: ").lower()
    bombHasBatteries = input("Does the bomb have batteries on it? [Y/N]: ").lower()
    while bombHasBatteries != "y" and bombHasBatteries != "n":
        bombHasBatteries = input("Invalid input, Does the button have text on it? [Y/N]: ").lower()
    if bombHasBatteries == "y":
        batteryNo = int(input("Enter the number of batteries on the bomb: "))


    # Code to run if the button is blue
    if buttonColour == "blue":
        # Code to run if the button is blue and says "abort"
        if buttonText == "abort" and buttonColour == "blue":
            buttonLitStrip()
        # Code block to deal with batteries on the bomb
        elif batteryNo > 1 and buttonText == "detonate":
            print("\n Press and immediately release the button")
            return
        elif batteryNo > 2:
            litIndicator = input("Is there a lit indicator with label FRK? [Y/N]: ")
            if litIndicator == "y":
                print("\n Press and immediately release the button")
                return
        else:
            buttonLitStrip()
            return
          

    # Code to run if the button is white
    if buttonColour == "white":
        litIndicator = input("Is there a lit indicator with label CAR? [Y/N]: ").lower()
        while litIndicator != "y" and litIndicator != "n":
            litIndicator = input("Invalid input, Is there a lit indicator with label CAR? [Y/N]: ").lower()
        if litIndicator == "y":
            litStrip()
        # Code block to deal with batteries on the bomb
        elif batteryNo > 1 and buttonText == "detonate":
            print("\n Press and immediately release the button")
            return
        elif batteryNo > 2:
            litIndicator = input("Is there a lit indicator with label FRK? [Y/N]: ")
            while litIndicator != "y" and litIndicator != "n":
                litIndicator = input("Invalid input, Is there a lit indicator with label FRK? [Y/N]: ").lower()
            if litIndicator == "y":
                print("\n Press and immediately release the button")
                return
        else:
            buttonLitStrip()
            return


    # Code to run if the button is yellow
    if buttonColour == "yellow":
        buttonLitStrip()
        # Code block to deal with batteries on the bomb
        if batteryNo > 1 and buttonText == "detonate":
            print("\n Press and immediately release the button")
            return
        elif batteryNo > 2:
            litIndicator = input("Is there a lit indicator with label FRK? [Y/N]: ")
            while litIndicator != "y" and litIndicator != "n":
                litIndicator = input("Invalid input, Is there a lit indicator with label FRK? [Y/N]: ").lower()
            if litIndicator == "y":
                print("\n Press and immediately release the button")
                return
        else:
            buttonLitStrip()
            return


    # Code to run if the button is red and has the text "hold"
    if buttonColour == "red" and buttonText == "hold":
        print("\n Press and immediately release the button")


    # Code to run if the button is only red
    elif buttonColour == "red":
        # Code block to deal with batteries on the bomb
        if batteryNo > 1 and buttonText == "detonate":
            print("\n Press and immediately release the button")
            return
        elif batteryNo > 2:
            litIndicator = input("Is there a lit indicator with label FRK? [Y/N]: ")
            while litIndicator != "y" and litIndicator != "n":
                litIndicator = input("Invalid input, Is there a lit indicator with label FRK? [Y/N]: ").lower()
            if litIndicator == "y":
                print("\n Press and immediately release the button")
                return
        else:
            buttonLitStrip()
            return

    # Catch all statement for batteries
    if buttonColour == "blue" or buttonColour == "white" or buttonColour == "yellow" or buttonColour == "red":
        if bombHasBatteries == "y" and batteryNo > 1 and buttonText == "detonate":
            print("Press and immediately release the button")
            return
        elif bombHasBatteries == "y" and batteryNo > 2:
            litIndicator = input("Is there a lit indicator with label FRK? [Y/N]: ").lower()
            while litIndicator != "y" and litIndicator != "n":
                litIndicator = input("Invalid input, Is there a lit indicator with label FRK? [Y/N]: ").lower()
            if litIndicator == "y":
                buttonLitStrip()
                return
        else:
            buttonLitStrip()
            return


    # Run the continue program function to check if they want to do another module
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
