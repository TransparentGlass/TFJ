from enum import Enum, auto
class Suit(Enum):
        WANDS = auto()
        CUPS = auto()
        SWORDS = auto()
        PENTACLES = auto()
        
class CourtRank(Enum):
    PAGE = 11
    KNIGHT = 12
    QUEEN = 13
    KING = 14
    ACE = 1
    

class MinorArcana:
    def __init__(self, suit: Suit, rank: CourtRank, card_id: int, path = None):
        self._rank = rank
        self._suit = suit
        self.id = card_id
        self.front = path
        
    def __repr__(self):
        return f"Minor arcana card: {self._rank} of {self._suit.name} id = {self.id}"
    
    @property
    def card_id(self) -> int:
        return self.id

class MajorArcana:
    NAMES = [
        "The Fool", "The Magician", "The High Priestess", "The Empress", 
        "The Emperor", "The Hierophant", "The Lovers", "The Chariot", 
        "Strength", "The Hermit", "Wheel of Fortune", "Justice", 
        "The Hanged Man", "Death", "Temperance", "The Devil", 
        "The Tower", "The Star", "The Moon", "The Sun", 
        "Judgement", "The World"
    ]
    def __init__(self, index: int, path = None):
        self.index = index
        self.name = self.NAMES[index]
        self.front = path
        
    def __repr__(self):
        return f"Major Arcana Card(index = {self.index}, name = '{self.name}')"
    
    @property
    def getIndex(self):
        return self.index
                