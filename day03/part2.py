"""advent of code day 2 part 1"""

def get_adjacent_stars(number, schmtic):
    """Checks if number has any adjacent characters around in schmtic"""
    y = number['begin']['y']
    adjacent_cells = []
    for x in range(number['begin']['x'], number['end']['x']+1):
        if 0 < x < len(schmtic[y])-1 and 0 < y < len(schmtic)-1:
            adjacent_cells.extend([[y,x-1],[y,x-1],[y,x+1],[y-1,x],[y+1,x],[y-1,x-1],[y-1,x+1],[y+1,x-1],[y+1,x+1]])
        if x == 0 and y == 0:
            adjacent_cells.extend([[y,x+1],[y+1,x],[y+1,x+1]])
        if x == 0 and y == len(schmtic)-1:
            adjacent_cells.extend([[y,x+1],[y-1,x],[y-1,x+1]])
        if x == len(schmtic[y])-1 and y == 0:
            adjacent_cells.extend([[y,x-1],[y+1,x],[y+1,x-1]])
        if x == len(schmtic[y])-1 and y == len(schmtic)-1:
            adjacent_cells.extend([[y,x-1],[y-1,x],[y-1,x-1]])
        if x == 0 and 0 < y < len(schmtic)-1:
            adjacent_cells.extend([[y,x+1],[y-1,x],[y+1,x],[y-1,x+1],[y+1,x+1]])
        if x == len(schmtic[y])-1 and 0 < y < len(schmtic)-1:
            adjacent_cells.extend([[y,x-1],[y-1,x],[y+1,x],[y-1,x-1],[y+1,x-1]])
        if y == 0 and 0 < x < len(schmtic[y])-1:
            adjacent_cells.extend([[y,x-1],[y,x+1],[y+1,x],[y+1,x-1],[y+1,x+1]])
        if y == len(schmtic)-1 and 0 < x < len(schmtic[y])-1:
            adjacent_cells.extend([[y,x-1],[y,x+1],[y-1,x],[y-1,x-1],[y-1,x+1]])
    adjacent_stars = set()
    for cell in adjacent_cells:
        if schmtic[cell[0]][cell[1]] == '*':
            gear_key = "x: " + str(cell[1]) + " y: " + str(cell[0])
            adjacent_stars.add(gear_key)
    return adjacent_stars

def find_gears(sch):
    """finds all gears in sch"""
    gears = {}
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
                for gear_key in get_adjacent_stars(number, sch):
                    if gear_key not in gears:
                       gears[gear_key] = []
                    if gear_key in gears:
                       gears[gear_key].append(number['value'])
                is_new_number = True
                number = {}
                begin = {}
                end = {}
    return gears

def prod_valid_gears(g, schematic):
    """sum of prod gears"""
    total = 0
    count = 0
    for gear in g:
        if len(g[gear]) == 2:
            count += 1
            total += g[gear][0] * g[gear][1]
    print(count)
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
    gears = find_gears(source_schmtic)
    print(str(prod_valid_gears(gears, source_schmtic)))
