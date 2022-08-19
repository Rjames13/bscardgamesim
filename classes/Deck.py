import random

from classes.card import Card


class Deck():
    cards=[]
    def __init__(self, deckmultiplier=1):

        for i in range(0,deckmultiplier*52):
            self.cards.append(Card(i))
    def shuffle(self):
        random.shuffle(self.cards)



