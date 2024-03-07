import unittest
from turnTracker import TurnTracker

# Implement your unit tests here

class TestTurnTracker(unittest.TestCase):
    def test_addPlayer(self):
        game1 = TurnTracker()
        game1.addPlayer("Sergio")

        self.assertEqual(game1.numberOfPlayers(), 1)

    
    def test_nextPlayer(self):
        game2 = TurnTracker()
        game2.addPlayer("Sergio")
        game2.addPlayer("Filipe")

        self.assertEqual(game2.nextPlayer(), "Sergio")


    def test_numberOfPlayers(self):
        game3 = TurnTracker()
        game3.addPlayer("Sergio")

        self.assertEqual(game3.numberOfPlayers(), 1)

    
    def test_skipNextPlayer(self):
        game3 = TurnTracker()
        game3.addPlayer("Sergio")
        game3.addPlayer("Filipe")
        game3.addPlayer("Elham")
        game3.skipNextPlayer()

        self.assertEqual(game3.nextPlayer(), "Filipe")
    
    def test_reverseTurnOrder(self):
        game4 = TurnTracker()
        game4.addPlayer("Sergio")
        game4.addPlayer("Filipe")
        game4.reverseTurnOrder()

        self.assertEqual(game4.nextPlayer(), "Sergio")
        self.assertEqual(game4.nextPlayer(), "Filipe")




unittest.main()