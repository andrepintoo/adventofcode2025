import time

start_time = time.time()

res2 = 0 
tiles = []
with open('input.txt', 'r') as infile:
    while line := infile.readline():
        line = line.strip()
        if not line:
            # it's a blank line
            continue
        values = line.split(',')
        # row, column
        y, x = int(values[0]), int(values[1])
        tiles.append((y,x))
    
    def getConnectingCoordinates(y2,y1,x2,x1):
        res = [] 
        if y1 == y2:              # horizontal
            min_x, max_x = min(x1, x2), max(x1, x2)
            for xx in range(min_x + 1, max_x):  # tiles strictly between red ones
                res.append((y1, xx))
        elif x1 == x2:            # vertical
            min_y, max_y = min(y1, y2), max(y1, y2)
            for yy in range(min_y + 1, max_y):
                res.append((yy, x1))
       
        return res

    limits = set(tiles)
    size = len(tiles)
    # build boundary lines
    for i in range(size):
        y1, x1 = tiles[i]
        y2, x2 = tiles[(i+1) % size] 
        limits.update(getConnectingCoordinates(y2, y1, x2, x1))
    
    # get inside tiles
    ys = [y for (y, x) in limits]
    xs = [x for (y, x) in limits]
    min_y, max_y = min(ys), max(ys)
    min_x, max_x = min(xs), max(xs)
    for yy in range(min_y, max_y + 1):
        row_xs = sorted(x for (y, x) in limits if y == yy)
        if len(row_xs) < 2:
            continue
        for xx in range(row_xs[0] + 1, row_xs[-1]):
            if (yy, xx) not in limits:
                limits.add((yy, xx))

    biggest = 0
    for i, v in enumerate(tiles):
        for j in range(i+1, size):
            cur = abs(v[0] - tiles[j][0] + 1) * abs(v[1] - tiles[j][1] + 1)
            if cur > biggest:
                y1,x1 = tiles[i]
                y2,x2 = tiles[j]
                min_y, max_y = min(y1, y2), max(y1, y2)
                min_x, max_x = min(x1, x2), max(x1, x2)
   
                ok = True
                for yy in range(min_y, max_y + 1):
                    for xx in range(min_x, max_x + 1):
                        if (yy, xx) not in boundaries:
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    biggest = cur

    res2 = biggest
print("Part 2: " + str(res2))
print("took %s seconds" % (time.time() - start_time))

# took 0.02652263641357422 seconds
