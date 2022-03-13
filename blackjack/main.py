"""this is a blackjack program"""
import random
from art import logo
import os


def blackjack():
    print(logo)
    game_end = False

    
    def deal_card()->int:
        """Deal card value to the player where a = 11 and JQK = 10"""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(cards)


    def calculate_score(
            list_of_cards)->int:
        """calculate the total score of cards owner according to blackjack rule"""
        total = sum(list_of_cards)
        if 11 in list_of_cards:
            if total >21: #if the card pool contain A and the sum exceed 21, A can be counted as 1 instead of 11
                list_of_cards.remove(11)
                list_of_cards.append(1)
        if total == 21: #define win condition as returning 0
            return 0
        return sum(list_of_cards)


    def compare(
            user_score:list,
            computer_score:list)->str:
        """compare the score of player and computer and return winner statement"""
        if user_score == computer_score:
            return "it is a draw"
        if computer_score == 0 or user_score > 21: #computer get blackjack or player get busted
            return "computer wins"
        if user_score == 0 or computer_score > 21: #player get blackjack or computer get busted
            return "user wins"
        else:
            if user_score > computer_score:
                return "user wins"
            else:
                return "computer wins"


    user_cards = [] #player's card pool
    computer_cards= [] #computer's card pool
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    print(f"you got card {user_cards}")
    print(f"computer got card {computer_cards}")
    
    while game_end == False:
        if calculate_score(user_cards) == 0 or calculate_score(user_cards)> 21:
            game_end = True
        if game_end == False:
            reply = input("do you want to draw another card? reply 'yes' or 'no'")
            if reply == "yes":
                user_cards.append(deal_card())
                print(f"you have new card {user_cards[-1]}, your new score is "\
                f"{calculate_score(user_cards)}")
            if reply == "no":
                game_end = True
    """after player deal all the cards he want, deal computer cards"""
    while sum(computer_cards) < 17: #computer need to draw cards until the sum of pool exceed 16
        computer_cards.append(deal_card())
        print(f"computer got card {computer_cards[-1]},the sum is " \
            f"{sum(computer_cards)}")
    """compare the score of player/computer cards and print the result"""
    print(compare(calculate_score(user_cards),calculate_score(computer_cards)))
    repeat_game = input("do you want to play another blackjack game?"\
                        "reply 'yes' or 'no'")
    if repeat_game == "no":
        print("Goodbye")
    else:
        os.system("clear") #clear the screen
        blackjack()


blackjack()
