import unittest
import randomgame

class TestGame(unittest.TestCase):
    def test_input(self):
        result = randomgame.run_guess_game(5, 5)
        self.assertTrue(result)

    def test_input_incorrect(self):

        result = randomgame.run_guess_game(5, 0)
        self.assertFalse(result)

    def test_input_number(self):
        result = randomgame.run_guess_game(5, 11)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = randomgame.run_guess_game(5, '')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()

