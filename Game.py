import random

class Set:
    def __init__(self):
        self.two = {"C":1, "D":1, "H":1, "P":1}
        self.three = {"C":1, "D":1, "H":1, "P":1}
        self.four = {"C":1, "D":1, "H":1, "P":1}
        self.five = {"C":1, "D":1, "H":1, "P":1}
        self.six = {"C":1, "D":1, "H":1, "P":1}
        self.seven = {"C":1, "D":1, "H":1, "P":1}
        self.eight = {"C":1, "D":1, "H":1, "P":1}
        self.nine = {"C":1, "D":1, "H":1, "P":1}
        self.ten = {"C":1, "D":1, "H":1, "P":1}
        self.knight = {"C":1, "D":1, "H":1, "P":1}
        self.queen = {"C":1, "D":1, "H":1, "P":1}
        self.king = {"C":1, "D":1, "H":1, "P":1}
        self.ace = {"C":1, "D":1, "H":1, "P":1}

class baseValue:
    def __init__(self):
        self.rfs = 1
        self.sfs = 2
        self.fur = 3
        self.ful = 4
        self.fs = 5
        self.sth = 6
        self.thr = 7
        self.tpr = 8
        self.pr = 9
        self.hig = 10

class deepValue:
    def __init__(self, hand):
        pval = 1
        self.uni = {
            "two":2,
            "three":3,
            "four":4,
            "five":5,
            "six":6,
            "seven":7,
            "eight":8,
            "nine":9,
            "ten":10,
            "knight":11,
            "queen":12,
            "king":13,
            "ace":14
        }
        for i in hand:
            if (i in self.uni):
                pvals[pval] = self.uni[i]
            else:
                print(ValueError)

    def compareValue(self):
        pass

class Game:
    def __init__(self, player, players):
        self.playername = player
        self.players = players
        self.round = 0
        self.pot = 0
        self.hand = []
        self.tokens = 100
        self.cardgame = Set()
        self.gamePlay()

    def gamePlay(self):
        while self.tokens > 0:
            self.round += 1
            Round(self.round, self.players)
        print("Game Over")

class Round:
    def __init__(self,round, players):
        self.round = round
        self.players = players
        self.roundCore()

    def roundCore(self):
        self.ongoing = true
        self.callPhase()
        self.drawPhase()
        #Premier call tant que le call n'est pas fini = remain
        #Tirage de carte
        #Deuxieme call
        #Tirage de carte
        #Troisieme call
        #Tirage de carte
        #Dernier call
        #Fin du round
        pass

    def cardDealer(self):
        pass

    def bindRetriever(set):
        pass

    def playOpt(self):
        pass