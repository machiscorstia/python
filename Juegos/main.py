import random

class Card:
    def __init__(self, number, color):
        self.__number = number
        self.__color = color
        self.__visibility = False
    
class Player:
    def __init__(self, name):
        self.name = name
        self.turn = False
        self.__cards = []

    def getCards(self):
        return len(self.__cards)

    def removeCard(self, card):
        self.__cards.remove(card)
    
    def takeCard(self, card):
        self.__cards.append(card)

    def throwCard(self, card):
        self.removeCard(card)
        return card

class Board:
    def __init__(self):
        self.__cards = []
        self.__players = []
        self.__accum = 0
        self.__currentCard = None
        
    def createCards(self):
        for color in range(0, 4):
            for number in range(0, 10):
                self.addCard(Card(number, color))
    
    def createPlayers(self, max):
        i = 0
        while i < max:
            tempName = str(input(f'Ingrese nombre del {i + 1} jugador: '))
            self.addPlayer(Player(tempName))
            i += 1
    
    def addCard(self, card):
        self.__cards.append(Card)

    def removeCard(self, card):
        self.__cards.remove(card)
    
    def addPlayer(self, player):
        self.__players.append(player)
        #print('\033[92m' + 'Jugador agregado correctamente' + '\033[0m')
    
    def getRandomCard(self):
        return self.__cards[random.randint(0, len(self.__cards))]

    def giveStartCards(self):
        for player in self.__players:
            i = 0
            while i < 4:
                card = self.getRandomCard()
                self.removeCard(card)
                player.takeCard(card)
                i += 1
    
    def setTurn(self):
        self.__players[random.randint(0, len(self.__players))].turn = True

mainBoard = Board()
maxPlayers = int(input('Cantidad de jugadores: '))

print(f"Configurando la partida para {maxPlayers} jugadores.")
mainBoard.createPlayers(maxPlayers)

print(f"\nConfigurando cartas..")
mainBoard.createCards()
mainBoard.giveStartCards()


