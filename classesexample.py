import random

class Deck(object):
    def __init__(self):
        self.suits =["Spades","Clubs","Hearts","Diamonds"]
        self.ranks = ["1","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]

    def shuffle(self):
        self.cards=[]
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(suit +" of "+ rank)
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()
