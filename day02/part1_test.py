import unittest
import part1

class TestPart2(unittest.TestCase):

    def test_parse_game(self):
        game = part1.parse_game('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green')
        games = [
            {
                'red': 4,
                'green': 0,
                'blue': 3,
            },
            {
                'red': 1,
                'green': 2,
                'blue': 6,
            },
            {
                'red': 0,
                'green': 2,
                'blue': 0,
            },
        ]
        self.assertEqual(game['id'], 1)
        self.assertEqual(game['games'], games)

    def test_is_game_possible(self):
        cubes_guess = {
            'red': 12,
            'green': 13,
            'blue': 14,
        }
        games_ok = [
            {
                'red': 4,
                'green': 0,
                'blue': 3,
            },
            {
                'red': 1,
                'green': 2,
                'blue': 6,
            },
            {
                'red': 0,
                'green': 2,
                'blue': 0,
            },
        ]
        games_error = [
            {
                'red': 20,
                'green': 8,
                'blue': 6,
            },
            {
                'red': 4,
                'green': 13,
                'blue': 5,
            },
            {
                'red': 1,
                'green': 5,
                'blue': 0,
            },
        ]
        self.assertTrue(part1.is_game_possible(games_ok, cubes_guess))
        self.assertFalse(part1.is_game_possible(games_error, cubes_guess))

    def test_day02_part1(self):
        cubes_guess = {
            'red': 12,
            'green': 13,
            'blue': 14,
        }
        self.assertEqual(part1.day02_part1('input_test', cubes_guess), 8)


if __name__ == '__main__':
    unittest.main()