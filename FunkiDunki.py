from utils import *

class FunkiDunki (Player):
    def __init__(self, size: int):
        self.oppo = Board(size)
        self.size = size
        self.myboard = Board(size)
        self.ships = []
        self.t = 0

    def place_ships(self, sizes: list[int]):
        dirs = [[1,0], [0,1]]
        posits = []
        for i in range(self.size):
            for j in range(self.size):
                posits.append([i,j])
        for si in sizes:
            found = False
            for pos in posits:
                for dir in dirs:
                    sh = Ship(si, pos, dir)
                    li = self.ships.copy()
                    li.append(sh)
                    if self.myboard.check_ship_list(li):
                        self.ships.append(sh)
                        found = True
                        break
                if found:
                    break
        return(self.ships)

    def make_play(self):
        play = [self.t%self.size, self.t//self.size]
        self.t+= 1
        return play

    def opponent_play(self, play: tuple[int, int]):
        pass

    def turn_feedback(self, play: tuple[int, int], hit: bool, sink: bool):
        pass