# Bottleship
 Battleship for bots

## Reqs for Board class
 __init_\_(size: int): fills board of that size
 place_ships(ships: [s1, s2, s3...]): takes list of ships and places them. returns False if non-valid
 sunk(): returns True if all ships on board are sunk, returns False otherwise
 is_valid_guess(pos: [x, y]): returns True if the position represents a valid play, False otherwise
 is_hit(pos: [x, y]): returns True if the position would represent a hit on the board, False otherwise
 make_play(play: [x, y]): makes a play at x, y, returns True if the ship it hit was sunk, returns False otherwise

## Reqs for Ship class
 __init_\_(length: int, start: tuple, dir: tuple)
 points: list of tuple points that the ship occupies

## Reqs for Player Class
 __init_\_(size: int): inits for a certain board size
 place_ships(sizes: List[int]): creates ships to place on the board of certain sizes and returns them
 make_play(): returns a play as a position [x, y]
 opponent_play(play): takes information about the opponent's turn, no action necessary
 turn_feedback(play, hit, sink): recieve info about your own play, hit and sink are bools for info about the play
