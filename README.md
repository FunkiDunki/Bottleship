# Bottleship
 Battleship for bots

## Reqs for Board class
 __init__(size: int): fills board of that size
 PlaceShips(ships: [s1, s2, s3...]): takes list of ships and places them. returns False if non-valid
 Sunk(): returns True if all ships on board are sunk, returns False otherwise
 IsValid(pos: [x, y]): returns True if the position represents a valid play, False otherwise
 IsHit(pos: [x, y]): returns True if the position would represent a hit on the board, False otherwise
 MakePlay(play: [x, y]): makes a play at x, y

## Reqs for Ship class
__init__(length: int, start: tuple, dir: tuple)
points: list of tuple points that the ship occupies

## Reqs for Player Class
 __init__(size: int): inits for a certain board size
 PlaceShips(sizes: List[int]): creates ships to place on the board of certain sizes and returns them
 MakePlay(): returns a play as a position [x, y]
 OpponentPlay(play): takes information about the opponent's turn, no action necessary
 TurnFeedback(play, hit, sink): recieve info about your own play, hit and sink are bools for info about the play
 