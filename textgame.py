
##program w no graphics
# Salwa Al-Kuwari
# skkuwari
# Term Project 1: Implimentation of UNO
import random 
import socket 

#from hw7:

class chatComm:
    def __init__(self,ipaddress,portnum):
        self.ip = ipaddress
        self.port = portnum
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def startConnection(self):
        self.s.connect((self.ip, self.port))

direction = 1
class card:
    def __init__ (self, c, v, s):
        self.getColor = c 
        self.getValue = v
        self.special = s
        # colors and vlaues for basic cards
    def printCard(self):
        if not self.special:
            return(self.getColor +"_"+ self.getValue)
        else:
            return((self.getValue))

# function to generate cards 
def deck():
    colors = ["red", "blue", "green", "yellow"]
    values = ['1', '2', '3', '4', '5', '6', '7' ,'8', '9','Draw 2', 'reverse', 'skip', 'show me', '0']
    #how much each card is repeated 
    count = [2] * 13 + [1]


    # list on special cards 
    specialCards = ['_Wild', '_Draw 4', '_swap', '_no']

    # list of all cards 
    unoDeck =[]  
    
    for i in range(len(colors)):
        j = 0
        l = 0

        for j in range (len(values)):
            for k in range (count[l]):
                unoDeck.append(card(colors[i], values[j], False).printCard())            
            l+=1

    for sCard in specialCards:
        for j in range (4):
            unoDeck.append(card("", sCard, True).printCard())

    return unoDeck


class player:
    def __init__ (self, n, c,):
        self.name = n
        self.cards = c
    
    
