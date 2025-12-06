import time

start_time = time.time()

intervals = []
ranges = {}

res1 = 0 
isFirstPart = True
with open('input.txt', 'r') as infile:
    while line := infile.readline():
        if not line.strip():
            # it's a blank line
            isFirstPart = False
            intervals.sort()
            continue
        
        if isFirstPart:
            x, y = line.split('-')
            start, end = int(x), int(y)
            intervals.append(start)
            if start in ranges:
                ranges[start] = max(ranges[start], end)
            else:
                ranges[start] = end
            continue
        
        cur = int(line)
        for v in intervals:
            if cur >= v and cur <= ranges[v]:
                res1 += 1
                break
            
print("Part 1: " + str(res1))
print("took %s seconds" % (time.time() - start_time))


# took  seconds
