from Draughts.Piece import Piece


class Utils:

    # reduces a jagged array be one dimension
    @staticmethod
    def flattenJaggedArray(array):

        if len(array) == 0 or type(array[0]) != list:
            return

        flattened = []

        for e in array:
            for e2 in e:
                flattened.append(e2)

        return flattened

    # Returns the column and row of a piece based on its 1-50 index
    @staticmethod
    def getCartesianCoordinate(pieceIndex):

        row = int((pieceIndex - 1) / 5) + 1

        columnInRow = ((pieceIndex - 1)  % 5) + 1

        if row % 2 == 0:
            column = (columnInRow * 2) - 1
        else:
            column = columnInRow * 2

        return tuple([column, row])

    @staticmethod
    def getStartStateString():
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
    def buildPieceListFromStringArray(stringArray):

        pieces = {}

        # Build a list of pieces on the bord from the string array representation
        for i in range(0, len(stringArray)):

            # If there is a piece in this place add it to the list

            if stringArray[i] != "-1":
                pieces[str(i + 1)] = Piece("%s:%s" % (stringArray[i], i + 1))

        return pieces

