dial = 50
res1, res2 = 0, 0

with open('input.txt', 'r') as infile:
    while line := infile.readline():
        if not line.strip():
            # skip blank lines
            continue
        cur = line.rstrip()
        move = cur[0]
        number = int(cur[1:])
        aux = dial
        times = number // 100
        res2 += times

        missing_steps = number % 100

        if move == 'L':
            if aux > 0 and missing_steps - aux >= 0:
                res2 += 1
            dial = (dial - missing_steps) % 100
        else:
            if aux > 0 and missing_steps + aux >= 100:
                res2 += 1
            dial = (dial + missing_steps) % 100

        if dial == 0:
            res1 += 1

print("Part 1: " + str(res1))
print("Part 2: " + str(res2))
