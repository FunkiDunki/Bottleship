

#runs a game between two players. The id of the winner is returned at the end. -1 for failure
def RunGame() -> bool:
    #TODO:setup board:
    p1_board = None
    p2_board = None

    #TODO:setup players:
    player_1 = None
    player_2 = None
    turn = 0 #turn parity determines which player's turn it is

    #TODO:players place their pieces
    sizes = [2, 3, 4, 5]
    p1_ships = player_1.PlaceShips(sizes)
    p2_ships = player_2.PlaceShips(sizes)
    if not p1_board.PlaceShips(p1_ships) or not p2_board.PlaceShips(p2_ships):
        #the placements were not valid:
        print(p1_ships)
        print(p2_ships)
        return -1

    #TODO:main loop, ends when the board detects a win:
    while not p1_board.Sunk() and not p2_board.Sunk():
        #it is player_1's turn
        if turn % 2 == 0:
            hit = True
            while hit:
                play = player_1.MakePlay() #ask the player to make a play
                if not p2_board.IsValid(play):
                    continue #if the play is not a good play, ask the player to make another play
                player_2.OpponentPlays(play) #tell the opponent what play was made
                hit = p2_board.IsHit(play) #check if the play is a hit
                player_1.TurnFeedback(play, hit)#tell the player if they made a hit or not with the play
                p2_board.MakePlay(play)#make the play on the board

        #it is player_2's turn
        else:
            hit = True
            while hit:
                play = player_2.MakePlay() #ask the player to make a play
                if not p1_board.IsValid(play):
                    continue #if the play is not a good play, ask the player to make another play
                player_1.OpponentPlays(play) #tell the opponent what play was made
                hit = p1_board.IsHit(play) #check if the play is a hit
                player_2.TurnFeedback(play, hit)#tell the player if they made a hit or not with the play
                p1_board.MakePlay(play)#make the play on the board

        turn += 1 #it is now the next turn
        break

    #TODO:end of game tasks
    return