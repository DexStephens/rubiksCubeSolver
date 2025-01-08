from typing import List


class Cube:
    def __init__(self):
        self.up: List[str] = [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']]
        self.down: List[str] = [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']]
        self.front: List[str] = [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]
        self.back: List[str] = [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']]
        self.left: List[str] = [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']]
        self.right: List[str] = [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]
    
    def shuffle(self):
        """
        Shuffles the cube up for solving by randomly performing operations on the cube
        """
        pass

    def solveFirstFace(self):
        """
        This consists of white cross and white corners
        """
        # White cross: no specific algorithm
        # White corners: R' D' R D, repeat until corner is oriented correctly, adjust the position of the corner to align under it's destination and reapply
        pass

    
    def solveMiddleLayer(self):
        """
        This consists of solving the middle layer edges
        """
        # For edges moving left: U' L' U L U F U' F'
        # For edges moving right: U R U' R' U' F' U F
        pass
    
    def solveTopLayer(self):
        """
        This consists of yellow cross, yellow corners, and yellow edges
        """
        # Yellow cross: Line pattern(F R U R' U' F'), L pattern(F U R U' R' F'), applied until a yellow cross forms
        # Yellow corners: U R U' L' U R' U' L, repeated until all corners are in the correct position
        # Yellow edges: R' D' R D, position the incorrect corner on the bottom right of the top face, apply repeatedly until the corner is oriented correctly, move next incorrect corner into place and repeat
        pass

    def performOperation(self, face: str, clockwise: bool):
        pass
    # What are my different options that can be performed on the cube??

    def __repr__(self):
        pass