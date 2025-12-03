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
        biggest = -1
        iteration +=1
        total = -1
        for i in range(size-1):
            second_biggest = -1
            cur = int(line[i])
            if cur <= biggest:
                continue
            
            biggest = cur
            for j in range(i+1, size):
                cur2 = int(line[j])
                if cur2 <= second_biggest:
                    continue
                second_biggest = cur2
            val = (biggest * 10) + second_biggest
            if val > total:
                total = val
        # print("line ("+str(iteration)+") -> " + str(total))
              
        res1 += total

print("Part 1: " + str(res1))

print("took %s seconds" % (time.time() - start_time))


# took 0.00976872444152832 seconds
