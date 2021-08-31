# import pyinputplus for validation
import pyinputplus as pyip

print(pyip.__version__)

new_game = pyip.inputYesNo("Do you want to start new game? yes or no :")

if new_game == "yes":
    print("Welcome!")
    name = pyip.inputStr("Please enter a name: ")
    silly_word = pyip.inputStr("Please enter a silly word: ")
    number = pyip.inputNum("Please enter a number: ")
    adjective = pyip.inputStr("Please enter first adjective: ")
    noun = pyip.inputStr("Please enter a noun: ")
    adjective_2 = pyip.inputStr("Please enter another adjective: ")
    relative = pyip.inputStr("Please enter your relative: ")
    adjective_3 = pyip.inputStr("Please enter another adjective: ")
    verb = pyip.inputStr("Please enter a verb: ")
    adjective_4 = pyip.inputStr("Please enter another adjective: ")
    adjective_5 = pyip.inputStr("Please enter the last one adjective: ")

    print(f"Hello my name is astronaut {name}. I am on my way to planet {silly_word}.I will be gone for {number} days. I am very {adjective} about the trip but I will miss my {noun}. I have heard that the atmosphere there is {adjective_2}. Luckily {relative} packed me a jacket to keep me {adjective_3}. When I land on the planet I will {verb} for joy. I am {adjective_4} to walk on another planet. I could not be more {adjective_5} for this trip!")

else:
    print("Good Bye!")
