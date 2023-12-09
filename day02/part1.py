"""advent of code day 2 part 1"""

def is_game_possible(games, cubes):
    """Checks if the game is possible"""
    for game in games:
        for color in game:
            if game[color] > cubes[color]:
                return False
    return True

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

def day02_part1(file_name, cubes):
    """main function"""
    total = 0
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            game = parse_game(line)
            if is_game_possible(game['games'], cubes):
                total += game['id']
    return total

if __name__ == '__main__':
    cubes_guess = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    print(str(day02_part1('input', cubes_guess)))
