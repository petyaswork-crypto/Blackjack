import random
from art import logo
from rules import rulebook

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Takes a list of cards and returns the calculated score from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    """Compares the user score against the computer score and returns the result as a string."""
    if u_score == c_score:
        return "Draw. 🤷‍♀️\n"
    elif u_score > 21:
        return "You went over. You lose. 🥺\n"
    elif u_score == 0:
        return "Blackjack! You win. 🥳\n"
    elif c_score > 21:
        return "Opponent went over. You win! 😁\n"
    elif c_score == 0:
        return "Opponent has a Blackjack. You lose. 😭\n"
    elif u_score > c_score:
        return "You win! 🎉\n"
    else:
        return "You lose. 😢\n"


def game_on():
    print("\n" * 20)
    print(logo)

    # Initialize empty hands and placeholder scores.
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    game_over = False

    # Deal 2 cards to each player at the start of the round.
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # End the player's turn immediately if: player has blackjack,
        # dealer has blackjack, or player busts.
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            # Otherwise, ask the player whether to hit or stand.
            user_should_deal = input("Type 'yes' to get another card, type 'no' to pass: ")
            if user_should_deal == "yes":
                user_cards.append(deal_card())
            else:
                game_over = True

    # Dealer must keep drawing until reaching at least 17 (or hitting blackjack = 0).
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Reveal both final hands and scores, and print the result of the comparison.
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ") == "yes":
    read_rules = input("Do you want to read the rules first? Type 'yes' or 'no': ")

    if read_rules == 'yes':
        print(rulebook)
        ready_check = input("Are you ready for a game of Blackjack? Type 'yes' or 'no': ")

        if ready_check == 'yes':
            game_on()

        if ready_check == 'no':
            print("Goodbye.")
            break

    if read_rules == 'no':
        game_on()


