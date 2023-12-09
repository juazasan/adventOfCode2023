"""advent of code 2023 - exercise 1 part 2"""

def is_number(line, i):
    """returns the number of the word in the line, or -1 if it is not a number"""
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    k = 1
    for number in numbers:
        if i + len(number) <= len(line) and number in line[i:i+len(number)]:
            return k
        k += 1
    return -1

def get_number(line):
    """returns the number of the line"""
    first_number = -1
    second_number = -1
    for i, c in enumerate(line):
        if c >= '0' and c <= '9' and first_number == -1:
            first_number = int(c)
            second_number = int(c)
            continue
        if c >= '0' and c <= '9' and first_number != -1:
            second_number = int(c)
            continue
        next_number =  is_number(line, i)
        if c >= 'a' and c <= 'z' and first_number == -1 and next_number != -1:
            first_number = next_number
            second_number = next_number
            continue
        if c >= 'a' and c <= 'z' and first_number != -1 and next_number != -1:
            second_number = next_number
    return first_number*10 + second_number

def main(file_name):
    """main function"""
    f = open(file_name, 'r', encoding='utf-8')
    total = 0
    while True:
        line = f.readline()
        if not line:
            break
        total += int(get_number(line))
    f.close()
    print(total)

main('input')
