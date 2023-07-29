from utils import Ship, Board, Player
from typing import Tuple, List



class StatPlayer(Player):
    
    

    def place_ships(self, sizes: List[int]) -> List[Ship]:
        pass

    def make_play() -> Tuple[int,int]:
        pass

    def opponent_play(play: Tuple[int, int]):
        pass

    def turn_feedback(play: Tuple[int, int], hit: bool, sink: bool):
        pass