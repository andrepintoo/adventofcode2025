import time

start_time = time.time()

res2 = 0 
grid = []
with open('input.txt', 'r') as infile:
    while line := infile.readline():
        line = line.strip()
        if not line:
            # it's a blank line
            continue
        grid.append(list(line))

    beams = {}
    for i, v in enumerate(grid[0]):
        if v == 'S':
            beams[i] = 1
            continue
        beams[i] = 0

    for i, curLine in enumerate(grid):
        if i == 0:
            continue
        
        for b in list(beams.keys()):
            timelines = beams[b]
            if timelines == 0:
                continue

            beam_pos_value = curLine[b]
            if beam_pos_value == '.':
                curLine[b] = '|'
                continue

            if beam_pos_value == '^':
                if b-1 >= 0:
                    beams[b-1] += timelines
                if b+1 < len(grid[0]):
                    beams[b+1] += timelines
                beams[b] = 0
          
    for _, v in beams.items():
        res2 += v 

print("Part 2: " + str(res2))
print("took %s seconds" % (time.time() - start_time))

# took 0.003591299057006836 seconds
