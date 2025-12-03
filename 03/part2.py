import time

start_time = time.time()

res2 = 0 
iteration = 0

def getNextBiggestDigit(arr, start, end):
    biggest = -1
    index = -1
    for idx in range(start, end):
        cur = int(arr[idx])
        if cur > biggest:
            biggest = cur
            index = idx
    return biggest, index

# reusing my part1
with open('input.txt', 'r') as infile:
    while line := infile.readline():
        if not line.strip():
            # skip blank lines
            continue
        line = line.rstrip()
        size = len(line)

        iteration += 1
        needed = 12
        index = -1
        bank = ""
        while needed > 0:
            biggest, index = getNextBiggestDigit(line, index + 1, size - needed + 1)
            bank += str(biggest)
            needed -= 1

        res2 += int(bank)
                
        print("line ("+str(iteration)+") -> " + str(bank))
print("Part 2: " + str(res2))
print("took %s seconds" % (time.time() - start_time))


# took 0.003597736358642578 seconds
