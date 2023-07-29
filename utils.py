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
        self.ships = []

    def add_ships(self, ships: List[Ship]) -> bool:
        if not self.check_ship_list(ships):
            return False
        for ship in ships:
            self.ships.append(ship)
        return True


    def check_ship_list(self, ships: List[Ship]) -> bool:
        for i, ship in enumerate(ships):
            for j,ship2 in enumerate(ships):
                if(i==j):
                    continue
                for p1 in ship.points:
                    for p2 in ship2.points:
                        if p1 == p2:
                            return False
        return True
            

    def is_valid(self, guess: tuple) -> bool:
        if guess[0] < 0 or guess[0] >= self.size or guess[1] < 0 or guess[1] >= self.size:
            return False
        val = self.squares[guess[0],guess[1]]
        return val>0

def print_board(board):

    for i in range(len(board.squares)):
        buff = chr(64 + len(board.squares) - i)
        buff += '   '
        for j in range(len(board.squares)):
            buff += str(board.squares[i][j]) + '  '

        print(buff)
    print()
    buff = '    '
    for i in range(len(board.squares)):
        buff += str(i) + '  '
    print(buff)


board = Board(10)

ships = [
    Ship(3, (3,3), (1,0))
]

board.add_ships(ships)
print_board(board)
