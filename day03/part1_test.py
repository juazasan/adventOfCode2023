"""test for part1.py"""
import part1

class TestPart1:
    """Tests for part1.py"""

    test1=[
        list(".......#."),
        list("......12."),
        list("......34."),
    ]

    test2=[
        list("467..114.."),
        list("...*......"),
        list("..35..633."),
        list("......#..."),
        list("617*......"),
        list(".....+.58."),
        list("..592....."),
        list("......755."),
        list("...$.*...."),
        list(".664.598.."),
    ]

    test3=[
        list("467..114.."),
        list("...*......"),
    ]

    test4=[
        list("467..114"),
        list("...*...*"),
    ]

    test5=[
        list("467**114"),
        list("........"),
    ]

    test6=[
        list(".679.....662....71............................805..........862.680...................................................................687...."),
        list("............*....-..811..........846..855......*.............*..$........230.92@............................=.....................92........"),
    ]

    def test_is_character(self):
        """Tests for is_character(c)"""
        assert part1.is_character('.') is False
        assert part1.is_character('1') is False
        assert part1.is_character('#') is True
        assert part1.is_character('L') is False
        assert part1.is_character('$') is True

    def test_c_has_adjacent(self):
        """Tests for c_has_adjacent(x, y, schmtic)"""
        assert part1.c_has_adjacent(0, 0, self.test1) is False
        assert part1.c_has_adjacent(7, 1, self.test1) is True
        assert part1.c_has_adjacent(8, 2, self.test1) is False
        assert part1.c_has_adjacent(5, 0, self.test3) is False
        assert part1.c_has_adjacent(6, 0, self.test3) is False
        assert part1.c_has_adjacent(7, 0, self.test3) is False

    def test_sum_parts(self):
        """Tests for sum_parts(schematic)"""
        assert part1.sum_parts(self.test1) == 12
        assert part1.sum_parts(self.test3) == 467
        assert part1.sum_parts(self.test4) == 581
        assert part1.sum_parts(self.test5) == 581
        assert part1.sum_parts(self.test2) == 4361
        assert part1.sum_parts(self.test6) == 3172
