import sys

## Input Syntax: Ace of Hearts and King of Spades -> AhKs
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

class Hand:
    def __init__(self, cards):
        self.cardA = cards[0]
        self.cardB = cards[1]


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

class Play:
    def __init__(self):
        pass

print(f"Hand 1 is: {hands[0].cardA.getValue()} of {hands[0].cardA.getSuit()} and {hands[0].cardB.getValue()} of {hands[0].cardB.getSuit()}")

print(f"Hand 2 is: {hands[1].cardA.getValue()} of {hands[1].cardA.getSuit()} and {hands[1].cardB.getValue()} of {hands[1].cardB.getSuit()}")