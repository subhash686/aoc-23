import os

nums = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

def calibration_sum(part: int):
    path = os.getcwd()
    file_path = os.path.join(path, 'day1.txt')
    filel = open(file_path, 'r')
    Lines = filel.readlines()
    sum = 0
    for line in Lines:
        current = line.strip()
        sum += get_num(current, part)
    print(sum)

def get_num(current: str, part: int) -> int:
    start = 0
    end = len(current) - 1
    tens = 0
    ones = 0

    while start <= end:
        if current[start].isdigit():
            tens = int(current [start])
            break
        if part == 2:
            num = word_to_num(current, start)
            if num > 0:
                tens = num
                break
        start += 1

    while end >= start:
        if current[end].isdigit():
            ones = int(current [end])
            break
        if part == 2:
            num = word_to_num_rev(current, start, end)
            if num > 0:
                ones = num
                break
        end -= 1

    cal = (tens * 10) + ones
    return cal

def word_to_num(current: str, index: int) -> int:
    for key, value in nums.items(): 
        if current.find(key, index) == index:
            return value
    return -1


def word_to_num_rev(current: str, start: int, end:int) -> int:
    for key, value in nums.items():
        if current.rfind(key, start, end+1) != -1 and current.rfind(key, start, end+1) + len(key)-1 == end:
            return value
    return -1

if __name__ == "__main__":
    calibration_sum(1)
    calibration_sum(2)
