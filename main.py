#Number Guessing Game Objectives:


from random import randint
count_of_easy=10
count_of_hard=5

def difficulty():
    choosen_diff=input("Choose a dificulty.Type 'easy' or 'hard':")
    if choosen_diff=="easy":
        return count_of_easy

    elif choosen_diff=="hard":
         return count_of_hard
        
def check_answer(answer,guess,attempts):
    if answer>guess:
        print("too less")
        return attempts-1
    elif answer<guess:
        print("too high")
        return attempts-1
    else:
        print(f"you guess it correct answer was{answer}")

    
    



def game():
    
    print("Welcome to the Number Guessing Name!\n")
    print("I am thinking of number between 1 and 100:")
    answer=randint(1,100)
    print(f"The Correct Answer is{answer}")

    attempts=difficulty()
    guess=0
    while(guess!=answer):
        print(f"you have {attempts} remaining to guess the number")

        guess=int(input("Make a guess!"))

        attempts=check_answer(answer,guess,attempts)
        if attempts==0:
             print("You've run out of guesses, you lose.")
             return 
        elif guess != answer:
          print("Guess again.")


game()

    
        
    
    
