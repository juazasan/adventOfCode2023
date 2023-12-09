import unittest
import part2

class TestPart2(unittest.TestCase):

    def test_parse_game(self):
        game = part2.parse_game('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green')
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

    def test_calculate_game_power(self):
        game_48 = [
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
        game_1560 = [
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
        self.assertEqual(part2.calculate_game_power(game_48), 48)
        self.assertEqual(part2.calculate_game_power(game_1560), 1560)

    def test_day02_part2(self):
        self.assertEqual(part2.day02_part2('input_test'), 2286)


if __name__ == '__main__':
    unittest.main()