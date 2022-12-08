values = {
    "X": 1,
    "Y": 2,
    "Z": 3
}
outcomes = {
    "A": {
        "X": 3,
        "Y": 6,
        "Z": 0
    }, 
    "B": {
        "X": 0,
        "Y": 3,
        "Z": 6
    },
    "C": {
        "X": 6,
        "Y": 0,
        "Z": 3
    }
}
# strategy: tuple[str, str] = [(line, line) for line in open("day-2/input.txt", "r").read().split("\n")];
strategy: tuple[str, str] = [(line[0], line[2]) for line in open(
    "day-2/input.txt", "r").read().split("\n")]
print(sum([values[line[1]] + outcomes[line[0]][line[1]] for line in strategy]))

