print(max([sum([int(line) for line in group.split("\n")]) for group in open("./input.txt", "r").read().split("\n\n")]))