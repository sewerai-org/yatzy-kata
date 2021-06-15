
from .categories import CATEGORIES


class Player:

    def __init__(self, position):
        self.position = position
        self.points = 0
        self.categories = {
            field: False for field in CATEGORIES._fields
        }


class YatzyGame:

    def __init__(self, num_players):
        self.players = [Player(i+1) for i in range(num_players)]

    def start(self):
        # play game
        pass
