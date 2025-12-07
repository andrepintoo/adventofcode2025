import time

start_time = time.time()

res1 = 0 
grid = []
with open('input.txt', 'r') as infile:
    while line := infile.readline():
        line = line.strip()
        if not line:
            # it's a blank line
            continue
        grid.append(list(line))

    splitterIdx = -1
    for i, v in enumerate(grid[0]):
        if v == 'S':
            splitterIdx = i
            break

    beams = {}
    print(splitterIdx)
    beams[splitterIdx] = True
    for i, v in enumerate(grid):
        if i == 0:
            continue
        
        for b in list(beams.keys()):
            beam_pos_value = v[b]
            if beam_pos_value == '.':
                v[b] = '|'
                continue
            if beam_pos_value == '^':
                del beams[b]
                res1 += 1
                if b-1 >= 0 and v[b-1] != '|':
                    beams[b-1] = True
                if b+1 < len(grid[0]) and v[b+1] != '|':
                    beams[b+1] = True
          
        print(v)
print("Part 1: " + str(res1))
print("took %s seconds" % (time.time() - start_time))


# took 0.011965274810791016 seconds
