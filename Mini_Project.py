# Guessing The Number. 
import random
Easy_Level_Attempts = 10
Hard_Level_Attempts = 5

def set_difficulty(level_choosen):
    if level_choosen == 'easy':
        return Easy_Level_Attempts
    elif level_choosen == 'hard':
        return Hard_Level_Attempts
    else:
        return

def check_answer(guessed_number,answer,attempts):
    if guessed_number < answer:
        print("Your guess is too low")
        return attempts-1
    elif guessed_number > answer:
        print("Your guess is too high")
        return attempts-1
    else:
        print(f"Your guess is right...The answer was {answer}")
        print("****************GAME-OVER****************")

def game():
    print("**********************************************")
    print("-------------Guessing The Number--------------")
    print("**********************************************")
    print("Let me think of a number between 1 to 50")
    answer=random.randint(1,50)
    #print(answer) 
    level=input("Choose level of difficulty...Type 'easy' or 'hard':-")
    attempts=set_difficulty(level)
    if attempts != Easy_Level_Attempts and attempts != Hard_Level_Attempts:
        print("You have entered Wrong difficulty level.. Play again!!")
        return
    
    guessed_number = 0
    while guessed_number!=answer:
        print("------------------------------------------")
        print(f"You have {attempts} remaining to guess the number.")
        guessed_number = int(input("Guess a Number:-"))
        attempts = check_answer(guessed_number,answer,attempts)
        if attempts == 0:
            print("You are out of guess...You lose!")
            return
        elif guessed_number != answer:
            print("Guess again")

game()