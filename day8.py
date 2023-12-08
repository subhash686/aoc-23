import os
from math import lcm

SOURCE = "AAA"
DEST = "ZZZ"

def navigate(part):
    path = os.getcwd()
    file_path = os.path.join(path, 'day8.txt')
    filel = open(file_path, 'r')
    Lines = filel.readlines()
    dirs = Lines[0].strip()
    graph = {}
    for l in range(2,len(Lines)):
        node = Lines[l].split("=")
        parent = node[0].strip()
        children = node[1].split(",")
        left = children[0][2:5]
        right = children[1][1:4]
        graph[parent] = [left, right]
    
    count = traverse_multiverse(graph, dirs, part)

    print(count)


def traverse_multiverse(graph, dirs, part):
    sources = get_sources(graph, part)
    counts = []
    for next in sources:
        count = 0
        d = 0
        while d < len(dirs):
            ind = 0 if dirs[d] == "L" else 1
            count += 1
            
            next = graph.get(next)[ind]
            if (part == 1 and next == "ZZZ") or next.endswith("Z"):
                break
            if d == len(dirs) - 1:
                d = 0
            else:
                d += 1
        counts.append(count)
    
    return lcm(*counts)

def get_sources(graph, part):
    if part == 1:
        return [SOURCE]
    
    sources = []
    for node in graph.keys():
        if node[2] == 'A':
            sources.append(node)
    return sources


if __name__ == "__main__":
    navigate(1)
    navigate(2)
