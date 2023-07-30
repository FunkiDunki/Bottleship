from utils import Ship, Board, Player
from typing import Tuple, List
import math


class GuessBoard:
    #dirs = [(int(math.cos(math.pi/2*i)), int(math.sin(math.pi/2*i))) for i in range(4)]
    def __init__(self, size):
        self.size = size
        self.sqaures = [[1 for i in range(size)] for j in range(size)]
    
    def set_ships(self, ships: List[int]):
        self.ships = ships
    
    def hit(self, pt):
        self.set_pt(pt, -1)

    def miss(self, pt):
        self.set_pt(pt,0)

    def set_pt(self, pt, val):
        self.sqaures[pt[0]][pt[1]] = val
    
    def get_pt(self,pt):
        return self.sqaures[pt[0]][pt[1]]
    
    def possible(self):
        possible = [[0 for i in range(self.size)] for j in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                if self.get_pt((i,j)) != 1:
                    continue
        


class StatPlayer(Player):
    
    def __init__(self, size):
        self.board = GuessBoard(size)

    def place_ships(self, sizes: List[int]) -> List[Ship]:
        pass

    def make_play() -> Tuple[int,int]:
        pass

    def opponent_play(play: Tuple[int, int]):
        pass

    def turn_feedback(play: Tuple[int, int], hit: bool, sink: bool):
        pass

