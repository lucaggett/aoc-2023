import re

total = 0

with open('input.txt') as file:
    for line in file:
        nums = re.findall("(\d|one|two|three|four|five|six|seven|eight|nine)", line)
        nums_map = {
            "one": 1, "two": 2, "three": 3, "four": 4, 
            "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
            }
        for idx, num in enumerate(nums[:]):
            if num in nums_map:
                nums[idx] = str(nums_map[num])
        total += int(nums[0] + nums[-1])

print(total)
