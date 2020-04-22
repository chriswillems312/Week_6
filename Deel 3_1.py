import random

with open("C:/Users/cwill/Dropbox/Master/Python/Basic track/Assignment/buzzwords.txt") as f:
    content = f.read()
    words = content.split()

def generate_card():
    card = {"B": [], "I": [], "N": [], "G": [], "O": []}
    for letter in card:
        card[letter] = random.sample(words, 5)
    return card

def print_card(card):
    for letter in card:
        print(letter, end=" ")
        for number in card[letter]:
            print(number, end=" ")
        print(" ")

def draw(card):
    number_drawn = random.choice(tuple(words))
    for letter in card:
        i = 0
        for number in card[letter]:
            if number == number_drawn:
                card[letter][i] = "X"
            i += 1
    return number_drawn

def check_win(card):
    win = False
    if card["B"][0] == "X" and card["I"][1] == "X" and card["N"][2] == "X" and card["G"][3] == "X" and card["O"][4] == "X":
        win = True
    elif card["O"][0] == "X" and card["G"][1] == "X" and card["N"][2] == "X" and card["I"][3] == "X" and card["B"][4] == "X":
        win = True
    elif card["B"][0] == "X" and card["O"][4] == "X" and card["B"][4] == "X" and card["O"][0] == "X":
        win = True
    return win


def main():
    card = generate_card()
    print_card(card)

    print("\nKeep pressing enter to continue or type quit to exit.\n")
    user_input = input()
    win = check_win(card)
    balls_till_win = 0

    while win == False and user_input != "quit":
        number_drawn = draw(card)
        balls_till_win += 1

        print((f"\nNumber drawn: {number_drawn}." + (f"\tTotal balls drawn: {balls_till_win}")))
        print_card(card)

        win = check_win(card)

        user_input = input()
    if win == True:
        print(f"\nBingo! Total balls to win: {balls_till_win}.")
    else:
        print("Goodbye! Thanks for playing!")

main()