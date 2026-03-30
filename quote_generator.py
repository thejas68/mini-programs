import random

quotes = [
    "Push yourself, because no one else is going to do it for you.",
    "Success doesn’t come from what you do occasionally, it comes from what you do consistently.",
    "Don’t watch the clock; do what it does. Keep going.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Stay hungry, stay foolish.",
    "Code. Learn. Build. Repeat.",
    "Small progress is still progress."
]

def get_random_quote():
    return random.choice(quotes)

if __name__ == "__main__":
    print("\n💡 Quote of the Day:\n")
    print(get_random_quote())
    