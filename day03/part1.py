"""advent of code day 2 part 1"""

def is_character(c):
    """Checks if c is a character"""
    if c == '.':
        return False
    if c.isdigit():
        return False
    return True

def number_has_adjacent(number, schmtic):
    """Checks if number has any adjacent characters around in schmtic"""
    y = number['begin']['y']
    cell_has_adjacent = False
    for x in range(number['begin']['x'], number['end']['x']):
        if 0 < x < len(schmtic[y])-1 and 0 < y < len(schmtic)-1 and \
            any(is_character(c) for c in [schmtic[y][x-1],
                                        schmtic[y][x+1],
                                        schmtic[y-1][x],
                                        schmtic[y+1][x],
                                        schmtic[y-1][x-1],
                                        schmtic[y-1][x+1],
                                        schmtic[y+1][x-1],
                                        schmtic[y+1][x+1]]):
            cell_has_adjacent = True
            break
        if not cell_has_adjacent and x == 0 and y == 0 and \
            any(is_character(c) for c in [schmtic[y][x+1],schmtic[y+1][x],schmtic[y+1][x+1]]):
            cell_has_adjacent = True
            break
        if not cell_has_adjacent and x == 0 and y == len(schmtic)-1 and \
            any(is_character(c) for c in [schmtic[y][x+1],schmtic[y-1][x],schmtic[y-1][x+1]]):
            cell_has_adjacent = True
            break
        if not cell_has_adjacent and x == len(schmtic[y])-1 and y == 0 and \
            any(is_character(c) for c in [schmtic[y][x-1],schmtic[y+1][x],schmtic[y+1][x-1]]):
            cell_has_adjacent = True
            break
        if not cell_has_adjacent and x == len(schmtic[y])-1 and y == len(schmtic)-1 and \
            any(is_character(c) for c in [schmtic[y][x-1],schmtic[y-1][x],schmtic[y-1][x-1]]):
            cell_has_adjacent = True
            break
        if not cell_has_adjacent and x == 0 and 0 < y < len(schmtic)-1 and \
            any(is_character(c) for c in [schmtic[y][x+1],
                                        schmtic[y-1][x],
                                        schmtic[y+1][x],
                                        schmtic[y-1][x+1],
                                        schmtic[y+1][x+1]]):
            cell_has_adjacent = True
            break
        if not cell_has_adjacent and x == len(schmtic[y])-1 and 0 < y < len(schmtic)-1 and \
            any(is_character(c) for c in [schmtic[y][x-1],
                                        schmtic[y-1][x],
                                        schmtic[y+1][x],
                                        schmtic[y-1][x-1],
                                        schmtic[y+1][x-1]]):
            cell_has_adjacent = True
            break
        if not cell_has_adjacent and y == 0 and 0 < x < len(schmtic[y])-1 and \
            any(is_character(c) for c in [schmtic[y][x-1],
                                        schmtic[y][x+1],
                                        schmtic[y+1][x],
                                        schmtic[y+1][x-1],
                                        schmtic[y+1][x+1]]):
            cell_has_adjacent = True
        if not cell_has_adjacent and y == len(schmtic)-1 and 0 < x < len(schmtic[y])-1 and \
            any(is_character(c) for c in [schmtic[y][x-1],
                                        schmtic[y][x+1],
                                        schmtic[y-1][x],
                                        schmtic[y-1][x-1],
                                        schmtic[y-1][x+1]]):
            cell_has_adjacent = True
            break
    return cell_has_adjacent

def find_numbers(sch):
    """finds all numbers in sch"""
    numbers = []
    for y, r in enumerate(sch):
        is_new_number = True
        number = {}
        begin = {}
        end = {}
        for x, c in enumerate(r):
            if c.isdigit() and is_new_number:
                is_new_number = False
                number['begin']={
                    'x': x,
                    'y': y,
                }
                number['value'] = int(c)
                continue
            if c.isdigit() and not is_new_number:
                number['value'] *= 10
                number['value'] += int(c)
            if not is_new_number and (not c.isdigit() or x == len(sch[y])-1):
                number['end']={
                    'x': x-1,
                    'y': y,
                }
                numbers.append(number)
                is_new_number = True
                number = {}
                begin = {}
                end = {}
    return numbers

def sum_parts(numbers, schematic):
    """sum valid engine parts"""
    total = 0
    for number in numbers:
        if number_has_adjacent(number, schematic):
            print(number['value'])
            total += number['value']
    return total

def parse_input(content):
    """parse input"""
    schmtic = []
    for line in content:
        row = list(line)
        schmtic.append(row)
    return schmtic

if __name__ == '__main__':
    source_schmtic = []
    with open('input', 'r', encoding='utf-8') as file:
        content = file.read()
    source_schmtic = parse_input(content.split('\n'))
    numbers = find_numbers(source_schmtic)
    print(str(sum_parts(numbers, source_schmtic)))
