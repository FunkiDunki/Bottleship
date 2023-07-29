def print_board(board):

    for i in range(board["y"]):
        buff = chr(64 + board["y"] - i)
        buff += '   '
        for j in range(board["x"]):
            buff += '.' + '  '

        print(buff)
    print()
    buff = '    '
    for i in range(board["x"]):
        buff += str(i) + '  '
    print(buff)


board = {
    "x": 10,
    "y":10,
}

print_board(board)