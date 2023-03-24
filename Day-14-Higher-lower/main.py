import random
from replit import clear
from art import logo, vs
from game_data import data

def generate_random_account():
  """Get data from random account"""
  return random.choice(data)

def check_answer(choice, person_a_followers, person_b_followers):
  """Checks followers against user's guess and returns True if they got it right. Or False if they got it wrong.""" 
  if person_a_followers > person_b_followers:
    return choice == "a"
  else:
    return choice == "b"

def game():
  game_end = False
  score = 0
  person_a = generate_random_account()
  person_b = generate_random_account()
  print(logo)
  while person_a == person_b:
    person_b = generate_random_account()
  while game_end == False:
    #be careful of '' and "" in print()
    print(f'Compare A: {person_a["name"]}, a {person_a["description"]}, from {person_a["country"]}.')
    print(vs)
    print(f'Against B: {person_b["name"]}, a {person_b["description"]}, from {person_b["country"]}.')
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    clear()
    print(logo)
    is_correct = check_answer(choice, person_a['follower_count'], person_b['follower_count'])
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      print(f"Sorry, that's wrong. Final score: {score}.")
      game_end = True


    person_a = person_b
    person_b = generate_random_account()
        
        

game()