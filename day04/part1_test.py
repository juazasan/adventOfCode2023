"""test for part1.py"""
import part1

class TestPart1:
    """Tests for part1.py"""

    def get_card_points(self):
        """Tests for get_card_points"""
        assert part1.get_card_points([1,2,3,4,5], [1,2,3,4,5]) == 16
        assert part1.get_card_points([1,2,3,4,5], [1,2,3,4]) == 8
        assert part1.get_card_points([1,2,3,4,5], [1,2,3]) == 4
        assert part1.get_card_points([1,2,3,4,5], [1,2]) == 2
        assert part1.get_card_points([1,2,3,4,5], [1]) == 1
        assert part1.get_card_points([1,2,3,4,5], [6]) == 0

    def parse_line(self):
        """Tests for parse_line"""
        input_line = 'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'
        assert part1.parse_line(input_line) == ([41,48,83,86,17], [83,86,6,31,17,9,48,53])

    def end_to_end(self):
        """end to end test"""
        input_content= """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
        cards = part1.parse_input(input_content.split('\n'))
        total = 0
        for card in cards:
            total +=    part1.get_card_points(card[0], card[1])
        print(total)
        assert total == 13
