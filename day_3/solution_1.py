import re

with open('input.txt') as f:
    lines = f.read().splitlines()

array = list(map(lambda x: list(x), lines))

special_chars = set()
for line in array:
    for char in line:
        if char != '.' and not char.isdigit():
            special_chars.add(char)

print("|".join(special_chars))

def check_neighbours(x, y):
    neighbours = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if x + i < 0 or x + i >= len(array):
                continue
            if y + j < 0 or y + j >= len(array[0]):
                continue
            neighbours.append(array[x + i][y + j])
    special_pattern = re.compile(r'(%|\/|@|=|-|\+|#|&|\*|\$)')
    for neighbour in neighbours:
        if special_pattern.match(neighbour):
            return True
    return False


def find_numbers(line: list) -> list[tuple]:
    pattern = re.compile(r'\d+')
    indices = []
    for match in pattern.finditer(''.join(line)):
        indices.append(match.span())
    return indices

def get_number(line, start, end) -> int:
    return int(''.join(line[start:end]))

total = 0
continue_counter = 0
for i in range(len(array)):
    for j in range(len(array[0])):
        if continue_counter > 0:
            continue_counter -= 1
            continue
        if array[i][j] == '.':
            continue
        if not check_neighbours(i, j):
            continue
        indices = find_numbers(array[i])
        if len(indices) == 0:
            continue
        number = get_number(array[i], indices[0][0], indices[0][1])
        total += number
        continue_counter = len(str(number)) - 1


print(total)
