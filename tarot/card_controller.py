import TarotCard
import random
class CardController:
    
    def __init__(self):
        self.deck = []
    
    def createDeck(self):
        id = 0
        TC = TarotCard
        for i in range(1,14 + 1):
            for j in TC.Suit:
                card = TC.MinorArcana(j, i, id)
                self.deck.append(card)
                print(card)
                id += 1
        
        for i in range(21):
            card = TC.MajorArcana(i)
            print(card)
            self.deck.append(card)
            
        return self.deck
    
    #TODO: add shuffle deck and draw deck

CC = CardController()
CC.createDeck()