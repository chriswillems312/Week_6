import random

with open("C:/Users/cwill/Dropbox/Master/Python/Basic track/Assignment/buzzwords.txt") as f:
    content = f.read()
    wordlist = content.split()

bingo_card = []
words = []

bingo_card = random.sample(wordlist, 25)
print("Welcome by this bingo game, the goal is to cross out 10 words, here is your bingo card: ")
print(bingo_card)

while len(bingo_card) != 14:
    print("the word drawn is: ", random.choice(wordlist), "\n")
    words.append(input("which word is drawn? "))
    bingo_card[:] = [x for x in bingo_card if random.choice(words) not in x]
    print("you have", len(bingo_card), "words left on your bingo card", "\n")
    if len(bingo_card) < 15:
        print("CALL BINGO")
    else:
        print("Come on, let's go for the next word :)")

