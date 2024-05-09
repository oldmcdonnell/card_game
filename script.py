import copy
import sys
import time
import random
import itertools


# class BuildingBlocks:
#     def __init__(self, suits, values):
#         self.suits = suits
#         ['♥', '♦', '♣', '♠']
#         self.values = [{"value":2,
#                     "face":'2'
#                     },
#                     {'value':3,
#                     "face":'3'
#                     },
#                     {"value":4,
#                     "face":'4'
#                     },
#                     {"value":5,
#                     "face":5
#                     },
#                     {"value":6,
#                         "face":'6'
#                     },
#                     {"value":7,
#                         "face":'7'
#                     },
#                     {"value":8,
#                         "face":'8'
#                     },
#                     {"value":9,
#                         "face":'9'
#                     },
#                     {"value":10,
#                         "face":'10'
#                     },
#                     {"value":11,
#                         "face":'Jack'
#                     },
#                     {"value":12,
#                         "face":'Queen'
#                     },
#                     {"value":13,
#                         "face":'King'
#                     },
#                     {"value":14,
#                         "face":'Ace'
#                     }
#                     ]


suits = ['♥', '♦', '♣', '♠']

values = [{"value":2,
            "face":'2'
            },
            {'value':3,
            "face":'3'
            },
            {"value":4,
             "face":'4'
             },
             {"value":5,
              "face":5
             },
             {"value":6,
                "face":'6'
             },
             {"value":7,
                "face":'7'
             },
             {"value":8,
                "face":'8'
             },
             {"value":9,
                "face":'9'
             },
             {"value":10,
                "face":'10'
             },
             {"value":11,
                "face":'Jack'
             },
             {"value":12,
                "face":'Queen'
             },
             {"value":13,
                "face":'King'
             },
             {"value":14,
                "face":'Ace'
             }
             ]

#basic card class
class Card:
    def __init__(self, value, suit):
        self.value = value["value"]
        self.face = value["face"]
        self.suit = suit

    
    def __str__(self):
        return f"{self.face} of {self.suit}"



class Deck():
    def __init__(self, packs = 1):
        self.packs = packs
        self.cards = [Card(value, suit) for value, suit in itertools.product(values, suits) 
                      for _pack in range(packs)]
        random.shuffle(self.cards)

    def __str__(self):
        return "\n".join(str(card) for card in self.cards)


class Player():
    def __init__(self, name, hand=0, wins=0):
        self.name = name
        self.hand = hand
        self.wins = wins


class Game():
    def create_decks(self):
        self.num_of_decks = input("how many decks do you want?")

    def set_name(self):
        self.name_input = input("Please enter your name")
    
    def __init__(self, deck):
        self.num_of_decks = 0
        self.name = ""

# new_game = Game()
# new_game.set_name()
# new_game.create_decks()
# # if __name__ == "__main__":
# #     deck = Deck(packs=2)
# #     print(deck)      
# deck_test = Deck(packs=2)

# print(deck_test.cards[0], 'and' ,deck_test.cards[1])

# test1 = Winner()
# test2 = Winner()
# if test1.cards[1].value == test2.cards[2].value:
#     print("test success")
#     print(test1.cards[1].value, test2.cards[1].value)
# else:
#     print("test fail")
#     print(test1.cards[1], test2.cards[12])


# # for i in test1.cards:
# #     print(i)



def introduce_player():
    name_input = input("Hello, please input your name: ")
    deck_input = input("how many decks do you want to play with? ")
    deck = Deck(packs = int(deck_input))
    player_hand = deck.cards[0]
    player_one = Player(name_input, player_hand)
    computer_hand = deck.cards[1]
    computer_player = Player("Computer",computer_hand)
    print('Hello', player_one.name)
    print("Your card is the", player_one.hand)
    print("The computer cards is the", computer_player.hand)
    return player_one, computer_player 


players = introduce_player()


def determine_winner(players):

    if players[0].hand.value == players[1].hand.value:
        print("draw")
    elif players[0].hand.value > players[1].hand.value:
        print("player wins")
        players[0].wins += 1
    else:
        print("computer wins")
        players[1].wins += 1
    time.sleep(3)
    print(f'{players[0].name} has {players[0].wins} wins, Computer has {players[1].wins} win')
    new_game = input ("Do you want to play again (Y/N)?")
    if new_game == "Y":
        start_new_game(players)
        return players
    else:
        quit()

players = determine_winner(players)

def start_new_game(players):
    new_hand = Deck()