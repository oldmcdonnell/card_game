import copy
import sys
import time
import random
import itertools


suits = ['♥', '♦', '♣', '♠']

values = ['2', '3', '4', '5', '6', 
          '7', '8', '9', '10', 
          'Jack', 'Queen', 'King', 'Ace']

#basic card class
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck():
    def __init__(self, packs = 1):
        self.packs = packs
        self.cards = [Card(value, suit) for value, suit in itertools.product(values, suits) 
                      for _pack in range(packs)]
        random.shuffle(self.cards)

    def __str__(self):
        return "\n".join(str(card) for card in self.cards)
    
class Winner():
    def __init__(self, packs = 1):
        self.packs = packs
        self.cards = [Card(value, suit) for value, suit in itertools.product(values, suits) 
                      for _pack in range(packs)]


    def __str__(self):
        return "\n".join(str(card) for card in self.cards)


class Player():
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

# # if __name__ == "__main__":
# #     deck = Deck(packs=2)
# #     print(deck)      
# deck_test = Deck(packs=2)

# print(deck_test.cards[0], 'and' ,deck_test.cards[1])

test1 = Winner()
test2 = Winner()
if str(test1.cards[1]) == str(test2.cards[1]):
    print("test success")
else:
    print("test fail")
    print(test1.cards[1], test2.cards[1])

for i in test1.cards:
    print(i)


def introduce_player():
    name_input = input("Hello, please input your name: ")
    deck_input = input("how many decks do you want to play with? ")
    deck = Deck(packs = int(deck_input))
    player_hand = deck.cards[0]
    player_one = Player(name_input, player_hand)
    computer_hand = deck.cards[1]
    computer_player = Player("Player",computer_hand)
    print('Hello', player_one.name)
    print("Your card is the", player_one.hand)
    print("The computer cards is the", computer_player.hand)
    return player_one, computer_player 


hands = introduce_player()
# winner_list = [Card(value, suit) for value in values for suit in suits]

def determine_winner(hands):
    winner_list = Winner()
    # if winner_list.cards.index(hands[0]) > winner_list.cards.index(hands[1]):
    #     print("player wins")
    # else:
    #     print("computer wins")
    # time.sleep(3)
    print(f'{hands[0].name}s hand is the {hands[0].hand}, Computer hand is the {hands[1].hand}')
determine_winner(hands)