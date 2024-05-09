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
        # shuffled = random.shuffle([Card(value, suit) for value in values for suit in suits])
        # self.cards = shuffled

    def __str__(self):
        return "\n".join(str(card) for card in self.cards)


if __name__ == "__main__":
    deck = Deck(packs=2)
    print(deck)      



# test_deck = Deck()
# for i in test_deck.cards:
#     print(i.color, i.value)


# def multi_deck_fn():
#     num = input("how many decks?" )
#     num_decks = Deck()
#     new_list = []

#     new_list.extend([num_decks] * num)
#     return new_list

# deck1 = Deck()
# deck2 = Deck()

# multi_deck = deck1 + deck2

# for i in multi_deck.cards:
#     print('multi', i.color, i.value)

# # multi_deck = multi_deck_fn()
# print(multi_deck)

# for i in multi_deck.cards:
#     print('multi', i.color, i.value)

# print(test_deck.order)



#    def add_deck(Deck, deck_obj):
#         num_of_deck = input("Please enter the number of decks")
#         multi_deck = num_of_deck * deck_obj
#         print(multi_deck.value, multi_deck.color)
#         #multi_deck = #number of decs
#         #shuffle(multideck)
# print("♥♦♣♠")

# print ('\u2663')

# deck = [Card(value, color) for value in values for color in colors]
# random.shuffle(deck)

# for i in deck:
#     print(i.value, i.color)

# for i in deck:
#     print(i.value, i.color)
# hand = deck[0]
# print('hand is', hand.value, hand.color)
