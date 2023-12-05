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


limit_dict = {"green": 13, "blue": 14, "red": 12}
games = {i: True for i in range(len(open('input.txt').readlines()))}

res = 0
invalid = False

for idx, entry in enumerate(data):
    max_dict = {"green": 0, "blue": 0, "red": 0}
    for bag_pull in entry:
        if any(num > limit_dict[color] for color, num in bag_pull.items()):
            invalid = True
            break
        for color, num in bag_pull.items():
            print(color, num)
            if num > max_dict[color]:
                max_dict[color] = num
    print(max_dict)

    if not invalid:
        res += idx + 1 
    else:
        invalid = False
print(res)
print(max_dict)