class UNO:
    def __init__(self, n, d):
        self.numOfPlayers = n
        self.deck = d
        random.shuffle(self.deck)
        self.playerList = []
        self.playerCardsList = []
        self.middleCard = self.generateMiddle()
        self.currentPlayer = 0
        self.won = False
        self.howmanytimes = 0
        self.drawCount = 0
        self.direction = 1
        self.nou = False
        self.lastCard = []
        for i in range (self.numOfPlayers) :
            self.lastCard.append(False)

    def distribute (self):
        for i in range (self.numOfPlayers):
            if len(self.deck) >= 8:
                cards = self.deck[0: 8]
                self.deck = self.deck[8:]
                self.playerList.append(player(int(i+1), cards))

    #helper to generate starting middle card 
    def generateMiddle(self):
        notNumbers = ['Draw 2', 'reverse', 'skip', 'show me', 'Wild', 'Draw 4', 'swap', 'no']
        i = 0
        # loops to find a middle card that has a number
        while (self.deck[i].split('_')[1] in notNumbers):
            i += 1

        middleCard = self.deck[i]
        del self.deck [i]
        return middleCard

    def drawCard(self):
        self.playerList[self.currentPlayer].cards += [self.deck[0]]
        self.deck = self.deck[1:]
        

    def makeMove(self):

        print('middle card is '+ self.middleCard)
        print("player " + str( self.playerList[self.currentPlayer].name) + '\'s cards: ' + str( self.playerList[self.currentPlayer].cards))
        validCard = False
        
        while(validCard == False):
            
            option = int(input('Enter 0 to play card or 1 to draw a card\n'))
            if option == 0:
              index = int(input('Enter the index of the card you would like to play\n'))
              current = self.playerList[self.currentPlayer].cards[index].split('_')[1]
              if self.isValidMove(self.playerList[self.currentPlayer].cards[index], index):
                print ("valid")
                validCard = True
              elif (self.drawCount != 0) and ('Draw' not in current):
                return 1
              elif (self.drawCount == 0)and ('Draw'  in self.middleCard):
                return 1
              else:
                print ("please make a vlaid move!")

            elif option == 1:
                if self.drawCount != 0:
                    # if the player laready has to draw cards he is not allowed the draw card option
                    # instead he will draw the number in the draw count
                    self.draw()
                    return 1
                else:
                    #ptherwise he will draw one card as he chooses
                    self.drawCard()
                return 1
            
        if validCard == True:

            self.middleCard = self.playerList[self.currentPlayer].cards[index]
            del self.playerList[self.currentPlayer].cards[index]
            self.deck.append(self.middleCard)
            validCard = False

            if self.middleCard.split('_')[1] == 'reverse':
                if self.numOfPlayers > 2:
                    self.direction *=-1
                    return -1
                else:
                    self.skip()

            elif self.middleCard.split('_')[1] == 'skip':
                self.skip()

            
            elif self.middleCard.split('_')[1] == 'no u' and self.nou == False:
                self.nou = True
                self.direction *=-1
                return -1
            
            while self.middleCard.split('_')[1] == 'no u' and self.nou == True:
                self.direction *=-1
                return -1
            self.nou = False

            return 1

            
    def isValidMove(self, card, i):
        middleC = self.middleCard.split('_')[0]
        middleN = self.middleCard.split('_')[1]
        cardC = card.split('_')[0]
        cardN = card.split('_')[1]

        if  (self.nou == True) and ('no' not in cardN):
            self.nou = False
            if self.drawCount !=  0:
                self.draw()
                return False
            else:
                return True

        elif  (self.nou == True) and ('no' in cardN):
            if cardN == 'no u':
                return True

        if (self.drawCount !=  0) and ('Draw' not in cardN) and ('no' not in cardN):
            self.draw()
            return False

        if (cardN == middleN or cardC == middleC):
            if cardN.isdigit() or cardN == 'skip' or cardN == 'reverse':
                return True

            elif cardN == 'show me':
                playerNums = []
                for i in range (1, self.numOfPlayers+1):
                    playerNums.append(i)
                del playerNums[self.currentPlayer]

                pNum = int (input( f"choose a player number {playerNums}:\n"))-1
                print('say less:', self.playerList[pNum].cards)
                return True

            if cardN == 'Draw 2':
                self.drawCount += 2
                return True
            
        elif cardN == 'Wild':
            self.wild(i) # I have no idea how this is working??
            return True    

        elif cardN == 'Draw 4' :
            self.wild(i)
            self.drawCount += 4
            return True 

        elif cardN == 'no':
            self.drawCount = 0 
            self.wild(i)
            return True
        
        elif cardN == 'no u':
            return True
        
        elif cardN == 'swap':
            n = int(input("Enter the numebr of the player you want to swap cards with:\n"))
            self.swap(n)
            return True
       
       
    def wild (self, i):
        colors = ["red", "blue", "green", "yellow"]
        color = int(input (('enter the index of the color you want ["red", "blue", "green", "yellow"]:\n')))
        new = colors[color] + self.playerList[self.currentPlayer].cards[i]
        self.playerList[self.currentPlayer].cards[i] = new


    def skip (self):
        if uno.currentPlayer + self.direction ==  uno.numOfPlayers:
            uno.currentPlayer = 0
        else:
            uno.currentPlayer += self.direction


    def draw(self):
        print (f"Draw {self.drawCount} cards lol")
        self.playerList[self.currentPlayer].cards += self.deck[:self.drawCount]
        self.deck = self.deck[self.drawCount:]
        self.drawCount = 0 

    def swap(self, n):
        temp = self.playerList[self.currentPlayer].cards[1:]
        self.playerList[self.currentPlayer].cards =  self.playerList[n-1].cards
        self.playerList[n-1].cards = temp




uno = UNO(2, deck())
uno.distribute()

while not uno.won:
    direction = uno.makeMove() * direction
    uno.currentPlayer +=direction
    if uno.currentPlayer ==  uno.numOfPlayers:
        uno.currentPlayer = 0
    
    

# TP2 updates:
# applied game rules
# show me card can show any players cards
# palyer has a valid car if one of the properties match (number or color for example)
# reverse card reverses the direction if the game
# skip card skips a player
# wild card makes the player changethe color of the middle card 
# draw 2, 4 can pile up
# some bug fixes 
# added a no u card




#time log
# 29/10/2022: lost code <3
# 30/10/2022: got valid card to work for numbers and wild and draw card.
# 31/10/2022: reverse card + fixing bugs  + skip card 
# 01/11/2022: fixed bugs with skip and draw 2 works, draw 4 works, piling up draw cards works, added a no u card which reverses and makes the otehr person draw.
# 02/11/2022: working on no and no u cards, fixing some draw cards bugs
