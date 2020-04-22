from collections import Counter

words = []
word_count = 0

while word_count != 50:
    words.append(input("Choose possible words for your bingo card "))
    for x in words:
        if words.count(x) > 1:
            words.remove(x)
            word_count = word_count - 1
    word_count = word_count + 1
    print(word_count)

with open('buzzwords.txt', 'w') as f:
    for item in words:
        f.write("%s\t" % item)

print(Counter(words))
