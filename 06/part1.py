import time

start_time = time.time()

grid = []

res1 = 0 
with open('input.txt', 'r') as infile:
    while line := infile.readline():
        line = line.strip()
        if not line:
            # it's a blank line
            continue
        vals = line.split()
        grid.append(vals)
          
    print(grid)

    rows = len(grid)
    for i, v in enumerate(grid[0]):
        operator = grid[-1][i]
        cur = 0
        if operator == '*':
            cur = 1
        for j in range(rows - 1):
            if operator == '*':
                cur *= int(grid[j][i])
            else:
                cur += int(grid[j][i])

        res1 += cur
            
print("Part 1: " + str(res1))
print("took %s seconds" % (time.time() - start_time))


# took  seconds
