from Draughts.Piece import Piece
import logging

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

    @staticmethod
    def __buildPieceListFromStringArray(stringArray):

        pieces = {}

        # Build a list of pieces on the bord from the string array representation
        for i in range(0, len(stringArray)):

            # If there is a piece in this place add it to the list

            if stringArray[i] != "-1":
                pieces[str(i + 1)] = Piece("%s:%s" % (stringArray[i], i + 1))

        return pieces

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

        self.__pieces = Game.__buildPieceListFromStringArray(Game.__getStartStateString())

        # self.__showPieces()

    # methods

    # TODO later i will probably implement a 'get valid moves' method for a given Piece
    #  This will later allow the user to highlight a piece in the GUI and get a list of valid moves

    # Updates the state of the game by carrying out a given move if the move is valid
    def makeMove(self, move):

        # If the move the user has given is not a valid move return
        if not self.checkMoveValid(move):
            return

        piece = move.getPiece()
        target = int(move.getTarget())

        # remove the piece from the board
        self.__pieces.pop(str(piece.getPosition()))

        # place the piece at the target
        self.__pieces[move.getTarget()] = piece

        # update the pieces internal position
        self.__pieces[move.getTarget()].setPosition(target)

    def checkMoveValid(self, move):

        # If there are any possible captures, the player must take them.
        # This is done first as if their move is not in this list it is irrelevant
        # TODO Check every piece the player has for a list of available captures
        # TODO: When we have this list of captures, the player must choose one which leads to the highest score
        #  (LiDraughts forces you to this, but i think it could be more interesting to let the AI learn this)

        # Kings can move, and take over any distance
        # (But may only take 1 draught with out a gap between, but this gap can be of any size)
        #
        # men may move 2 forwards or backwards when taking

        # Return True if the move is in the sequence of a highest scoring capture

        # There is no piece at this coord
        if move.getPiece() is None:
            print("There is no piece here!")
            logging.error("Player \"%s\" attempted to move a piece from somewhere there was not a piece" % (move.getPlayer().getName()))
            return False

        # The Player who made the move does not own the piece
        if move.getPlayer().getFaction() != move.getPiece().getAllegiance():
            print("you do not own that piece!")
            logging.error("Player \"%s\" attempted to move the piece at position %s, but does not own this piece" % (move.getPlayer().getName(), move.getPiece().getPosition()))
            return False

        # The Target is not Empty
        if move.getTarget() in self.__pieces.keys():
            logging.error("Player \"%s\" attempted to move the piece at position %s, to position %s which is not empty" % (move.getPlayer().getName(), move.getPiece().getPosition(), move.getTarget()))
            print("This space is not empty!")
            return False

        # TODO: extract this into helper method
        # TODO: Kings dont follow this rule
        # If the target is not diagonally adjacent to the piece (with no capture). This rule does not apply to Kings.

        # get a row index from 0-4 of the piece and target
        pieceColumnIndex  = (int(move.getPiece().getPosition()) - 1) % 5
        targetColumnIndex = (int(move.getTarget()) - 1) % 5
        pieceRow = int(move.getPiece().getPosition() / 5) + 1
        logging.debug("pieceColumnIndex: %s. targetColumnIndex: %s. pieceRow:%s. pieceRowEven: %s" % (
        pieceColumnIndex, targetColumnIndex, pieceRow, pieceRow % 2 == 0))
        # In even Rows the diagonally adjacent pieces are in column indices equal to or + 1 of the piece's column
        # In Odd rows it is equal to or -1
        if not pieceColumnIndex == targetColumnIndex:
            if pieceRow % 2 == 0 and not pieceColumnIndex - 1 == targetColumnIndex:
                logging.error("Player \"%s\" attempted to move the piece at %s to %s, but this piece cannot move there" % (move.getPlayer().getName(), move.getPiece().getPosition(), move.getTarget()))
                print("This piece cannot move there!")
                return False
            if pieceRow % 2 != 0 == "B" and not pieceColumnIndex + 1 == targetColumnIndex:
                logging.error("Player \"%s\" attempted to move the piece at %s to %s, but this piece cannot move there" % (move.getPlayer().getName(), move.getPiece().getPosition(), move.getTarget()))
                print("This piece cannot move there!")
                return False

        # TODO: For kings we must check that the target is diagonal from the piece

        return True

#    def evaluateGameWon(self):
#        return

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

    # Helpers

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
