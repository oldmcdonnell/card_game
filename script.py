import copy
import sys
import time
import random
import itertools


suits = ['♥', '♦', '♣', '♠']

values = ['ace', '2', '3', '4', '5', '6', 
          '7', '8', '9', '10', 
          'Jack', 'Queen', 'King']

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


# if __name__ == "__main__":
#     deck = Deck(packs=2)
#     print(deck)      
deck_test = Deck(packs=2)

for i in deck_test:
    print
# class Player():
#     def __init__(self, name, hand):
#         self.name = name
#         self.hand = hand
    
# def introduce_player():
#     name_input = input("Hello, please input your name: ")
#     deck_input = input("how many decks do you want to play with? ")
#     deck = Deck(packs = deck_input)
#     player_one = Player(name_input)
#     print('Hello', player_one.name)

introduce_player()