import time

start_time = time.time()

res1 = 0 
iteration = 0
grid = []

def countAdjacentRolls(matrix, row, col, totalR, totalC) -> int:
    count = 0
    if row > 0:
        if matrix[row-1][col] == '@':
            count += 1
        if col > 0 and matrix[row-1][col-1] == '@':
            count += 1
        if col < totalC - 1 and matrix[row-1][col+1] == '@':
            count += 1
    if row < totalR - 1:
        if matrix[row+1][col] == '@':
            count += 1
        if col > 0 and matrix[row+1][col-1] == '@':
            count += 1
        if col < totalC - 1 and matrix[row+1][col+1] == '@':
            count+=1
    if col > 0 and matrix[row][col-1] == '@':
        count += 1 
    if col < totalC - 1 and matrix[row][col+1] == '@':
        count += 1 
    return count

with open('input.txt', 'r') as infile:
    while line := infile.readline():
        if not line.strip():
            # skip blank lines
            continue
        line = line.rstrip()
        grid.append(line)
    totalRows, totalCols = len(grid), len(grid[0])
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == '@' and countAdjacentRolls(grid, i, j, totalRows, totalCols) < 4: 
                res1 += 1

print("Part 1: " + str(res1))
print("took %s seconds" % (time.time() - start_time))


# took 0.003597736358642578 seconds
