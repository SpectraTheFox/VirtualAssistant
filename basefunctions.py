import random
import os
import listenforinput as listenforinput


def selectinputmethod():
    inputs = ["text", "voice"]
    selectedinput = ""

    while selectedinput not in inputs:
        
        selectedinput = input(f"Choose input method from the following options: {inputs}: \n")
    
        if selectedinput not in inputs:
            print("Invalid input method selected. Please try again.")
            continue
        else:
            print(f"You have selected {selectedinput} as your input method.")
            return selectedinput
                
def usevoiceinput():
    userinput = listenforinput.ListenForInput()
    if userinput is None:
        return None
    else:
        return userinput
    
def usetextinput():
    userinput = input("Please enter your command: \n")
    print(f"You entered: {userinput}")
    return userinput

def useinputmethod(inputmethod):
    if inputmethod == "voice":
        return usevoiceinput()
    elif inputmethod == "text":
        return usetextinput()

def getrandomgreeting():
    greetings = [
        "Hello, how can I assist you today?",
        "Hi there! What can I do for you?",
        "Greetings! How may I help you?",
        "Hey! What would you like to know?",
        "Good day! How can I be of service?",
    ]
    return random.choice(greetings)

def getrandomfarewell():
    farewells = [
        "Goodbye! Have a great day!",
        "See you later! Take care!",
        "Farewell! Until next time!",
        "Bye! Stay safe!",
        "Take care! Talk to you soon!",
    ]
    return random.choice(farewells)

def listmodules():
    moduleslist = []
    for (dirpath, dirnames, filenames) in os.walk("modules"):
        moduleslist.extend(filenames)
        break
    moduleslist = [x.replace(".py", "") for x in moduleslist]
    if ".DS_Store" in moduleslist:
        moduleslist.remove(".DS_Store")
    return moduleslist
    