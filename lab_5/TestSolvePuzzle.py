from solve_puzzle import solve_puzzle as puzzle
import unittest

class TestSolvePuzzle(unittest.TestCase):
        def testClockwise(self):
                """Tests a board solveable using only CW moves"""
        print(solve_puzzle([3, 6, 4, 1, 3, 4, 2, 0]))

        def testCounterClockwise(self):
                """Tests a board solveable using only CCW moves"""
        

        def testMixed(self):
                """Tests a board solveable using only a combination of CW and CCW moves"""

        
        def testUnsolveable(self):
                """Tests an unsolveable board"""


unittest.main()