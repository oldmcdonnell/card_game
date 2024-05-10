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
        self.repeat = True


class Game():
    def create_decks(self):
        self.num_of_decks = input("how many decks do you want? ")

    def set_name(self):
        self.name_input = input("Please enter your name: ")
    
    def __init__(self):
        self.num_of_decks = 0
        self.name = ""
        self.player_wins = 0
        self.computer_wins = 0
        self.stored_data = {}


new_game = Game()
new_game.set_name()
new_game.create_decks()

def start_game():
    print(f'{new_game.name} has {new_game.player_wins} wins, Computer has {new_game.computer_wins} wins')
    deck = Deck(packs = int(new_game.num_of_decks))
    player_hand = deck.cards[0]
    player_one = Player(new_game.name, player_hand)
    computer_hand = deck.cards[1]
    computer_player = Player("Computer",computer_hand)
    print('Hello', new_game.name)
    print("Your card is the", player_one.hand)
    print("The computer cards is the", computer_player.hand)
    return player_one, computer_player 


players = start_game()

def start_new_game():
    print(f'{new_game.name} has {new_game.player_wins} wins, Computer has {new_game.computer_wins} wins')
    time.sleep(2)
    deck = Deck(packs = int(new_game.num_of_decks))
    player_hand = deck.cards[0]
    player_one = Player(new_game.name, player_hand )
    computer_hand = deck.cards[1]
    computer_player = Player("Computer", computer_hand)
    print('Hello', new_game.name)
    print("Your card is the", player_one.hand)
    print("The computer cards is the", computer_player.hand)

def determine_winner(players):
    if players[0].hand.value == players[1].hand.value:
        print("draw")
    elif players[0].hand.value > players[1].hand.value:
        print("player wins")
        new_game.player_wins += 1
    else:
        print("computer wins")
        new_game.computer_wins += 1
    time.sleep(2)
    another_game = input ("Do you want to play again (Y/N)?")
    if another_game == "Y":
        start_new_game()
        return players
    else:
        quit()


players = determine_winner(players)

def start_new_game():
    print(f'{new_game.name} has {new_game.player_wins} wins, Computer has {new_game.computer_wins} wins')
    time.sleep(2)
    deck = Deck(packs = int(new_game.num_of_decks))
    player_hand = deck.cards[0]
    player_one = Player(new_game.name, player_hand )
    computer_hand = deck.cards[1]
    computer_player = Player("Computer", computer_hand)
    print('Hello', new_game.name)
    print("Your card is the", player_one.hand)
    print("The computer cards is the", computer_player.hand)
players = determine_winner(players)

# def start_new_game(players):
#     new_game.player_wins = players[0].wins
#     new_game.computer_wins = players[1].wins
#     print(f'{new_game.name} has {new_game.player_wins} wins, Computer has {new_game.computer_wins} wins')
#     time.sleep(2)
#     deck = Deck(packs = int(new_game.ne computer cards is the", computer_player.hand)
#     player_hand = deck.cards[0]
#     player_one = Player(new_game.name, player_hand )
#     computer_hand = deck.cards[1]
#     computer_player = Player("Computer", computer_hand)
#     print('Hello', new_game.name)
#     print("Your card is the", player_one.hand)
#     print("The computer cards is the", computer_player.hand)
#     return player_one, computer_player