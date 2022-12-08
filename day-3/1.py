input = open("day-3/input.txt").read()
def item_prio(char: chr) -> int :
    if (ord(char) >= ord("a") and ord(char) <= ord("z")):
        return ord(char) - ord("a") + 1;
    if (ord(char) >= ord("A") and ord(char) <= ord("Z")):
        return ord(char) - ord("A") + 27;
    raise Exception("Invalid item type");
sum = 0;
lines = [ list(line) for line in input.split("\n")]
for line in lines:
    sack_size = int(len(line) / 2)
    first = line[0 : sack_size]
    second = line[-sack_size : ]
    intersection = set(first).intersection(set(second)).pop()
    sum += item_prio(intersection)
print(sum)