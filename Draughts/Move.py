class Move:
    __doc__ = "An object to contain the information relative to a move in a Draughts game"

    __player = ""
    __piece = object
    __target = ""
    __score = -1

    # used for tracking sequences of moves
    __next = object
    __prev = object

    # constructs a Move object
    #   player - The Player object representing the player that makes the move
    #   piece - A piece object representing the piece being moved
    #   target - consists of the coordinate of the space to move too
    def __init__(self, player, piece, target):
        self.__player = player
        self.__piece = piece
        self.__target = target

    # adds a new move to the sequence of moves, after this object
    def addToSequence(self, move):
        __next = move
        move.setPrev(self)

    def getPlayer(self):
        return self.__player

    def getPiece(self):
        return self.__piece

    def getTarget(self):
        return self.__target

    def getScore(self):
        return self.__score

    def setScore(self, score):
        self.__score = score

    def getNext(self):
        return self.__next

    def getPrev(self):
        return self.__prev

    def setPrev(self, move):
        self.__prev = move



