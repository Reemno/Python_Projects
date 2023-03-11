import random
import string
from words import words

def get_random_word(words):
    random_word=random.choice(words)
    while '-' in random_word or '' in random_word:
        random_word = random.choice(words)
    return random_word.upper()

def hangman():
    word=get_random_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercases)
    used_letters = set()
    user_letter = input("Guess a letter: ").upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter


user_input = input("Type a letter ")
print(user_input)
