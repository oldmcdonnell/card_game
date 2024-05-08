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

class Deck(Card):
    def __init__(self) -> None:
        pass

print("♥♦♣♠")

print ('\u2663')

deck = [Card(value, color) for value in values for color in colors]

# for i in deck:
#     print(i.value, i.color)

random.shuffle(deck)

for i in deck:
    print(i.value, i.color)
hand = deck[0]
print('hand is', hand.value, hand.color)