"""test for part1.py"""
import part1
import re

class TestPart1:
    """Tests for part1.py"""

    test1={
        'schematic': [
            list(".......#."),
            list("......12."),
            list("......34."),
        ],
        'numbers': [
            {
                'begin': {
                    'x': 6,
                    'y': 1,
                },
                'end': {
                    'x': 7,
                    'y': 1,
                }
            },
            {
                'begin': {
                    'x': 6,
                    'y': 2,
                },
                'end': {
                    'x': 7,
                    'y': 2,
                }
            },
        ],
    }

    test2={
        'sch': [
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
    ],
        'numbers': [467, 114, 35, 633, 617, 58, 592, 755, 664, 598],
    }

    test3={
        'sch' : [
        list("467..114.."),
        list("...*......"),
    ],
        'numbers': [467, 114],
    }

    test4={
        'sch': [
        list("467..114"),
        list("...*...*"),
    ],
    'numbers': [467, 114],
    }

    test5={
        'sch': [
        list("467**114"),
        list("........"),
    ],
    'numbers': [467, 114],
    }

    test6={
        'sch': [
        list(".679.....662....71............................805..........862.680...................................................................687...."),
        list("............*....-..811..........846..855......*.............*..$........230.92@............................=.....................92........"),
    ],
    'numbers': [679, 662, 71, 805, 862, 680, 687, 811, 846, 855, 230, 92, 92],
    'valid_numbers': [662, 71, 805, 862, 680, 92],
    }

    def test_is_character(self):
        """Tests for is_character(c)"""
        assert part1.is_character('.') is False
        assert part1.is_character('1') is False
        assert part1.is_character('#') is True
        assert part1.is_character('L') is True
        assert part1.is_character('$') is True

    def test_number_has_adjacent(self):
        """Tests for c_has_adjacent(x, y, schmtic)"""
        assert part1.number_has_adjacent(self.test1['numbers'][0], self.test1['schematic']) is True
        assert part1.number_has_adjacent(self.test1['numbers'][1], self.test1['schematic']) is False
        got_numbers = part1.find_numbers(self.test6['sch'])
        got_valid_numbers = []
        for number in got_numbers:
            if part1.number_has_adjacent(number, self.test6['sch']):
                got_valid_numbers.append(number['value'])
        assert got_valid_numbers == self.test6['valid_numbers']
        # assert part1.c_has_adjacent(5, 0, self.test3) is False
        # assert part1.c_has_adjacent(6, 0, self.test3) is False
        # assert part1.c_has_adjacent(7, 0, self.test3) is False

    def test_find_numbers(self):
        """Tests for find_numbers(sch)"""
        for number in part1.find_numbers(self.test2['sch']):
            assert number['value'] in self.test2['numbers']
        for number in part1.find_numbers(self.test6['sch']):
            assert number['value'] in self.test6['numbers']
        for number in part1.find_numbers(self.test1['schematic']):
            assert number['value'] in [12, 34]
        for number in part1.find_numbers(self.test3['sch']):
            assert number['value'] in self.test3['numbers']
        for number in part1.find_numbers(self.test4['sch']):
            assert number['value'] in self.test4['numbers']
        for number in part1.find_numbers(self.test5['sch']):
            assert number['value'] in self.test5['numbers']

        """now from input"""
        # Read the file
        with open('day03/input', 'r') as file:
            content = file.read()
        # Extract all numbers using regular expression
        expected_numbers = [int(num) for num in re.findall(r'\d+', content)]
        # Got numbers from input
        source_schmtic = part1.parse_input(content.split('\n'))
        got_numbers = part1.find_numbers(source_schmtic)

        assert len(expected_numbers) == len(got_numbers)
        total = 0
        for number in got_numbers:
            total += number['value']
            assert number['value'] in expected_numbers
        assert total == sum(expected_numbers)

