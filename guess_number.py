"""
  A number guessing game where the program selects a random number between 1 and 20, 
  and the user must guess it. 
  Provide hints like "Too high" or "Too low".
  Make sure that the user is only entering values between 1 and 20 and the user has 
  maximum of 5 guesses. 
  If the user exceeds the max number of gusses then program
  should print "Game over!".

  Algorithm
  -----------------------
  Start
  Generate a random number between 1 and 20
  Set guess count to 1
  Repeat till User makes the correct guess or guess count reaches 5
  Accept the user input
  Verify the user input is between 1 and 20 and if not ask the user to input again
  If user input is less than random number print "Too Low"
  If user input is greater than random number print "Too High"
  If user input is same as random number print "Correct"
  End

"""
import random

random_number = random.randint(1, 20)  # Generate a random number between 1 and 20
guess_count = 0
max_guesses = 5

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 20. Can you guess it?")

while guess_count < max_guesses:
    try:
        guess = int(input("Enter your guess (1-20): "))
        if guess < 1 or guess > 20:
            print("Invalid input! Please enter a number between 1 and 20.")
            continue
        
        guess_count += 1
        
        if guess < random_number:
            print("Too Low!")
        elif guess > random_number:
            print("Too High!")
        else:
            print(f"Correct! You guessed the random number : {random_number} in {guess_count} tries.")
            break
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if guess_count == max_guesses and guess != random_number:
    print("Game over! The correct number was:", random_number)
