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
        pass

    
    def solveMiddleLayer(self):
        """
        This consists of solving the middle layer edges
        """
        pass
    
    def solveTopLayer(self):
        """
        This consists of yellow cross, yellow corners, and yellow edges
        """
        pass

    def performOperation(self, face: str, clockwise: bool):
        pass
    # What are my different options that can be performed on the cube??

    def __repr__(self):
        pass