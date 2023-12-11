"""advent of code day 2 part 1"""

def is_character(c):
    """Checks if c is a character"""
    if c == '.':
        return False
    if c.isdigit():
        return False
    if 'A' <= c <= 'Z':
        return False
    if 'a' <= c <= 'z':
        return False
    return True

def c_has_adjacent(x, y, schmtic):
    """Checks if x,y has any adjacent characters around in schmtic"""
    cell_has_adjacent = False
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
    if not cell_has_adjacent and x == 0 and y == 0 and \
        any(is_character(c) for c in [schmtic[y][x+1],schmtic[y+1][x],schmtic[y+1][x+1]]):
        cell_has_adjacent = True
    if not cell_has_adjacent and x == 0 and y == len(schmtic)-1 and \
        any(is_character(c) for c in [schmtic[y][x+1],schmtic[y-1][x],schmtic[y-1][x+1]]):
        cell_has_adjacent = True
    if not cell_has_adjacent and x == len(schmtic[y])-1 and y == 0 and \
        any(is_character(c) for c in [schmtic[y][x-1],schmtic[y+1][x],schmtic[y+1][x-1]]):
        cell_has_adjacent = True
    if not cell_has_adjacent and x == len(schmtic[y])-1 and y == len(schmtic)-1 and \
        any(is_character(c) for c in [schmtic[y][x-1],schmtic[y-1][x],schmtic[y-1][x-1]]):
        cell_has_adjacent = True
    if not cell_has_adjacent and x == 0 and 0 < y < len(schmtic)-1 and \
        any(is_character(c) for c in [schmtic[y][x+1],
                                      schmtic[y-1][x],
                                      schmtic[y+1][x],
                                      schmtic[y-1][x+1],
                                      schmtic[y+1][x+1]]):
        cell_has_adjacent = True
    if not cell_has_adjacent and x == len(schmtic[y])-1 and 0 < y < len(schmtic)-1 and \
        any(is_character(c) for c in [schmtic[y][x-1],
                                      schmtic[y-1][x],
                                      schmtic[y+1][x],
                                      schmtic[y-1][x-1],
                                      schmtic[y+1][x-1]]):
        cell_has_adjacent = True
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
    return cell_has_adjacent

def sum_parts(schematic):
    """sum vaid engine parts"""
    total = 0
    for y, r in enumerate(schematic):
        is_new_number = True
        is_valid_part = False
        new_number = 0

        for x, c in enumerate(r):
            if not c.isdigit() and not is_new_number and is_valid_part:
                total += new_number
                is_new_number = True
                is_valid_part = False
                new_number = 0
                continue
            if not c.isdigit() and not is_new_number and not is_valid_part:
                is_new_number = True
                is_valid_part = False
                new_number = 0
                continue
            if c.isdigit() and not is_new_number:
                new_number *= 10
                new_number += int(c)
            if c.isdigit() and is_new_number:
                new_number = int(c)
                is_new_number = False
            if c.isdigit() and not is_valid_part:
                is_valid_part = c_has_adjacent(x, y, schematic)
        
        if not is_new_number and is_valid_part:
            total += new_number

    return total

if __name__ == '__main__':
    source_schmtic = []
    with open('input', 'r', encoding='utf-8') as file:
        for line in file:
            row = list(line)
            source_schmtic.append(row)
    print(str(sum_parts(source_schmtic)))
