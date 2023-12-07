import os

def ways_to_win(part):
    path = os.getcwd()
    file_path = os.path.join(path, "day6.txt")
    filel = open(file_path, 'r')
    Lines = filel.readlines()
    
    sum = 1
    if part == 1:
        times, distance = parse_par1(Lines)
    else:
        times, distance = parse_par2(Lines)
    print(times)
    print(distance)

    for x in range(1, len(times)):
        time = int(times[x])
        dist = int(distance[x])
        half = int(time/2)

        left = half
        right =half + 1
        count = 0
        if time%2==0 and left * left > dist:
            count =1
            left -= 1
            right = left + 2
        while left * right > dist:
            count += 2
            left -= 1
            right += 1
        sum *= count

    print(sum)


def parse_par1(Lines):
    line = Lines[0]
    times = line.split()
    line = Lines[1]
    distance = line.split()
    return times, distance

def parse_par2(Lines):
    line = Lines[0]
    times = ("").join(line.split()).split(":")
    line = Lines[1]
    distance = ("").join(line.split()).split(":")
    return times, distance

if __name__ == "__main__": 
    ways_to_win(1)
    ways_to_win(2)
