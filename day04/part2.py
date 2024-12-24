"""advent of code day 4 part 2"""

def get_scratchcards(source_cards):
    """get scratchcards"""
    processed_cards = []
    to_process_cards = [source_cards[0]]
    for len(to_process_cards) > 0:
        card = to_process_cards[0]
        processed_cards.append(card)
        to_process_cards = to_process_cards[1:]
        winning_numbers = card[0]
        got_numbers = card[1]
        matches = 0
        for number in got_numbers:
            if number in winning_numbers:
                matches += 1
        if matches > 0:
            to_process_cards.extend
    return len(processed_cards)

def parse_line(line):
    """parse line"""
    line = line.split(' | ')
    winning_numbers = [int(x) for x in line[0].split(':')[1].split(' ') if x != '']
    got_numbers = [int(x) for x in line[1].split(' ') if x != '']
    return (winning_numbers, got_numbers)

def parse_input(content):
    """parse input"""
    cards = ()
    i = 1
    for line in content:
        cards += ((1,parse_line(line)),)
    return cards

if __name__ == '__main__':
    with open('input', 'r', encoding='utf-8') as file:
        content = file.read()
    cards = parse_input(content.split('\n'))
    total = 0
    for card in cards:
        total += get_card_points(card[0], card[1])
    print(str(total))
