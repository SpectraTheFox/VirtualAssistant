import texttospeech
import importlib
import basefunctions



def run(inputmethod, userinput):
    print("Welcome to SpectraTheFox's Virtual Assistant!")
    print("Initializing...")

    if inputmethod is None:
        inputmethod = basefunctions.selectinputmethod()


    if userinput is None:
        userinput = basefunctions.useinputmethod(inputmethod)
        print("No valid input received. Exiting.")
        return
    
    exitkeywords = ["exit", "quit", "goodbye", "bye"]

    while not any(keyword in userinput.lower() for keyword in exitkeywords):
        if userinput.strip() == "":
            print("Empty input received. Please try again.")
        else:
            for line in basefunctions.listmodules():
                module = importlib.import_module(f"modules.{line}")
                
                if module.checkactivation(userinput):
                    response = module.run(userinput)
                    print(f"Assistant: {response}")
                    texttospeech.TextToSpeech(response)
                    break

        userinput = basefunctions.useinputmethod(inputmethod)
        if userinput is None:
            print("No valid input received. Exiting.")
            return

run(None, None)