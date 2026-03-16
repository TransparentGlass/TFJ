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
    

class MinorArcana:
    def __init__(self, suit: Suit, rank: CourtRank, card_id: int, path):
        self._rank = rank
        self._suit = suit
        self.id = card_id
        self.front = path
        
    def __repr__(self):
        return f"Minor arcana card: ${self._rank} of ${self._suit} id = ${self.id}"
    
    @property
    def card_id(self) -> int:
        return self.id

class MajorArcana:
    def __init__(self, index: int, name: str, path):
        self.index = index
        self.name = name
        self.front = path
        
    def __repr__(self):
        return f"Major Arcana Card(index = {self.index}, name = '{self.name}')"
    
    @property
    def getIndex(self):
        return self.index
                