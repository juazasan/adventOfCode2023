import unittest
import part2

class TestPart2(unittest.TestCase):

    def test_is_number(self):
        self.assertEqual(part2.is_number('one', 0), 1)
        self.assertEqual(part2.is_number('onTest', 0), -1)
        self.assertEqual(part2.is_number('Testone', 4), 1)
        self.assertEqual(part2.is_number('Testtwo', 4), 2)
        self.assertEqual(part2.is_number('Testtwo', 3), -1)

    def test_get_number(self):
        self.assertEqual(part2.get_number('one'), 11)
        self.assertEqual(part2.get_number('seightwoplhzgbvb7275'), 85)
        self.assertEqual(part2.get_number('qkg2fivemrlzlhxxzcmfive'), 25)
        self.assertEqual(part2.get_number('lnbgnkkfhseven5zfive2qcr'), 72)

if __name__ == '__main__':
    unittest.main()