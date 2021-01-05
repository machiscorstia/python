import random

class cardName:
    color = ['Azul', 'Rojo', 'Amarillo', 'Verde']

class Card:
    def __init__(self, number, color):
        self.number = number
        self.color = color
        self.visibility = False

    def name(self):
        print(cardName.color[self.color] + self.number)
    
class Player:
    def __init__(self, name):
        self.name = name
        self.turn = False
        self.__cards = []

    def viewCards(self):
        i = 0
        for card in self.__cards:
            print(f'{i}: {card.name}')
            i += 1
        
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
        self.targetPlayer = None
        self.currentCard = 0
        self.__cards = []
        self.__players = []
        self.__accum = 0
    
    def getPlayers(self):
        for player in self.__players:
            print(f'{player.name}')
        
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
        return self.__cards[random.randint(0, len(self.__cards) - 1)]

    def setCurrentCard(self):
        targetCard = self.getRandomCard()
        self.removeCard(targetCard)
        self.currentCard = targetCard

    def giveStartCards(self):
        for player in self.__players:
            i = 0
            while i < 4:
                card = self.getRandomCard()
                self.removeCard(card)
                player.takeCard(card)
                i += 1
    
    def nextTurn(self):
        pass

    def setStartTurn(self):
        print(len(self.__players) - 1)
        rnd = random.randint(0, len(self.__players) - 1)
        self.targetPlayer = self.__players[rnd]
        self.targetPlayer.turn = True

mainBoard = Board()
maxPlayers = int(input('Cantidad de jugadores: '))

print(f"Configurando la partida para {maxPlayers} jugadores.")
mainBoard.createPlayers(maxPlayers)

print(f"\nConfigurando el tablero..")
mainBoard.createCards()
mainBoard.setCurrentCard()
mainBoard.giveStartCards()
mainBoard.setStartTurn()

inGame = True
while inGame:
    player = mainBoard.targetPlayer
    currentCard = mainBoard.currentCard
    print(f'Turno del jugador {player.name} \n')
    print('Carta actual: ', currentCard)
    player.viewCards()
    temp = input()

    
    

