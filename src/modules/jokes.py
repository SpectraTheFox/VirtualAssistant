import random

jokes = ["Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I'm afraid for the calendar. Its days are numbered.",
    "Why do fathers take an extra pair of socks when they go golfing? In case they get a hole in one!",
    "What do you call a factory that makes okay products? A satisfactory.",
    "What do you call a fake noodle? An impasta.",
    "What's the best thing about Switzerland? I don't know, but the flag is a big plus.",
    "I don't trust stairs. They're always up to something.",
    "Did you hear about the claustrophobic astronaut? He just needed a little space.",
    "Why don't scientists trust atoms? Because they make up everything!",
    "What did the ocean say to the beach? Nothing, it just waved.",
    "Why did the scarecrow win an award? He was outstanding in his field.",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "What do you call a bear with no teeth? A gummy bear.",
    "How does a penguin build its house? Igloos it together.",
    "Why don't eggs tell jokes? They'd crack each other up.",
    "What do you call a sleeping bull? A bulldozer.",
    "Why did the math book look so sad? Because it had too many problems.",
    "What's orange and sounds like a parrot? A carrot.",
    "Why couldn't the bicycle stand up by itself? It was two tired.",
    "What do you call a fish wearing a bowtie? Sofishticated.",
    "I used to hate facial hair, but then it grew on me."]

def checkactivation(userinput):
    activationkeywords = ["joke", "funny", "laugh"]
    
    if any(keyword in userinput.lower() for keyword in activationkeywords):
        return True
    else:
        return False

def run(userinput):
    joke = random.choice(jokes).strip()
    return joke
