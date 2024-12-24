"""advent of code day 4 part 1"""

def get_card_points(winning_numbers, got_numbers):
    """get card points"""
    matches = 0
    points = 0
    for number in got_numbers:
        if number in winning_numbers:
            matches += 1
    if matches > 0:
        points = pow(2,matches-1)
    return points

def parse_line(line):
    """parse line"""
    line = line.split(' | ')
    winning_numbers = [int(x) for x in line[0].split(':')[1].split(' ') if x != '']
    got_numbers = [int(x) for x in line[1].split(' ') if x != '']
    return (winning_numbers, got_numbers)

def parse_input(content):
    """parse input"""
    cards = ()
    for line in content:
        cards += (parse_line(line),)
    return cards

if __name__ == '__main__':
    with open('input', 'r', encoding='utf-8') as file:
        content = file.read()
    cards = parse_input(content.split('\n'))
    total = 0
    for card in cards:
        total += get_card_points(card[0], card[1])
    print(str(total))
