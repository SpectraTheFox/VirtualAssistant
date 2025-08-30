import random 

def checkactivation(userinput):
    activationkeywords = ["coin", "flip", "toss"]
    
    if any(keyword in userinput.lower() for keyword in activationkeywords):
        return True
    else:
        return False
    
def run(userinput):
    outcomes = ["Heads", "Tails"]
    result = random.choice(outcomes)
    return f"The coin landed on {result}."