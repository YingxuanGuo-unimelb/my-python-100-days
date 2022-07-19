# TODO-1: import the game data and logo and vs, then print the logo.
from art import logo
from art import vs
from game_data import data
import random
from replit import clear
data_now = data
# TODO-2: create a function to choose one person from gamedata randomly and show him to the player.
def choose_item():
    person = random.choice(data_now)
    data_now.remove(person)
    return person

# TODO-3: ask the player to choose which is higher
# TODO-4: create a function to compare the score between two person
def compare_score(first_score, second_score):
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    if first_score > second_score and answer == "A":
        return "You're right!"
    elif first_score < second_score and answer == "B":
        return "You're right!"
    else:
        return "Sorry, that's wrong."

def print_information(person_one, person_two):

    print(f"Compare A: {person_one['name']}, a {person_one['description']}, from {person_one['country']}.")
    print(vs)
    print(f"Against B: {person_two['name']}, a {person_two['description']}, from {person_two['country']}.")
# TODO-5: create a function to turn the winner to the first person and choose another person from the game data randomly, ask the player to guess.
# TODO-6: if the player guess correctly, then call the function and plus 1 score. otherwise he lose. print the score every time after he guesses.

def game_play():
    is_continue = True
    result = "You're right!"
    score = 0
    times = 0
    while is_continue:
        clear()
        print(logo)
        if times != 0:
            print(f"{result} Final score: {score}")
        if result == "Sorry, that's wrong.":
            return
        elif data_now == []:
            print("Congratulations! You've choosed all the correct answers!")
            return
        elif score == 0:
            item_one = choose_item()
            item_two = choose_item()
        else:
            item_one = item_two
            item_two = choose_item()
        print_information(item_one, item_two)
        result = compare_score(item_one['follower_count'], item_two['follower_count'])
        times += 1
        if result == "You're right!":
            score += 1

game_play()
