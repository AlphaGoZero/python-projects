"""this is a number guessing game"""
from art import logo
import random
import os

def number_guessing_game():

    
    def set_difficulty():
        global trial
        difficulty = input("Wellcome to the number guess game, please "
                       "select the difficult\n reply 'normal' or 'hard'")
        if difficulty =="normal":
            return 10
        elif difficulty =="hard":
            return 5

    
    def compare_number(
            guess:int,
            answer:int)->str:
        if guess > answer:
            return"too high"
        elif guess < answer:
            return"too low"
        elif guess == answer:
            return f"you are correct, the number is {answer}."

    
    answer = random.randint(1,100)
    trial = 0
    game_end =False
    print(logo)
    trial = set_difficulty()

    while game_end == False:
        guess_num = int(input("please enter a number between 1 and 100 "))
        trial -= 1
        print(compare_number(guess_num,answer))
        if guess_num == answer or trial  == 0 :
            game_end = True
        else:
            print(f"you have {trial} trials remained")
    
    replay = input("do you want to play the game again? reply 'yes' or 'no'")
    
    if replay == "yes":
        os.system("clear")
        number_guessing_game()
    elif replay == "no":
        print("Goodbye")

number_guessing_game()
