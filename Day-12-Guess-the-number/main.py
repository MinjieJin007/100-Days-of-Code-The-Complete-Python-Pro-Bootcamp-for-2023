#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random

#create a global constant in upper case
EASY_ATTEMPTS = 10
HARD_ATTEMPTS =5

#Function to check user's guess against actual answer
def check_answer(guess, com_num, attempts):
  """checks answer against guess. Returns the number of turns remaining."""
  #when we hit the answer at the last chance, there is still one attempt left. Because we don't return attempts-1.
  if com_num == guess:
    print(f"You got it! The answer was {com_num}.")
  elif com_num > guess:
    print("Too low.")
    return attempts - 1
  elif com_num < guess:
    print("Too high.")
    return attempts - 1

#Function to set difficulty.
def set_difficulty():
  difficulty = input("Choose a  difficulty. Type 'easy' or 'hard': ").lower()
  if difficulty == "easy":
    return EASY_ATTEMPTS
  elif difficulty == "hard":
    return HARD_ATTEMPTS

def game():
  print(logo)
  print("Welcome to the Number Guessing Game! \nI'm thinking a number between 1 and 100.")
  com_num = random.randint(1, 100)
  print(f"answer: {com_num}")
  attempts = set_difficulty()
  guess = 0
  while guess != com_num:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attempts = check_answer(guess, com_num, attempts)
    if attempts == 0:
      print("You've run out of guesses, you lose.")
      return
      # return in a function can end a function
    elif guess != com_num:
      print("Guess again.")
  
game()





