import pygame
import random 
pygame.init()
direction = 1

#frame
clock = pygame.time.Clock()

#display
screen = pygame.display.set_mode((1300,600))
pygame.display.set_caption("UNO")

#background
pink = (219,112,147)
black = (0, 0, 0)
white = (255, 255, 255)
#background from: https://64.media.tumblr.com/ef038e0f975454f67e57632a84a3a26e/tumblr_ntnvadc3lK1smn4pqo1_1280.png
bg = pygame.image.load('images/background.png')
screen.blit(bg, (0,0))

#updates the window
def gameScreen():
    pygame.display.update()

# credit: coding with russ, adding buttons on youtube (changed it to my needs)
class Button:
    def __init__(self, x, y, image, ind, scale = 1, player = 0):
        w = image.get_width()
        h = image.get_height()
        self.image = pygame.transform.scale(image, (int(w*scale), int(h*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.ind = ind

    def draw(self):
        # gets mosue pos
        # can still keep  pressing and not press once as i csould with the falg
        pos = pygame.mouse.get_pos()
        screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.rect.collidepoint(pos):
            action = False
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                return action
    def getIndex(self):
        return self.ind
    def getPlayer(self):
        return player
#loading all cards

cardsPics = [pygame.image.load('cards_png/red_0.png').convert_alpha(), pygame.image.load('cards_png/red_1.png').convert_alpha(), pygame.image.load('cards_png/red_2.png').convert_alpha(),
pygame.image.load('cards_png/red_3.png').convert_alpha(), pygame.image.load('cards_png/red_4.png').convert_alpha(), pygame.image.load('cards_png/red_5.png').convert_alpha(),
pygame.image.load('cards_png/red_6.png').convert_alpha(), pygame.image.load('cards_png/red_7.png').convert_alpha(), pygame.image.load('cards_png/red_8.png').convert_alpha(),
pygame.image.load('cards_png/red_9.png').convert_alpha(), pygame.image.load('cards_png/red_reverse.png').convert_alpha(), pygame.image.load('cards_png/red_skip.png').convert_alpha(),
pygame.image.load('cards_png/red_Draw 2.png').convert_alpha(), pygame.image.load('cards_png/red_show me.png').convert_alpha(), pygame.image.load('cards_png/yellow_0.png').convert_alpha(),
pygame.image.load('cards_png/yellow_1.png').convert_alpha(), pygame.image.load('cards_png/yellow_2.png').convert_alpha(), pygame.image.load('cards_png/yellow_3.png').convert_alpha(),
pygame.image.load('cards_png/yellow_4.png').convert_alpha(), pygame.image.load('cards_png/yellow_5.png').convert_alpha(), pygame.image.load('cards_png/yellow_6.png').convert_alpha(),
pygame.image.load('cards_png/yellow_7.png').convert_alpha(), pygame.image.load('cards_png/yellow_8.png').convert_alpha(), pygame.image.load('cards_png/yellow_9.png').convert_alpha(),
pygame.image.load('cards_png/yellow_reverse.png').convert_alpha(), pygame.image.load('cards_png/yellow_skip.png'), pygame.image.load('cards_png/yellow_Draw 2.png').convert_alpha(),
pygame.image.load('cards_png/yellow_show me.png').convert_alpha(),pygame.image.load('cards_png/blue_0.png').convert_alpha(), pygame.image.load('cards_png/blue_1.png').convert_alpha(),
pygame.image.load('cards_png/blue_2.png').convert_alpha(), pygame.image.load('cards_png/blue_3.png').convert_alpha(), pygame.image.load('cards_png/blue_4.png').convert_alpha(),
pygame.image.load('cards_png/blue_5.png').convert_alpha(), pygame.image.load('cards_png/blue_6.png').convert_alpha(), pygame.image.load('cards_png/blue_7.png').convert_alpha(),
pygame.image.load('cards_png/blue_8.png').convert_alpha(), pygame.image.load('cards_png/blue_9.png').convert_alpha(), pygame.image.load('cards_png/blue_reverse.png').convert_alpha(),
pygame.image.load('cards_png/blue_skip.png').convert_alpha(), pygame.image.load('cards_png/blue_Draw 2.png').convert_alpha(), pygame.image.load('cards_png/blue_show me.png').convert_alpha(),
pygame.image.load('cards_png/green_0.png').convert_alpha(), pygame.image.load('cards_png/green_1.png').convert_alpha(), pygame.image.load('cards_png/green_2.png').convert_alpha(),
pygame.image.load('cards_png/green_3.png').convert_alpha(), pygame.image.load('cards_png/green_4.png').convert_alpha(), pygame.image.load('cards_png/green_5.png').convert_alpha(),
pygame.image.load('cards_png/green_6.png').convert_alpha(),pygame.image.load('cards_png/green_7.png').convert_alpha(), pygame.image.load('cards_png/green_8.png').convert_alpha(),
pygame.image.load('cards_png/green_9.png').convert_alpha(), pygame.image.load('cards_png/green_reverse.png').convert_alpha(), pygame.image.load('cards_png/green_skip.png').convert_alpha(),
pygame.image.load('cards_png/green_Draw 2.png').convert_alpha(), pygame.image.load('cards_png/green_show me.png').convert_alpha()]

specialCards = [pygame.image.load('cards_png/_Draw 4.png').convert_alpha(), pygame.image.load('cards_png/_wild.png').convert_alpha(), pygame.image.load('cards_png/_no.png').convert_alpha(),
pygame.image.load('cards_png/_swap.png').convert_alpha(), pygame.image.load('cards_png/red_wild.png'),pygame.image.load('cards_png/yellow_wild.png'), pygame.image.load('cards_png/blue_wild.png'),
 pygame.image.load('cards_png/green_wild.png')]

cardsD = {'red_0': cardsPics[0], 'red_1': cardsPics[1], 'red_2': cardsPics[2],'red_3': cardsPics[3], 
'red_4': cardsPics[4], 'red_5': cardsPics[5], 'red_6': cardsPics[6], 'red_7': cardsPics[7], 
'red_8': cardsPics[8], 'red_9': cardsPics[9], 'red_reverse': cardsPics[10], 'red_skip': cardsPics[11], 
'red_Draw 2': cardsPics[12], 'red_show me': cardsPics[13], 'yellow_0': cardsPics[14], 'yellow_1': cardsPics[15], 
'yellow_2': cardsPics[16], 'yellow_3': cardsPics[17], 'yellow_4': cardsPics[18], 'yellow_5': cardsPics[19],
'yellow_6': cardsPics[20], 'yellow_7': cardsPics[21], 'yellow_8': cardsPics[22], 'yellow_9': cardsPics[23],
'yellow_reverse': cardsPics[24],'yellow_skip': cardsPics[25], 'yellow_Draw 2': cardsPics[26], 'yellow_show me': cardsPics[27], 
'blue_0': cardsPics[28],'blue_1': cardsPics[29], 'blue_2': cardsPics[30], 'blue_3': cardsPics[31], 'blue_4': cardsPics[32], 
'blue_5': cardsPics[33],'blue_6': cardsPics[34], 'blue_7': cardsPics[35], 'blue_8': cardsPics[36], 'blue_9': cardsPics[37],
'blue_reverse': cardsPics[38], 'blue_skip': cardsPics[39], 'blue_Draw 2': cardsPics[40], 'blue_show me': cardsPics[41], 
'green_0': cardsPics[42], 'green_1': cardsPics[43], 'green_2': cardsPics[44], 'green_3': cardsPics[45], 'green_4': cardsPics[46], 
'green_5': cardsPics[47],'green_6': cardsPics[48],'green_7': cardsPics[49], 'green_8': cardsPics[50], 'green_9': cardsPics[51],
'green_reverse': cardsPics[52], 'green_skip': cardsPics[53], 'green_Draw 2': cardsPics[54], 'green_show me': cardsPics[55], 
'_Draw 4': specialCards[0], '_Wild': specialCards[1], '_no': specialCards[2], '_swap': specialCards[3], 'red_Wild':specialCards[4], 
"yellow_Wild":specialCards[5], "blue_Wild": specialCards[6], "green_Wild": specialCards[7]}

playersD = {"p1": pygame.image.load('images/p1.jpg').convert_alpha(), "p2" : pygame.image.load('images/p2.jpg').convert_alpha(), "p3": pygame.image.load('images/p3.jpg').convert_alpha(),
"p4" : pygame.image.load('images/p4.jpg').convert_alpha()}

colorsD = {"red": pygame.image.load('images/red.jpg').convert_alpha(), "blue" : pygame.image.load('images/blue.jpg').convert_alpha(), "yellow": pygame.image.load('images/yellow.jpg').convert_alpha(),
"green" : pygame.image.load('images/green.jpg').convert_alpha()}
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
        self.action = False
        self.ran = False
        self.draw
        self.player1But = None
        self.player2But = None
        self.player3But = None
        self.player4But = None
        self.drawColors= False
        self.color = ""
        for i in range (self.numOfPlayers) :
            self.lastCard.append(False)

        self.allPlayers = ["p1", "p2", "p3", "p4"][:self.numOfPlayers]
        #draw button
        self.drawButton = Button (10, 200, pygame.image.load('images/draw.png').convert_alpha(), 0, 0.3)
        # players as button in case of swap card


        #colors buttons
        self.redBut = Button(1100, 250, colorsD["red"], 0, 0.5 )
        self.blueBut = Button(1100, 150, colorsD["blue"], 0, 0.5 )
        self.greenBut = Button(1000, 250, colorsD["green"],0,  0.5 )
        self.yellowBut = Button(1000, 150, colorsD["yellow"],0, 0.5 )


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
    
    def playersButtons (self):
        index = 0
        x = 0
        currentp = 0
        playerNow = "p" + str(self.currentPlayer + 1)
        otherPlayers = self.allPlayers.copy()
        otherPlayers.remove(playerNow)
        center = (1300 - ((self.numOfPlayers-3) * 230) + 108) // 3 + self.numOfPlayers - 1
        
        for person in otherPlayers:
            
            btn = Button (center + x , 30, playersD[person], 0, 0.4, player = currentp)
            btn.draw()
            font = pygame.font.Font('freesansbold.ttf', 32)
            cardsNum = font.render((" " + str (len(self.playerList[currentp].cards)) + " "), True, pink, white)
            screen.blit(cardsNum, (center+x, 30 ))
            if currentp == 0:
                self.player1But = btn
            elif currentp == 1:
                self.player2But = btn
            elif currentp == 2:
                self.player3But = btn
            elif currentp == 3:
                self.player4But = btn
            x += 230
            index +=1
            currentp +=1
        return 1
        

    def tempFun(self):
        self.action = False
        flag = False
        validCard = False
        i = 0
        ind = 0
        screen.blit(cardsD[self.middleCard], (600, 200))
        center = (1300 - (len(self.playerList[self.currentPlayer].cards) * 80))//2
        self.playersButtons()
        
        if self.drawColors == True:
            font = pygame.font.Font('freesansbold.ttf', 35)
            text = font.render(("Pick a color!"), True, pink, white)
            screen.blit(text, (1000, 80 ))
            if self.redBut.draw():
                self.color = "red"
            if self.blueBut.draw():
                self.color = "blue"
            if self.yellowBut.draw():
                self.color = "yellow"
            if self.greenBut.draw():
                self.color = "green"
            

        # button to draw a card
        if self.drawButton.draw():
            screen.blit(bg, (0,0))
            self.drawCard()
            self.drawButton.clicked = False
            self.action = True
            self.playersButtons()
            return 1

        
        while (validCard == False):
            #makes players avatars as buttons 
            for card in self.playerList[self.currentPlayer].cards:
                btn = Button(center+i, 400, cardsD[card], ind)
                ind+=1
                i+=80
                if btn.draw() == True:
                    index = btn.getIndex()
                    flag = True
                #if the move is valid change the middle card and append it to the main deck
            if (flag == True) and self.isValidMove(self.playerList[self.currentPlayer].cards[index], index):
                print ("valid")
                self.middleCard = self.playerList[self.currentPlayer].cards[index]
                del self.playerList[self.currentPlayer].cards[index]
                self.deck.append(self.middleCard)
                screen.blit(bg, (0,0))
                self.action = True
                validCard == True               
                self.playersButtons()   
            elif (flag == True) and not self.isValidMove(self.playerList[self.currentPlayer].cards[index], index):
                print ("please make a vlaid move!")
            return 1  

        # reverses order
        if self.middleCard.split('_')[1] == 'reverse':
            if self.numOfPlayers > 2:
                self.direction *=-1
                return -1
            else:
                #skips if there are 2 players
                self.skip()

        #skips a player
        elif self.middleCard.split('_')[1] == 'skip':
            self.skip()

        # no u card reverses and changes order of draw
        elif self.middleCard.split('_')[1] == 'no u' and self.nou == False:
            self.nou = True
            self.direction *=-1
            return -1
        
        while self.middleCard.split('_')[1] == 'no u' and self.nou == True:
            self.direction *=-1
            return -1
        self.nou = False
        return 1
        

    # checks if plaeer made a valid move
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

        #player drawall card in darw count if they havent played a "no" card
        if (self.drawCount !=  0) and ('Draw' not in cardN) and ('no' not in cardN):
            self.draw()
            return False

        if (cardN == middleN or cardC == middleC):
            if cardN.isdigit() or cardN == 'skip' or cardN == 'reverse':
                return True

            elif cardN == 'show me':
                playerNums = []
                
                #de4lets th current player from the players nums list so they don't choose themselves
                for i in range (1, self.numOfPlayers+1):
                    playerNums.append(i)

                del playerNums[self.currentPlayer]

                if self.player1But.draw():
                    pNum = self.player1But.getPlayer()
                    print('say less:', self.playerList[pNum].cards)

                elif self.player2But.draw():
                    pNum = self.player2But.getPlayer()
                    print('say less:', self.playerList[pNum].cards)

                elif self.player3But != None and self.player3But.draw():
                    pNum = self.player3But.getPlayer()
                    print('say less:', self.playerList[pNum].cards)

                elif self.player4But != None and self.player4But.draw():
                    pNum = self.player4But.getPlayer()
                    print('say less:', self.playerList[pNum].cards)
                else:
                    return False
                return True

            if cardN == 'Draw 2':
                self.drawCount += 2
                return True
            
        elif cardN == 'Wild':
            self.redBut.draw()
            self.wild(i) 
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
            n = int(input("Enter the number of the player you want to swap cards with:\n"))
            self.swap(n)
            return True

    #choose color you want to change 
    def wild (self, i):
        self.drawColors = True
        #buttons for each color
        if self.redBut.draw():
            new = self.color + self.playerList[self.currentPlayer].cards[i]
            self.playerList[self.currentPlayer].cards[i] = new
        else:
            print("not working")
            return False
        # colors = ["red", "blue", "green", "yellow"]
        # color = int(input (('enter the index of the color you want ["red", "blue", "green", "yellow"]:\n')))
        
        


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


uno = UNO(3, deck())
uno.distribute()


#mainloop
run = True
while run:
    d = uno.tempFun()
    uno.playersButtons()
    if uno.action and not uno.won:
        direction = d * direction
        uno.currentPlayer +=direction
        if uno.currentPlayer  ==  uno.numOfPlayers:
            uno.currentPlayer = 0
    clock.tick(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    gameScreen()

pygame.quit()

#bugs: not accurate cards since my flag doesnt work when i press so it keeps pressing