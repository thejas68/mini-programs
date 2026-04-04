import random

def affirmation_generator():
    affirmations = [
        "You are capable of amazing things.",
        "Your potential is limitless.",
        "You bring light to those around you.",
        "You are stronger than you think.",
        "You deserve happiness and success.",
        "Your kindness makes the world better.",
        "You are enough, just as you are.",
        "You inspire others with your presence."
    ]
    
    name = input("What's your name? ")
    affirmation = random.choice(affirmations)
    print(f"{name}, remember: {affirmation}")

# Run the generator
affirmation_generator()
