from functools import reduce

data = []

with open('input.txt') as f:
    for line in f.readlines():
        game, pulls = line.split(":")
        game_num = game.split()[1]
        parsed_pulls = [
            {color.strip(): int(num.strip()) 
            for num, color in (pair.split() for pair in entry.split(','))} 
            for entry in pulls.split(';')
        ]
        
        data.append(parsed_pulls)

games = {i: True for i in range(len(open('input.txt').readlines()))}

power_sum = 0
for idx, entry in enumerate(data):
    max_dict = {"green": 0, "blue": 0, "red": 0}
    for bag_pull in entry:
        for color, num in bag_pull.items():
            if num > max_dict[color]:
                max_dict[color] = num
    power_sum += reduce(lambda x, y: x * y, max_dict.values())
print(power_sum)
