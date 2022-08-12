from classes import card


if __name__ == '__main__':
    a=card.Card(4, card.Suits.SPADE, 0).ID
    print(a)
    print(card.Card(a).NUMBER)