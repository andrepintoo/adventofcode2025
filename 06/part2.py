import time

start_time = time.time()

grid = []
indexes = {}
res2 = 0 
with open('input.txt', 'r') as infile:
    while line := infile.readline():
        if not line.strip():
            # it's a blank line
            continue
        grid.append(line)
        val = line.strip()
        if not val[0].isdecimal():
            for i, v in enumerate(line):
                if v == '*' or v == '+':
                    indexes[i] = True

    rows = len(grid)
    currentNumber = ''
    currentOperator = ''
    currentOperation = []
    size = len(grid[0])
    for i, v in enumerate(grid[0]):
        # finished with an operation
        if (i + 1) in indexes or i == size - 1:
            cur = 0
            if currentOperator == '*':
                cur = 1
            for number in currentOperation:
                if currentOperator == '*':
                    cur *= number
                else:
                    cur += number

            res2 += cur
            currentOperation = []
            continue

        if i in indexes:
            currentOperator = grid[-1][i]
        
        currentNumber = ''
        for j in range(rows - 1):
            if grid[j][i].isdigit():
                currentNumber += grid[j][i]

        if currentNumber != '':
            currentOperation.append(int(currentNumber))
            
print("Part 2: " + str(res2))
print("took %s seconds" % (time.time() - start_time))

# took 0.006444692611694336 seconds
