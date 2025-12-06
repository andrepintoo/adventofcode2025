import time

start_time = time.time()

intervals = []
ranges = {}
newIntervals = []
newRanges = {}
res2 = 0 
isFirstPart = True
with open('input.txt', 'r') as infile:
    while line := infile.readline():
        if not line.strip():
            # it's a blank line
            isFirstPart = False
            intervals.sort()
            
            # make sure no interval overlaps another one
            newIntervals.append(intervals[0])
            newRanges[intervals[0]] = ranges[intervals[0]]
            for i in range(1, len(intervals), 1):
                cur = intervals[i]
                prev = newIntervals[-1]

                if cur <= newRanges[prev]:
                    newRanges[prev] = max(ranges[prev], ranges[cur])
                    continue
                newIntervals.append(cur)
                newRanges[cur] = ranges[cur]

            for v in newIntervals:
                res2 += newRanges[v] - v + 1
            break
        
        if isFirstPart:
            x, y = line.split('-')
            start, end = int(x), int(y)
            intervals.append(start)
            if start in ranges:
                ranges[start] = max(ranges[start], end)
            else:
                ranges[start] = end
            continue
            
print("Part 2: " + str(res2))
print("took %s seconds" % (time.time() - start_time))

# took 0.002724170684814453 seconds
