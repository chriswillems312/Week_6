import random
import time

words = []

with open("C:/Users/cwill/Dropbox/Master/Python/Basic track/Assignment/buzzwords.txt") as f:
    content = f.read()
    words = content.split()

bingo_card = random.sample(words, 25)

for i in bingo_card:
    print(i)
    time.sleep(1)

