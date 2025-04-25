# Dictionary of synonyms
synonyms = {
    "happy": "joyful",
    "sad": "unhappy",
    "fast": "quick",
    "slow": "lethargic",
    "big": "huge",
    "small": "tiny",
    "smart": "intelligent",
    "strong": "powerful"
}

# Take user input
word = input("Enter a word: ").lower()

# Find and display the synonym
if word in synonyms:
    print(f"The synonym of '{word}' is '{synonyms[word]}'.")
else:
    print(f"Sorry, no synonym found for '{word}'.")
