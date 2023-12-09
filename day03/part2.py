"""advent of code day 2 part 1"""

def calculate_game_power(games):
    """Checks if the game is possible"""
    min_blue = 0
    min_red = 0
    min_green = 0
    for game in games:
        if game['blue'] > min_blue:
            min_blue = game['blue']
        if game['red'] > min_red:
            min_red = game['red']
        if game['green'] > min_green:
            min_green = game['green']
    return min_blue * min_red * min_green

def parse_game(line):
    """Parse a game"""
    game_id =int(line.split(':')[0].split(' ')[1])
    games = []
    for game in line.split(':')[1].split(';'):
        new_game = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }
        for cube in game.split(','):
            new_game[cube.strip().split(' ')[1]] = int(cube.strip().split(' ')[0])
        games.append(new_game)
    return {
        'id': game_id,
        'games': games,
    }

def day02_part2(file_name):
    """main function"""
    total = 0
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            game = parse_game(line)
            total += calculate_game_power(game['games'])
    return total

if __name__ == '__main__':
    cubes_guess = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    print(str(day02_part2('input')))
