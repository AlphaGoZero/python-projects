"""here is a higher lower game"""
from art import logo,vs
from game_data import data
import os
import random

def higher_lower_game():
    winning_streak = 0


    def selector()->int:
        """select the location of dict needed from the list"""
        selected_location = random.randint(0, len(data) - 1)
        return selected_location

        
    def information(
            person:dict)->int:
        """showcase of user information and return its follower count"""
        print(f"{person['name']},a{person['description']} from {person['country']}")
        return person['follower_count']

    
    def answer_section(
            answer:str)->None:
        global winning_streak
        print(f"you selected {answer}")       
        if answer == "A":
            print(f"it has {A_follower} million followers"
                  f", while B has {B_follower} million followers.")    
            if A_follower >= B_follower:
                print("you wins")
                winning_streak +=1
                print(f"winning streak = {winning_streak}")
            else:
                print("you lose")
                winning_streak = 0
                
        if answer == "B":
            print(f"it has {B_follower} million followers"
                  f", while A has {A_follower} million followers.")    
            if B_follower >= A_follower:
                print("you wins")
                winning_streak += 1
                print(f"winning streak = {winning_streak}")
            else:
                print("you lose")
                winning_streak = 0

                
    print(logo)
    A_location = selector()
    print("A")
    A_follower = information(data[A_location])
    print(vs)
    B_location = selector()
    while A_location == B_location:
        B_location = selector()
    print("B")
    B_follower = information(data[B_location])
    print()
    reply =input("do you think which one has a higher "
                 "follower base? reply 'A' or 'B': ")
    answer_section(reply)
    print()
    replay =input("do you want to play again? reply 'yes' or 'no': ")
    if replay == "yes":
        os.system("clear")
        higher_lower_game()
    else:
        print("Goodbye")


higher_lower_game()
