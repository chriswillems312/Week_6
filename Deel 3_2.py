import random
import pandas as pd

with open("C:/Users/cwill/Dropbox/Master/Python/Basic track/Assignment/buzzwords.txt") as f:
    content = f.read()
    words = content.split()

bingo_card = []
for i in range(25):
    bingo_card.append(random.choice(words))

def mark_words(a, b):
    for i, v in enumerate(bingo_card):
        if a in v:
            bingo_card[i] = v.replace(a, b)
    print(bingo_card)
    print(a)

mark_words("vitesse", "marked")