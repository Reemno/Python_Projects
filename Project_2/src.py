import random
import string
from words import words

def get_random_word(words):
    random_word=random.choice(words)
    while '-' in random_word or '' in random_word:
        random_word = random.choice(words)
    return random_word.upper()

