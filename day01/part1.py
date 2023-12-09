def get_number(line):
    first_number = -1
    second_number = -1
    for c in line:
        if c >= '0' and c <= '9' and first_number == -1:
            first_number = int(c)
            second_number = int(c)
        if c >= '0' and c <= '9' and first_number != -1:
            second_number = int(c)
    return first_number*10 + second_number 

def main(file_name):
    f = open(file_name, 'r')
    total = 0
    while True:
        line = f.readline()
        if not line:
            break
        total += int(get_number(line))
    f.close()
    print(total)

main('input')