class Piece:
    __doc__ = "A object to represent a piece in a game of Draughts"

    # fields
    __allegiance = ""
    __pieceState = ""

    # TODO: redundant information
    __position = -1

    # constructors

    # constructs a new piece
    #   allegiance the side of the game which the piece is on ("B" or "W")
    #   state whether the piece is a man, or king. ("m", "K")
    def __init__(self, allegiance, state, position):
        self.__allegiance = allegiance
        self.__pieceState = state
        self.__position = position

    # constructs a new piece from a string representation
    def __init__(self, pieceString):

        # TODO: Check string format matches correct format, else throw error

        self.__allegiance = pieceString[0]
        self.__pieceState = pieceString[1]

        self.__position = int(pieceString[3:])

    # methods

    def setKing(self):
        self.__pieceState = "K"

    # getters setters

    def getAllegiance(self):
        return self.__allegiance

    def getPieceState(self):
        return self.__pieceState

    def getPosition(self):
        return self.__position

    def setPosition(self, position):
        self.__position = position

    # to string method

    def toString(self):
        return "%s%s:%s" % (self.__allegiance, self.__pieceState, self.__position)


