import numpy as np


class ChessBoard:
    def __init__(self, pieces):   
        self._array = np.array(
            [[pieces["BR1"], pieces["BN1"], pieces["BB1"], pieces["BQ"], pieces["BK"], pieces["BB2"], pieces["BN2"], pieces["BR2"]],
            [pieces["Bp1"], pieces["Bp2"], pieces["Bp3"], pieces["Bp4"], pieces["Bp5"], pieces["Bp6"], pieces["Bp7"], pieces["Bp8"]],
            ["0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0"],
            [pieces["Wp1"], pieces["Wp2"], pieces["Wp3"], pieces["Wp4"], pieces["Wp5"], pieces["Wp6"], pieces["Wp7"], pieces["Wp8"]],
            [pieces["WR1"], pieces["WN1"], pieces["WB1"], pieces["WQ"], pieces["WK"], pieces["WB2"], pieces["WN2"], pieces["WR2"]]]
        )

    @property
    def array(self):
        return self._array
    
    @array.setter
    def array(self, value):
        self._array = value

        

class ChessPiece:
    def __init__(self, color, position, movement):
        self._color = color
        self._position = position
        self._column = position[0]
        self._row = position[1]
        self._movement = movement

    def move(self):


class Pawn(ChessPiece):
    def __init__(self, color, position):
        super().__init__(
            color,
            position,
            movement = "forward"
        )

    def move(self):
        if self._color == "W":
            self.position[0] = 





        
