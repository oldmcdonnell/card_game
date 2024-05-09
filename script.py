import sys
import time
import random

print("program activated")


colors = ['♥', '♦', '♣', '♠']

values = ['ace', '2', '3', '4', '5', '6', 
          '7', '8', '9', '10', 
          'Jack', 'Queen', 'King']

#basic card class
class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

class Deck():
    def __init__(self, amount = 1):
        self.amount = amount
        shuffled = random.shuffle([Card(value, color) for value in values for color in colors])
        self.cards = shuffled

# test_deck = Deck()
# for i in test_deck.cards:
#     print(i.color, i.value)


def multi_deck_fn():
    num = input("how many decks?" )
    num_decks = Deck()
    new_list = []
    
    new_list.extend([num_decks] * num)
    return new_list


multi_deck = multi_deck_fn()
print(multi_deck)

for i in multi_deck.cards:
    print('multi', i.color, i.value)

# print(test_deck.order)



#    def add_deck(Deck, deck_obj):
#         num_of_deck = input("Please enter the number of decks")
#         multi_deck = num_of_deck * deck_obj
#         print(multi_deck.value, multi_deck.color)
#         #multi_deck = #number of decs
#         #shuffle(multideck)
print("♥♦♣♠")

print ('\u2663')

# deck = [Card(value, color) for value in values for color in colors]
# random.shuffle(deck)

# for i in deck:
#     print(i.value, i.color)

# for i in deck:
#     print(i.value, i.color)
# hand = deck[0]
# print('hand is', hand.value, hand.color)
