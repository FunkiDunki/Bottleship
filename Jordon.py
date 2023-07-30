from typing import Tuple
from utils import Player, Board, Ship


class JordonBot(Player):
    def __init__(self, size: int):
        super().__init__(size)
        self.myboard = Board(size)
        self.opponentboard = Board(size)
        self.ships = []

    def place_ships(self, sizes: list[int]):
            self.ships = sizes;

    def make_play(self):
         pass
    
    def opponent_play(self, play: Tuple[int, int]):
        pass
    
    def turn_feedback(self, play: Tuple[int, int], hit: bool, sink: bool):
        return super().turn_feedback(play, hit, sink)
    