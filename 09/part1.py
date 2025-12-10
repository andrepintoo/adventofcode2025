import time

start_time = time.time()

res1 = 0 
tiles = []
with open('input.txt', 'r') as infile:
    while line := infile.readline():
        line = line.strip()
        if not line:
            # it's a blank line
            continue
        values = line.split(',')
        y, x = int(values[0]), int(values[1])
        tiles.append((y,x))
    
    biggest = 0
    size = len(tiles)
    for i, v in enumerate(tiles):
        for j in range(i+1, size):
            cur = (v[0] - tiles[j][0] + 1) * (v[1] - tiles[j][1] + 1)
            if cur > biggest:
                biggest = cur

    res1 = biggest
print("Part 1: " + str(res1))
print("took %s seconds" % (time.time() - start_time))

# took 0.02652263641357422 seconds
