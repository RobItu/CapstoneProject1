
import random


def card_addition(player_cards):
    total = 0
    for card in player_cards:
        total += card
    if total > 21 and 11 in player_cards:
        total -= 10
    return total


def computer_addition(computer, cards):
    total = 0
    for card in computer:
        total += card

    if total > 21 and 11 in computer:
        total -= 10
        if total >= 21:
            return total

    elif total >= 17:
        return total

    else:
        computer.append(cards[random.randint(0, 12)])
        computer_addition(computer, cards)


def tie_message():
    print(f"Your cards: {player_cards}, your score: {card_addition(player_cards)}")
    print(f"Computer cards: {computer}, its score: {computer_addition(computer, cards)}")
    print("You TIED")


def message():
    print(f"Your cards: {player_cards}, your score: {card_addition(player_cards)}")


def computer_message():
    print(f"Computer cards: {computer}, its score: {computer_addition(computer, cards)}")


def busted_message():
    print(f"Your cards: {player_cards}, your score: {card_addition(player_cards)} \n BUSTED")


start_game = input("Would you like to play BlackJack? y/n \n")
play_again = True
while play_again:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    computer = []

    if start_game == "y":
        player_cards = [cards[random.randint(0, 12)], cards[random.randint(0, 12)]]
        computer = [cards[random.randint(0, 12)]]
        card_addition(player_cards)

        if card_addition(player_cards) <= 21:
            message()
            print(f"Computer cards: {computer}")
            should_continue = True
            while should_continue:
                if input("Another card? y/n \n") == "y":
                    player_cards.append(cards[random.randint(0, 12)])
                    card_addition(player_cards)

                    if card_addition(player_cards) > 21:
                        busted_message()
                        should_continue = False

                    elif card_addition(player_cards) <= 21:
                        message()
                else:
                    should_continue = False

            computer_addition(computer, cards)
            score = card_addition(player_cards)
            cscore = computer_addition(computer, cards)
            computer_score = 21 - cscore
            user_score = 21 - score
            if cscore > 21 and score > 21 or cscore == score:
                tie_message()
            elif cscore > 21 and score <= 21:
                message()
                computer_message()
                print("You win!")
            elif score > 21:
                message()
                computer_message()
                print("You lose!")

            elif computer_score > user_score:
                message()
                computer_message()
                print("You win!")
            else:
                message()
                computer_message()
                print("You lose!")
            play_again = input("Play again? y/n \n")
            if play_again == "n":
                play_again = False



        else:
            busted_message()