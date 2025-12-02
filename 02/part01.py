res1 = 0 

with open('input.txt', 'r') as infile:
    while line := infile.readline():
        if not line.strip():
            # skip blank lines
            continue
        inputs = line.split(",")
        for input in inputs:
            # input = "11-22"
            splitted = input.split("-")
            x, y = int(splitted[0]), int(splitted[1])
            for n in range(x, y+1):
                # n = 11
                n_str = str(n)
                n_digits = len(n_str)
                if n_digits % 2 == 1:
                    # an odd length will never be an invalid Id
                    continue
                if n_str[:n_digits//2] == n_str[n_digits//2:]:
                    res1 += n
        
print("Part 1: " + str(res1))
