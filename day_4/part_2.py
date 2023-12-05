data = open('input.txt').read().splitlines()
card_total = 0
card_counts = {}


def get_winning_total(card: str) -> int:
    card_num, numbers = card.split(":")
    winning_numbers, drawn_numbers = numbers.split("|")
    winning_numbers = set(int(number) for number in winning_numbers.strip().split())
    drawn_numbers = set(int(number) for number in drawn_numbers.strip().split())
    card_value = 0

    for number in drawn_numbers:
        if number in winning_numbers:
            card_value += 1
    return card_value


for idx, line in enumerate(data):
    card_value = get_winning_total(line)
    card_total += card_value
    card_counts[idx] = card_value
