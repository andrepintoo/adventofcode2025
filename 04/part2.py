import time

start_time = time.time()

res2 = 0 
grid = []

def countAdjacentRolls(matrix, row, col, totalR, totalC) -> int:
    count = 0
    
    directions = [
        (-1,-1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    for dr, dc in directions:
        newRow, newCol = row + dr, col + dc
        if 0 <= newRow < totalR and 0 <= newCol < totalC:
            if matrix[newRow][newCol] == '@':
                count += 1

    return count

with open('input.txt', 'r') as infile:
    while line := infile.readline():
        if not line.strip():
            # skip blank lines
            continue
        line = line.rstrip()
        grid.append(list(line))
    totalRows, totalCols = len(grid), len(grid[0])
    cleaningNeeded = True
    while cleaningNeeded:
        cleaningNeeded = False
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == '@' and countAdjacentRolls(grid, i, j, totalRows, totalCols) < 4: 
                    grid[i][j] = '.'
                    res2 += 1
                    cleaningNeeded = True

print("Part 2: " + str(res2))
print("took %s seconds" % (time.time() - start_time))


# took 0.1364338397979736 seconds
