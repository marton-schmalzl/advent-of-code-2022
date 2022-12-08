values = {
    "A": 1,
    "B": 2,
    "C": 3
}
outComeValues = {
    "X": 0,
    "Y": 3,
    "Z": 6
}
outcomes = {
    "A": {
        "X": "C",
        "Y": "A",
        "Z": "B"
    }, 
    "B": {
        "X": "A",
        "Y": "B",
        "Z": "C"
    },
    "C": {
        "X": "B",
        "Y": "C",
        "Z": "A"
    }
}
# strategy: tuple[str, str] = [(line, line) for line in open("day-2/input.txt", "r").read().split("\n")];
strategy: list[tuple[str, str]] = [(line[0], line[2]) for line in open(
    "day-2/input.txt", "r").read().split("\n")]
# strategy = [
#     ("A", "Y"),
#     ("B", "X"),
#     ("C", "Z")
#     ]
# strategy = [
#     ("B", "X"),
# ]
# line = ("B", "X")
# print (outcomes[line[0]][line[1]])
print(sum([outComeValues[line[1]] + values[outcomes[line[0]][line[1]]] for line in strategy]))

