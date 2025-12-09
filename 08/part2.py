import time

start_time = time.time()

res1 = 0 
all_boxes = []

with open('input.txt', 'r') as infile:
    while line := infile.readline():
        line = line.strip()
        if not line:
            # it's a blank line
            continue
        x, y, z = map(int, line.split(','))
        all_boxes.append((x, y, z))
    
    size = len(all_boxes)
    # (distance, i, j)
    distances = [] 
    for i in range(size):
        x1, y1, z1 = all_boxes[i]
        for j in range(i+1, size):
            x2, y2, z2 = all_boxes[j]
            dx, dy, dz = x1 - x2, y1 - y2, z1 - z2
            distance = dx * dx + dy * dy + dz * dz
            distances.append((distance, i, j))

    # sort the distances 
    distances.sort(key=lambda e: e[0])
    parent = list(range(size)) # stores the direct parent
    count = [1] * size

    def get_parent(box_id):
        # until I get to the root
        while parent[box_id] != box_id:
            box_id = parent[box_id]
        return box_id

    def union(x,y):
        # connect y into x (y --> x)
        parent_x, parent_y = get_parent(x), get_parent(y)
        if parent_x == parent_y:
            return False
        # attach the root of one to another
        if count[parent_x] < count[parent_y]:
            parent_x, parent_y = parent_y, parent_x
        parent[parent_y] = parent_x
        count[parent_x] += count[parent_y]
        return True

    total_circuits = size
    last_i, last_j = 0, 0 

    for idx, (_, x, y) in enumerate(distances): 
        if union(x,y):
            total_circuits -= 1
            last_i, last_j = x, y
            if total_circuits == 1:
                break

    x1 = all_boxes[last_i][0]
    x2 = all_boxes[last_j][0]

    res1 = x1 * x2 
        

print("Part 2: " + str(res1))
print("took %s seconds" % (time.time() - start_time))

# took 0.011965274810791016 seconds
