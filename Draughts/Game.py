from Draughts.Piece import Piece


class Game:

    # static methods

    @staticmethod
    def __getStartStateString():
        #  W - White
        #  B - Black
        #  m - Man
        #  B - King
        # -1 - Empty
        return [
            "Bm", "Bm", "Bm", "Bm", "Bm",
            "Bm", "Bm", "Bm", "Bm", "Bm",
            "Bm", "Bm", "Bm", "Bm", "Bm",
            "Bm", "Bm", "Bm", "Bm", "Bm",
            "-1", "-1", "-1", "-1", "-1",
            "-1", "-1", "-1", "-1", "-1",
            "Wm", "Wm", "Wm", "Wm", "Wm",
            "Wm", "Wm", "Wm", "Wm", "Wm",
            "Wm", "Wm", "Wm", "Wm", "Wm",
            "Wm", "Wm", "Wm", "Wm", "Wm",
        ]

    # attributes

    __player1 = object
    __player2 = object
    __gameOver = False
    __gameWon = False

    __pieces = {}

    # constructor

    def __init__(self, player1, player2):

        self.__player1 = player1
        self.__player2 = player2

        self.__pieces = self.__buildPieceListFromStringArray(Game.__getStartStateString())

        # self.__showPieces()

    # methods

    # TODO: Check move is valid and implement taking
    # Updates the state of the game by carrying out a given move if the move is valid
    def makeMove(self, move):
        piece = move.getPiece()

        if piece is None:
            print("no piece found at this position")
            return

        # remove the piece from the board
        self.__pieces.pop(str(piece.getPosition()))

        # place the piece at the target
        self.__pieces[move.getTarget()] = piece

        # update the pieces internal position
        self.__pieces[move.getTarget()].setPosition(move.getTarget())

    def endGame(self):
        self.__gameOver = True

    # getters setters

    def getPlayerOne(self):
        return self.__player1

    def getPlayerTwo(self):
        return self.__player2

    def getGameWon(self):
        return self.__gameOver

    def getGameOver(self):
        return self.__gameOver

    def getStateString(self):

        if len(self.__pieces) == 0:
            return

        stateStringArray = []

        # create an empty board
        for i in range(0, 50):
            stateStringArray.append("-1")

        # put the pieces on the board. The Keys to the pieces dictionary is the coordinate of the piece
        ps = self.__pieces
        for coord in ps:
            stateStringArray[int(coord) - 1] = "%s%s" % (ps[coord].getAllegiance(), ps[coord].getPieceState())

        return stateStringArray

    def getWinner(self):

        if not self.getGameWon():
            return None

        return self.getPlayerOne() if self.__player1.getScore() > self.__player2.getScore() else self.getPlayerOne

    def getPiece(self, coordinate):
        if not coordinate in self.__pieces.keys():
            return None

        return self.__pieces[str(coordinate)]

    # private functions
    def __buildPieceListFromStringArray(self, stringArray):

        pieces = {}

        # Build a list of pieces on the bord from the string array representation
        for i in range(0, len(stringArray)):

            # If there is a piece in this place add it to the list

            if stringArray[i] != "-1":
                pieces[str(i + 1)] = Piece("%s:%s" % (stringArray[i], i + 1))

        return pieces

    def __showPieces(self):

        line = ""
        ps = self.__pieces
        for k in ps:
            line += " %s%s:%s" % (ps[k].getAllegiance(), ps[k].getPieceState(), k)

        print(line)

#    def checkMoveValid(self, move):
#
#        # If there are any possible captures, the player must take them.
#        # This is done first as if their move is not in this list it is irrelevant
#        # TODO Check every piece the player has for a list of available captures
#
#        # There is no piece at this coord
#        if move.getPiece() is None:
#            return False
#
#        # The Player who made the move does not own the piece
#        if move.getPlayer().getFaction() != move.getPiece().getAllegiance():
#            return False
#
#        # The Target is not Empty
#
#        # If the
#
#        return True
