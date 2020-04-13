class Move:
    __doc__ = "An object to contain the information relative to a move in a Draughts game"

    __player = ""
    __piece = object
    __target = ""

    # constructs a Move object
    #   player - The Player object representing the player that makes the move
    #   piece - A piece object representing the piece being moved
    #   target - consists of the coordinate of the space to move too
    def __init__(self, player, piece, target):
        self.__player = player
        self.__piece = piece
        self.__target = target

    def getPlayer(self):
        return self.__player

    def getPiece(self):
        return self.__piece

    def getTarget(self):
        return self.__target



