from typing import List

class Ship:
    def __init__(self, length: int, start: tuple, dir:tuple):
        self.length = length
        self.points = [(start[0]+dir[0]*i, start[1]+dir[1]*i)for i in range(length)]
    
    def check_hit(self, pt: tuple) -> bool:
        for p in self.points:
            if(p == pt):
                return True
        return False
    

class Board:
    def __init__(self, size: int):
        self.squares = [[1 for i in range(size)] for j in range(size)]
        self.ships: List[ships] = []
        self.sunkships = []

    def add_ships(self, ships: List[Ship]) -> bool:
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
            

    def is_valid_guess(self, guess: tuple) -> bool:
        if not self.is_pt(guess):
            return False
        val = self.squares[guess[0]][guess[1]]
        return val>0
    
    def is_pt(self, pt: tuple) -> bool:
        return pt[0] >= 0 and pt[0] < self.size and pt[1] >= 0 and pt[1] < self.size

    def sunk(self) -> bool:
        for b in self.sunkships:
            if not b:
                return False
        return True
    
    def is_hit(self, guess) -> bool:
        assert self.is_pt(guess)
        for ship in ships:
            for pt in ship.points:
                if guess == pt:
                    return True
        return False

    def is_sunk(self, guess) -> bool:
        assert self.is_pt(guess)
        index = abs(self.squares[guess[0]][guess[1]])-2
        if index == -1:
            return False
        ship: Ship = self.ships[index]
        for pt in ship.points:
            if self.squares(pt[0], pt[1])>1:
                return False
        return True


    def make_play(self, guess) -> bool:
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
    for i in range(len(board.squares)):
        buff += chr(64 + len(board.squares) - i)
        buff += '   '
        for j in range(len(board.squares)):
            addchar = (board.squares[i][j])
            addchar = str(addchar) if addchar != 1 else "."
            buff += addchar + '  '

        buff += "\n"
    buff += "\n"
    buff += '    '
    for i in range(len(board.squares)):
        buff += str(i) + '  '
    return buff



if __name__ == "__main__":
    board = Board(10)

    ships = [
        Ship(3, (3,3), (1,0))
    ]

    board.add_ships(ships)
    
    print(board)
