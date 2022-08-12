import enum
class Suits(enum.Enum):
    SPADE = 0
    HEART = 1
    CLUB = 2
    DIAMOND = 3

"""
 This class defined a card in the deck
 id: is an int that holds all the card info in the form n+13s+52d
 where n is the number 0-12, where 12 is the king,
 s is the suit 0-3 acording to the enum suits and d is the deck
"""
class Card:

    def __init__(self, *argv):
        if not isinstance(argv[0], int):
                raise TypeError
        if(len(argv) ==1):


            self.ID = argv[0]
            self.DECK = self.ID // 52
            self.SUIT=Suits((self.ID - self.DECK * 52) // 13)
            self.NUMBER=(self.ID - 52 * self.DECK - self.SUIT.value * 13)
        elif(len(argv) == 3):
            if argv[0] < 1 or type(argv[0]) is not int:
               self.NUMBER = 1
            if not isinstance(argv[1], Suits):
                raise TypeError
            if not isinstance(argv[2], int):
                raise TypeError
            self.NUMBER = argv[0]
            self.SUIT = argv[1]
            self.DECK = argv[2]
            self.ID = self.NUMBER + self.SUIT.value * 13 + self.DECK * 52






