data = open('input.txt').read().splitlines()
point_total = 0


for line in data:
    line = line.split(":")[1].strip()
    winning_numbers, drawn_numbers = line.split("|")
    winning_numbers = set(int(number) for number in winning_numbers.strip().split())
    drawn_numbers = set(int(number) for number in drawn_numbers.strip().split())
    card_value = 0

    for number in drawn_numbers:
        if number in winning_numbers:
            if card_value == 0:
                card_value = 1
            else:
                card_value *= 2
    point_total += card_value

print(point_total)