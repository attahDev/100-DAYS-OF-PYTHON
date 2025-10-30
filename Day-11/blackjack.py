import random
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_score(score1, score2):
    if score1 == score2:
        return "You Draw"
    elif score1 == 0:
        return "You Win"
    elif score2 == 0:
        return "You Lose"
    elif score1 > 21:
        return "Bust. You Lose"
    elif score2 > 21:
        return "You Win"
    elif score1 > score2:
        return "You Win"
    else:
        return "You Lose"


def main():
    print(logo)
    user_cards =[]
    computer_cards = []
    user_score = -1
    computer_score = -1
    game_end = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_end:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f" Your cards: {user_cards} and your score is {user_score}")
        print(f"computer picks: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_end = True
        else:
            replay = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if replay == 'y':
                user_cards.append(deal_card())
            else :
                game_end = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final card: {user_cards} and your score is {user_score}")
    print(f"Computer final card: {computer_cards} and computer score is {computer_score}")
    print(compare_score(user_score, computer_score))


while input("Do you want to play a game of BlackJack? (y/n): ").lower() == 'y':
    print("\n" * 20)
    main()

