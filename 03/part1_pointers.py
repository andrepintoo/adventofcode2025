import time

start_time = time.time()

res1 = 0 
iteration = 0
with open('input.txt', 'r') as infile:
    while line := infile.readline():
        if not line.strip():
            # skip blank lines
            continue
        line = line.rstrip()
        size = len(line)
        biggest_decimals = {}
        biggest = 0

        iteration += 1
        # start looking until the penultimate number
        for idx in range(0, size - 1):
            cur = int(line[idx])
            if cur >= biggest:
                if biggest_decimals and cur != biggest:
                    biggest_decimals.pop(biggest)
                biggest = cur
                if cur not in biggest_decimals:
                    biggest_decimals[cur] = []
                biggest_decimals[cur].append(int(idx))

        if len(biggest_decimals[biggest]) > 1 and int(line[size-1]) <= biggest:
            val = (biggest * 10) + biggest
            res1 += val
             # print("line ("+str(iteration)+") -> " + str(val))
            continue

        second_biggest = 0
        for i in range(biggest_decimals[biggest][0]+1, size):
           cur = int(line[i])
           if cur > second_biggest:
            second_biggest = cur
        line_biggest_number = (biggest * 10) + second_biggest
        res1 += line_biggest_number
        # print("line ("+str(iteration)+") -> " + str(line_biggest_number))
print("Part 1: " + str(res1))
print("took %s seconds" % (time.time() - start_time))


# took 0.003597736358642578 seconds
