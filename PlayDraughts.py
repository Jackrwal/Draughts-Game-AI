from Draughts.Game import Game
from Draughts.Player import Player

def getPieceDisplayChar(string):

    if string[0] == 'W':
        if string[1] == 'm':
            return 'o'
        else:
            return 'O'
    else:
        if string[1] == 'm':
            return 'x'
        else:
            return 'X'

def displayGameToConsole(game):
    stateString = game.getStateString()
    #print(stateString)
    logging = False

    print('/-----------------\\')
    for i in range(0, 10):
        line = "| "

        for j in range(0, 10):
            boardIndex = (i * 10 + j) + 1

            # for Even Rows
            if i % 2 == 0:

                # Even squares are empty
                if j % 2 == 0:
                    line += "  "
                    if logging: print("i: %s, j:%s, board: %s, Line: %s" % (i, j, boardIndex, line))

                else:
                    pieceIndex = int((5*i + (j/2)) + 1)

                    if stateString[pieceIndex - 1] == "-1":
                        line += "-"

                    else:
                        line +=  getPieceDisplayChar(stateString[pieceIndex - 1])

                    if logging: print("i: %s, j:%s, board: %s, piece: %s,  stateString: %s, line: %s" % (i, j, boardIndex, pieceIndex, stateString[pieceIndex - 1], line))

            # For Odd Rows
            else:

                # Odd rows are empty
                if j % 2 != 0:
                    line += "  "
                    if logging: print("i: %s, j:%s, board: %s, Line: %s" % (i, j, boardIndex, line))

                else:
                    pieceIndex = int((5 * i + (j / 2)) + 1)

                    if stateString[pieceIndex - 1] == "-1":
                        line += "-"

                    else:
                        line += getPieceDisplayChar(stateString[pieceIndex - 1])

                    if logging: print("i: %s, j:%s, board: %s, piece: %s,  stateString: %s, line: %s" % (i, j, boardIndex, pieceIndex, stateString[pieceIndex - 1], line))

        print(line + " |")
    print('\\-----------------/')


# end function

player1 = Player("Player One", "W")
player2 = Player("Player Two", "B")

game = Game(player1, player2)

while not game.getGameOver():
    displayGameToConsole(game)

    move = player1.getMove(game)

    if move == "q":
        game.endGame()
    else:
        game.makeMove(move)


