############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

from art import logo
import random
from replit import clear
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def player(p_card):    
    p_card.append(random.choice(cards)) 
    p_card.append(random.choice(cards)) 
    
def computer(c_card):    
    c_card.append(random.choice(cards))
    c_card.append(random.choice(cards))
    
def calculation_score(whose_cards):
    current_score = 0
    for card in whose_cards:
        current_score += card
    return current_score
    
def print_final(p_card, c_card, p_score, c_score):
    print(f"Your final hand: {p_card}, final score: {p_score}")
    print(f"computer's final hand: {c_card}, final score: {c_score}")
    if p_score == 21 and 11 in p_card and 10 in p_card:
        print("Win with a blackjack!")
    elif c_score == 21 and 11 in c_card and 10 in c_card:
        print("Lose, opponent has Blackjack 😱")
    elif p_score > 21:
        print("You went over. You lose 😤")
    elif c_score > 21:
        print("Opponent went over. You win 😁") 
    elif p_score == c_score:
        print("Draw 🙃")
    elif p_score > c_score:
        print("You win 😃")
    else:
        print("You lose 😤")

def player_continue(p_card, p_score, c_card):

    while input("Type 'y' to get another card, type 'n' to pass: ") == "y":
        p_card.append(random.choice(cards))
        p_score = calculation_score(p_card)
        ace_change(p_score, p_card)
        p_score = calculation_score(p_card)
        print_current(p_card, p_score, c_card)
        if p_score > 21:
            return p_score
    return p_score

def computer_continue(c_card, c_score):
    while c_score < 17:
        c_card.append(random.choice(cards))
        c_score = calculation_score(c_card)
        ace_change(c_score, c_card)
        c_score = calculation_score(c_card)
    return c_score
        
def print_current(p_card, p_score, c_card):

    print(f"Your cards: {p_card}, current score: {p_score}")
    print(f"computer's first card: {c_card[0]}")

def ace_change(score, whose_cards):
    if score > 21 and 11 in whose_cards:
        whose_cards[whose_cards.index(11)] = 1
      
def game_start():
    game_continue = True
    while game_continue:
        if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") != "y":
            return
        clear()
        print(logo)
        p_card = []
        c_card = []
        player(p_card)
        computer(c_card)
        p_score = calculation_score(p_card)
        c_score = calculation_score(c_card)
        print_current(p_card, p_score, c_card)
        if p_score == 21 or c_score == 21:
            print_final(p_card, c_card, p_score, c_score)
            game_start()
        else:
            p_score = player_continue(p_card, p_score, c_card)
            c_score = computer_continue(c_card, c_score)
            print_final(p_card, c_card, p_score, c_score)
            
game_start()
