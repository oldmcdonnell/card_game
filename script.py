import copy
import sys
import time
import random
import itertools


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
        self.cards = [Card(value, suit) for value, suit in itertools.product(self.values, self.suits) 
                      for _pack in range(packs)]
        random.shuffle(self.cards)

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

    def __str__(self):
        return "\n".join(str(card) for card in self.cards)


class Player():
    def __init__(self, name, hand=0, wins=0):
        self.name = name
        self.hand = hand
        self.wins = wins


class Game():
    def determine_winner(self):
        if self.player_one.hand.value == self.computer_player.hand.value:
            print("draw")
        elif self.player_one.hand.value  > self.computer_player.hand.value:
            print("player wins")
            self.player_one.wins += 1
        else:
            print("computer wins")
            self.computer_player.wins += 1
        time.sleep(2)
        print(f'{self.player_one.name} has {self.player_one.wins} wins, Computer has {self.computer_player.wins} wins')
        another_game = input ("Do you want to play again (Y/N)?")
        if another_game == "Y":
            self.deal()
        else:
            quit()


    def deal(self):
        self.player_one.hand = self.deck.cards[0]
        self.computer_player.hand = self.deck.cards[1]
        print("Your card is the", self.player_one.hand)
        print("The computer cards is the", self.computer_player.hand)
        self.determine_winner()

    def create_decks(self):
        self.num_of_decks = input("how many decks do you want? ")
        return Deck(int(self.num_of_decks))


    def set_name(self):
        return input("Please enter your name: ")

    
    def __init__(self):
        self.num_of_decks = 0
        self.stored_data = {}
        self.player_one = Player(self.set_name())
        self.deck = self.create_decks()
        self.computer_player = Player("Computer")
        print('Hello', self.player_one.name)
        self.deal()




Game()
# new_game.set_name()
# new_game.create_decks()

# def start_game():
#     print(f'{new_game.name} has {new_game.player_wins} wins, Computer has {new_game.computer_wins} wins')
#     deck = Deck(packs = int(new_game.num_of_decks))
#     player_hand = deck.cards[0]
#     player_one = Player(new_game.name, player_hand)
#     computer_hand = deck.cards[1]
#     computer_player = Player("Computer",computer_hand)
#     print('Hello', new_game.name)
#     print("Your card is the", player_one.hand)
#     print("The computer cards is the", computer_player.hand)
#     return player_one, computer_player 


# players = start_game()

# def start_new_game():
#     print(f'{new_game.name} has {new_game.player_wins} wins, Computer has {new_game.computer_wins} wins')
#     time.sleep(2)
#     deck = Deck(packs = int(new_game.num_of_decks))
#     player_hand = deck.cards[0]
#     player_one = Player(new_game.name, player_hand )
#     computer_hand = deck.cards[1]
#     computer_player = Player("Computer", computer_hand)
#     print('Hello', new_game.name)
#     print("Your card is the", player_one.hand)
#     print("The computer cards is the", computer_player.hand)

# def determine_winner(players):
#     if players[0].hand.value == players[1].hand.value:
#         print("draw")
#     elif players[0].hand.value > players[1].hand.value:
#         print("player wins")
#         new_game.player_wins += 1
#     else:
#         print("computer wins")
#         new_game.computer_wins += 1
#     time.sleep(2)
#     another_game = input ("Do you want to play again (Y/N)?")
#     if another_game == "Y":
#         start_new_game()
#         return players
#     else:
#         quit()


# players = determine_winner(players)

# def start_new_game():
#     print(f'{new_game.name} has {new_game.player_wins} wins, Computer has {new_game.computer_wins} wins')
#     time.sleep(2)
#     deck = Deck(packs = int(new_game.num_of_decks))
#     player_hand = deck.cards[0]
#     player_one = Player(new_game.name, player_hand )
#     computer_hand = deck.cards[1]
#     computer_player = Player("Computer", computer_hand)
#     print('Hello', new_game.name)
#     print("Your card is the", player_one.hand)
#     print("The computer cards is the", computer_player.hand)
# players = determine_winner(players)

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