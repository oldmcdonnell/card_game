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

print(deck)