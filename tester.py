import unittest
from simple_guess_game import play_guess_game

class TestSimpleGuessGame(unittest.TestCase):

    def test_correct_guess(self):
        output = []
        result = play_guess_game(secret=5, input_func=lambda _: "5", print_func=output.append)
        self.assertEqual(result, "Correct!")
        self.assertIn("Correct!", output)

    def test_too_low(self):
        output = []
        result = play_guess_game(secret=8, input_func=lambda _: "2", print_func=output.append)
        self.assertEqual(result, "Too low!")
        self.assertIn("Too low!", output)

    def test_too_high(self):
        output = []
        result = play_guess_game(secret=3, input_func=lambda _: "9", print_func=output.append)
        self.assertEqual(result, "Too high!")
        self.assertIn("Too high!", output)

if __name__ == '__main__':
    unittest.main()
