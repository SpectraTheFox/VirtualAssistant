#import any necessary libraries here


def checkactivation(userinput):
    activationkeywords = [""] # Add keywords that will activate this module
    
    if any(keyword in userinput.lower() for keyword in activationkeywords):
        return True
    else:
        return False
    
def run(userinput):
    # Implement the main functionality of the module here
    return None 