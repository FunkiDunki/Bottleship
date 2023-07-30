from utils import Board, Ship
from FunkiDunki import FunkiDunki
import time



#runs a game between two players. The id of the winner is returned at the end. -1 for failure
def RunGame() -> bool:
    size = 8
    #TODO:setup board:
    p1_board = Board(size)
    p2_board = Board(size)

    #TODO:setup players:
    player_1 = FunkiDunki(size)
    player_2 = FunkiDunki(size)
    turn = 0 #turn parity determines which player's turn it is

    #TODO:players place their pieces
    sizes = [2, 3, 4, 5]
    p1_ships = player_1.place_ships(sizes)
    p2_ships = player_2.place_ships(sizes)
    if not p1_board.place_ships(p1_ships) or not p2_board.place_ships(p2_ships):
        #the placements were not valid:
        print(p1_ships)
        print(p2_ships)
        return -1

    print(p1_board)
    print(p2_board)
    #TODO:main loop, ends when the board detects a win:
    while not p1_board.sunk() and not p2_board.sunk():
        time.sleep(0.5)
        #it is player_1's turn
        if turn % 2 == 0:
            hit = True
            while hit:
                play = player_1.make_play() #ask the player to make a play
                if not p2_board.is_valid_guess(play):
                    continue #if the play is not a good play, ask the player to make another play
                player_2.opponent_play(play) #tell the opponent what play was made
                hit = p2_board.is_hit(play) #check if the play is a hit
                sink = p2_board.make_play(play)#make the play on the board, check if it sunk a ship
                player_1.turn_feedback(play, hit, sink)#tell the player if they made a hit or not with the play

        #it is player_2's turn
        else:
            hit = True
            while hit:
                play = player_2.make_play() #ask the player to make a play
                if not p1_board.is_valid_guess(play):
                    continue #if the play is not a good play, ask the player to make another play
                player_1.opponent_play(play) #tell the opponent what play was made
                hit = p1_board.is_hit(play) #check if the play is a hit
                sink = p1_board.make_play(play)#make the play on the board, check if it sunk a ship
                player_2.turn_feedback(play, hit, sink)#tell the player if they made a hit or not with the play

        print(p1_board)
        print(p2_board)
        turn += 1 #it is now the next turn

    #TODO:end of game tasks
    return

if __name__ == "__main__":
    RunGame()