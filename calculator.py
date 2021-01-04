import sys
import random

## Input Syntax: Ace of Hearts and Two of Spades -> Ah2s
##               Jack of Diamonds and Ten of Diamonds -> JTd or JdTd


## For simplicity, A, K, Q, J, T will be represented with
## integer values of 14, 13, 12, 11, 10 respectively

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def getValue(self):
        return self.value
    def getSuit(self):
        return self.suit
    def compareCards(self, cardB):
        if self.getValue() == cardB.getValue() and self.getSuit() == cardB.getSuit():
            return True
        return False
    def printCard(self):
        print(f"{self.value} of {self.suit}")

class Hand:
    def __init__(self, cards):
        self.cardA = cards[0]
        self.cardB = cards[1]
    def getCardA(self):
        return self.cardA
    def getCardB(self):
        return self.cardB
    def printHand(self):
        self.cardA.printCard()
        self.cardB.printCard()

class Play:
    def __init__(self, hands):
        self.player1 = hands[0]
        self.player2 = hands[1]
        self.deck = None
        self.board = None

    def newDeck(self):
        suit_count = 0
        deck = []
        while suit_count <= 3:
            value_count = 2
            while value_count <= 14:
                if suit_count == 0:
                    deck.append(Card(value_count, 'c'))
                elif suit_count == 1:
                    deck.append(Card(value_count, 'd'))
                elif suit_count == 2:
                    deck.append(Card(value_count, 'h'))
                elif suit_count == 3:
                    deck.append(Card(value_count, 's'))
                value_count += 1
            suit_count += 1
        
        indexer = 0
        remove_counter = 0
        while indexer < len(deck):
            c = deck[indexer]

            if c.compareCards(self.player1.getCardA()):
                del deck[indexer]
                indexer -= 1
                remove_counter += 1
            elif c.compareCards(self.player1.getCardB()):
                del deck[indexer]
                indexer -= 1
                remove_counter +=1
            elif c.compareCards(self.player2.getCardA()):
                del deck[indexer]
                indexer -= 1
                remove_counter += 1
            elif c.compareCards(self.player2.getCardB()):
                del deck[indexer]
                indexer -= 1
                remove_counter += 1
            indexer += 1
        if remove_counter != 4:
            print("4 cards were not removed")
            sys.exit()

        self.deck = deck

    def newBoard(self):
        board = []
        flop_random = [random.randint(0, 47), random.randint(0, 46), random.randint(0, 45)]
        turn_random = random.randint(0, 44)
        river_random = random.randint(0, 43)

        board.append(self.deck[flop_random[0]])
        del self.deck[flop_random[0]]
        board.append(self.deck[flop_random[1]])
        del self.deck[flop_random[1]]
        board.append(self.deck[flop_random[2]])
        del self.deck[flop_random[2]]
        board.append(self.deck[turn_random])
        del self.deck[turn_random]
        board.append(self.deck[river_random])
        del self.deck[river_random]

        self.board = board
    
    def printDeck(self):
        for c in self.deck:
            c.printCard()

    def printBoard(self):
        for c in self.board:
            c.printCard()

input_hands = [sys.argv[1].lower(), sys.argv[2].lower()]

def valueToInt(v):
    if v.isdigit():
        return int(v)
    else:
        if v == 'a':
            return 14
        elif v == "k":
            return 13
        elif v == "q":
            return 12
        elif v == "j":
            return 11
        elif v == "t":
            return 10

## Find a way to do this with a for-each loop without the problem of object names

handA = input_hands[0]
if len(handA) == 3:
    first_cardA = Card(valueToInt(handA[0]), handA[2])
    first_cardB = Card(valueToInt(handA[1]), handA[2])
    first_hand = Hand([first_cardA, first_cardB])
elif len(handA) == 4:
    first_cardA = Card(valueToInt(handA[0]), handA[1])
    first_cardB = Card(valueToInt(handA[2]), handA[3])
    first_hand = Hand([first_cardA, first_cardB])
else:
    print("Invalid input")
    sys.exit()

handB = input_hands[1]
if len(handB) == 3:
    second_cardA = Card(valueToInt(handB[0]), handB[2])
    second_cardB = Card(valueToInt(handB[1]), handB[2])
    second_hand = Hand([second_cardA, second_cardB])
elif len(handB) == 4:
    second_cardA = Card(valueToInt(handB[0]), handB[1])
    second_cardB = Card(valueToInt(handB[2]), handB[3])
    second_hand = Hand([second_cardA, second_cardB])
else:
    print("Invalid input")
    sys.exit()

hands = [first_hand, second_hand]

play = Play(hands)
play.newDeck()
play.printDeck()
print("****** DECK BEFORE BOARD")
play.newBoard()
play.printBoard()
print("******** BOARD")
play.printDeck()
print("****** DECK AFTER BOARD")

play.player2.cardA.printCard()
play.player2.cardB.printCard()
## Start at an attempt to execute the above-code with a for-each loop instead

# for h in input_hands:
#     if len(h) == 3:
#         cardA = Card(valueToInt(h[0]), h[2])
#         cardB = Card(valueToInt(h[1]), h[2])
#         hand = Hand([cardA, cardB])
#     elif len(h) == 4:
#         cardA = Card(valueToInt(h[0]). h[1])
#         cardB = Card(valueToInt(h[2]), h[3])
#         hand = Hand([cardA, cardB])
#     else:
#         print("Invalid input")
#         sys.exit()

# print(f"Hand 1 is: {hands[0].cardA.getValue()} of {hands[0].cardA.getSuit()} and {hands[0].cardB.getValue()} of {hands[0].cardB.getSuit()}")

# print(f"Hand 2 is: {hands[1].cardA.getValue()} of {hands[1].cardA.getSuit()} and {hands[1].cardB.getValue()} of {hands[1].cardB.getSuit()}")

