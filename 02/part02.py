res2 = 0 

def isInvalid(number: int) -> bool:
    n_string = str(number)
    totalSize = len(n_string)

    # +1 to account for odd lengths
    for patternSize in range(1, totalSize // 2 + 1):
        # since the total word needs to be repeated evenly, we can discard these cases
        if totalSize % patternSize != 0:
            continue

        block = n_string[:patternSize]
        repeats = totalSize // patternSize

        # block = "12"
        # block * repeats = "12121212"
        if repeats >= 2 and block * repeats == n_string:
            return True
    return False

with open('input.txt', 'r') as infile:
    while line := infile.readline():
        if not line.strip():
            # skip blank lines
            continue
        inputs = line.split(",")
        for input in inputs:
            splitted = input.split("-")
            x, y = int(splitted[0]), int(splitted[1])
            for n in range(x, y+1):
                if isInvalid(n):
                    res2 += n
        
print("Part 1: " + str(res2))
