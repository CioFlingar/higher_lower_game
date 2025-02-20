from art import logo, vs
from game_data import data
import random
import os

def get_random_bio(already_exist=None):
    """Returns a random bio,  exclude the already exist details."""
    bio = random.choice(data)
    while bio == already_exist:
        bio = random.choice(data)
    return bio




def show_bios(bio_a, bio_b):
    """displays two bios for comparison."""
    print(f"Compare A: {bio_a['name']}, a {bio_a['description']}, from {bio_a['country']}.")
    print(vs)
    print(f"Against B: {bio_b['name']}, a {bio_b['description']}, from {bio_b['country']}.")

def check_answer(guess, bio_a, bio_b):
    """Checks if the user's guess is correct."""
    a_followers = bio_a['follower_count']
    b_followers = bio_b['follower_count']
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


continue_game = True
"""Main game function."""
high_score = 0
while continue_game:
    print(logo)
    user_score = 0
    bio_a = get_random_bio()
    should_continue = True

    while should_continue:
        bio_b = get_random_bio(already_exist=bio_a)
        show_bios(bio_a, bio_b)

        user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
        while user_input not in ['a', 'b']:
            print("Not a valid input! Please chose between 'A' and 'B'.")
            user_input = input("Who has more fan-followers count? Type 'A' or 'B': ").lower()

        if check_answer(user_input, bio_a, bio_b):
            user_score += 1
            print(logo)
            print(f"WOW! Nailed it! Current score: {user_score}")
            bio_a = bio_b  # Move bio_b to bio_a for the next round
        else:
            print(logo)
            print(f"Oh noh! Bad luck -guessed wrong-. Final score: {user_score}")
            if user_score > high_score:
                high_score = user_score
                print(f"New high score: {high_score}!")
            should_continue = False
            continue_game = False

