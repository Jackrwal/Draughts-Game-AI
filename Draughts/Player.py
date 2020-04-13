from Draughts.Move import Move


class Player:
    __score = 0
    __name = ""
    __faction = ""

    # Constructor

    def __init__(self, name, faction):
        self.__name = name
        self.__faction = faction

    # TODO: input validation
    # functions
    def getMove(self, game):
        move = input("%s .Enter the position of a draught (1-50 top-left to bottom-right) and the position to move it to " % self.__name +
                     "in the format '31:27'. \n\r" +
                     "Enter 'q' to quit. \n\r")

        if move == "q":
            return 'q'

        moveSplit = move.split(':')
        return Move(self, game.getPiece(moveSplit[0]), moveSplit[1])

    # getters setters

    def getScore(self):
        return self.__score

    def setScore(self, score):
        self.__score = score

    def getName(self):
        return self.__name

    def getFaction(self):
        return self.__faction
