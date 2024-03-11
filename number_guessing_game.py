"""
A number guessing game which uses the concepts of global and local scope of variables in functions, 
random module and loops in python.

Get your own ASCII text from this link - https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
"""


import random
from art import guess_the_number_logo

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def check_answer(guessed_number, chosen_number):
    if guessed_number < chosen_number:
        print("Too Low. Guess again.")
    elif guessed_number > chosen_number:
        print("Too high. Guess again.")
    return guessed_number
    

def set_difficulty():
    difficulty_chosen = input("Choose difficulty: Type 'easy' or 'hard' - ")
    attempts_number = 0

    if difficulty_chosen == "easy":
        attempts_number = EASY_LEVEL_ATTEMPTS
        return attempts_number
    elif difficulty_chosen == "hard":
        attempts_number = HARD_LEVEL_ATTEMPTS
        return attempts_number
    else:
        print("Please input a valid difficulty level.")


def game():
    print(guess_the_number_logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")

    answer = random.randint(1, 100)

    def start_game():
        attempts = set_difficulty()
        print(f"You get {attempts} attempts to guess the number.")

        while attempts is not 0:
            user_guess = int(input("Make a guess : "))
            guessed_number = check_answer(user_guess, answer)
            if guessed_number == answer:
                print(f"You Won! You have guessed the number correctly in {attempts} attempt.\n{guessed_number} is the correct answer. ")
                break
            attempts -= 1
            print(f"You have {attempts} attempts left.")
            if attempts == 0:
                print("Game Over!")
    
    start_game()
    game_replay = input("Do you want to play again? Type 'y' or 'n' : ")
    while game_replay == 'y':
        start_game()
        replay_choice = input("Do you want to play again? Type 'y' or 'n' : ")
        game_replay = replay_choice
    print("Thankyou for trying this game! See you soon!!")

game()
    

