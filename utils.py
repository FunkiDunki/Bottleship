from typing import List, Tuple
from abc import ABC, abstractmethod


class Player(ABC):

    @abstractmethod
    def place_ships(sizes: List[int]):
        pass

    @abstractmethod
    def make_play():
        pass

    @abstractmethod
    def opponent_play(play: Tuple[int, int]):
        pass

    @abstractmethod
    def turn_feedback(play: Tuple[int, int], hit: bool, sink: bool):
        pass

class Ship:
    def __init__(self, length: int, start: Tuple[int,int], dir:Tuple[int,int]):
        self.length = length
        self.points = [(start[0]+dir[0]*i, start[1]+dir[1]*i)for i in range(length)]
    
    def check_hit(self, pt: Tuple[int,int]) -> bool:
        for p in self.points:
            if(p == pt):
                return True
        return False
    

class Board:
    def __init__(self, size: int):
        self.squares = [[1 for i in range(size)] for j in range(size)]
        self.ships: List[ships] = []
        self.sunkships = []
        self.size = size

    def place_ships(self, ships: List[Ship]) -> bool:
        if not self.check_ship_list(ships):
            return False
        for ship in ships:
            val = len(self.ships)+2
            self.ships.append(ship)
            self.sunkships.append(False)
            for pt in ship.points:
                self.squares[pt[0]][pt[1]] = val
        return True


    def check_ship_list(self, ships: List[Ship]) -> bool:
        for i, ship in enumerate(ships):
            for p1 in ship.points:
                    if not self.is_pt(p1):
                        return False
            for j,ship2 in enumerate(ships):
                if(i==j):
                    continue
                for p1 in ship.points:
                    if not self.is_pt(p1):
                        return False
                    for p2 in ship2.points:
                        if p1 == p2:
                            return False
        return True
            

    def is_valid_guess(self, guess: Tuple[int,int]) -> bool:
        if not self.is_pt(guess):
            return False
        val = self.squares[guess[0]][guess[1]]
        return val>0
    
    def is_pt(self, pt: Tuple[int,int]) -> bool:
        return pt[0] >= 0 and pt[0] < self.size and pt[1] >= 0 and pt[1] < self.size

    def sunk(self) -> bool:
        for b in self.sunkships:
            if not b:
                return False
        return True
    
    def is_hit(self, guess: Tuple[int,int]) -> bool:
        assert self.is_pt(guess)
        for ship in self.ships:
            for pt in ship.points:
                if guess == pt:
                    return True
        return False

    def is_sunk(self, guess:Tuple[int,int]) -> bool:
        assert self.is_pt(guess)
        index = abs(self.squares[guess[0]][guess[1]])-2
        if index == -1:
            return False
        ship: Ship = self.ships[index]
        for pt in ship.points:
            if self.squares[pt[0]][pt[1]]>1:
                return False
        return True


    def make_play(self, guess: Tuple[int,int]) -> bool:
        assert self.is_valid_guess(guess)
        index = abs(self.squares[guess[0]][guess[1]])-2
        self.squares[guess[0]][guess[1]] *= -1
        if(self.is_sunk(guess)):
            self.sunkships[index] = True
            return True
        return False

    def __str__(self):
        return print_board(self)

def print_board(board: Board):
    buff = ""
    
    buff += '    '
    for i in range(len(board.squares)):
        buff += str(i) + '  '
    buff += "\n"
    for i in range(len(board.squares)):
        buff += chr(65 + i)
        buff += '   '
        for j in range(len(board.squares)):
            addchar = board.squares[j][i]
            if addchar == 1:
                addchar = '.'
            elif addchar == -1:
                addchar = 'O'
            elif addchar < 0:
                addchar = 'X'
            else:
                addchar = str(addchar)
            buff += addchar + '  '
        buff += "\n"
    return buff



if __name__ == "__main__":
    board = Board(10)

    ships = [
        Ship(3, (3,3), (1,0))
    ]

    board.place_ships(ships)
    
    print(board)
