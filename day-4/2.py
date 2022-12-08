input = open("day-4/input.txt").read()
lines = [ [{"start": int(zone.split("-")[0]), "end": int(zone.split("-")[1])} for zone in (line).split(",")] for line in input.split("\n")]
cnt = 0;
for line in lines:
    left, rigth = line
    if (left['start'] <= rigth['start'] and left['end'] >= rigth['start']) or (rigth['start'] <= left['start'] and rigth['end'] >= left['start']):
        cnt+=1

print(cnt)