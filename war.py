#!/usr/bin/env python3.9

import random
import os
import argparse
import logging

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
if args.verbose:
    logging.basicConfig(format="%(message)s", level=logging.DEBUG)


class Card:
    def __init__(self, suit, rank):
        # Create the 3 attributes of a card by importing the 2 lists, and 1 dictionary
        self.suit = suit
        self.rank = rank
        # import the dictionary by assigning the key values, and the value [rank]
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:

    def __init__(self):

        # create a list that starts blank until filed in    
        self.all_cards = []

        for suit in suits:

            for rank in ranks:

                # Create the card object rotatiing through each suit, hearts-clubs, and each rank 2-ace
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):

        # shuffle all cards in the deck by using the random library
        random.shuffle(self.all_cards)

    def deal_one(self):

        # removes one card from the deck.all_cards as you deal each card to a player
        return self.all_cards.pop()

    def card_total(self):

        return len(self.all_cards)



class Player:

    def __init__(self, name):

        #creates a player class with the attributes name, and giving a deck/hand to the player
        self.name = name
        self.all_cards = []
        self.winnings = []
        self.shuffle_count = 0

    def remove_one(self):

        # creates the function to remove a card from the top of the players deck/hand
        if len(self.all_cards) == 0:
            self.shuffle()
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):

        self.all_cards.append(new_cards)

    def add_winnings(self, new_cards):
        if type(new_cards) == type([]):
            self.winnings.extend(new_cards)
        else:
            self.winnings.append(new_cards)

    def shuffle(self):
        if len(self.all_cards) == 0 and len(self.winnings) > 0:
            random.shuffle(self.winnings)
            self.all_cards.extend(self.winnings)
            self.winnings = []
            print(f"\nPlayer {self.name} has reshuffled winnings")
            print(f"{len(self.all_cards)} left in deck\n")
            self.shuffle_count += 1

    def card_total(self):

        return (len(self.all_cards) + len(self.winnings))

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


def clear():
    
    os.system('clear')

def victory():
    if winner is player_one.name:
        print(f"Player {player_two.name} is out of cards")
    else:
        print(f"Player {player_one.name} is out of cards")
    print(f"PLAYER {winner.upper()} WINS!")
    print(f"Player {player_one.name} shuffled {player_one.shuffle_count} times")
    print(f"Player {player_two.name} shuffled {player_two.shuffle_count} times")
    print(f"Ended game on round {round_num}")
    game_on = False

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack',
         'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

# creates 2 players using the player class function
player_one = Player("One")
player_two = Player("Two")

# create a new ordered deck
new_deck = Deck()

# to debug to see ordered deck, uncomment the next two lines
# for a in new_deck.all_cards:
#    print(a)

# shuffle the deck, ordered decks are boring!
new_deck.shuffle()
# range is a variable of deck size divided by 2
for x in range(new_deck.card_total()//2):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
#starts a new game at round 0, which is immediately followed by a +1 for round 1
round_num = 0

while game_on:

    # time.sleep(3)
    round_num += 1
    print(f"Round {round_num}")
    
    # get a running scoreboard every 5 rounds
    if round_num %1 == 0:
        logging.debug(f"\n--- Scoreboard ---\n"
        f"Player {player_one.name} : {player_one.card_total()}\n"
        f"Player {player_two.name} : {player_two.card_total()}\n"
        )

    # too much output! clear the screen every 50 rounds
    if round_num %50 == 0:
        # clear()
        print(f"Completed round {round_num} cleared output")

    # if player is out of cards, shuffle winnings, apply to bottom of stack
    player_one.shuffle()
    player_two.shuffle()

    if len(player_one.all_cards) == 0:
        victory()
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        victory()
        game_on = False
        break
    
    # players delt hand starts empty, removes one from their deck, and applys it to their delt
    player_one_cards = []
    player_two_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards.append(player_two.remove_one())

    # delt hands are applied, let the games begin!
    at_war = True

    while at_war:
        
        logging.debug(f"Player {player_one.name}: {player_one_cards[-1]} vs. Player {player_two.name}: {player_two_cards[-1]}")
       
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_winnings(player_one_cards)
            player_one.add_winnings(player_two_cards)
            # winner is determined, no additional war needed
            logging.debug(f"Player {player_one.name} wins round {round_num}")
            winner = player_one.name
            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_winnings(player_one_cards)
            player_two.add_winnings(player_two_cards)
            # winner is determined, no additional war needed
            logging.debug(f"Player {player_two.name} wins round {round_num}")
            winner = player_two.name
            at_war = False
        else:
            print("WAR!")

            # determine if players have enough cards to perform war
            if player_one.card_total() < 3:
                print("Player One unable to declare war")
                victory()
                game_on = False
                break
            elif player_two.card_total() < 3:
                print("Player Two unable to declare war")
                victory()
                game_on = False
                break
            else:
                for num in range(3):
                    
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
