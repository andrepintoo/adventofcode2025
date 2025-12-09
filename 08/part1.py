import time

start_time = time.time()

res1 = 0 
all_boxes = []
k = 1000

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

    for idx, (_, x, y) in enumerate(distances): 
        if idx == k:
            break
        # connect y into x (y --> x)
        parent_x, parent_y = get_parent(x), get_parent(y)
        if parent_x == parent_y:
            continue
        # attach the root of one to another
        if count[parent_x] < count[parent_y]:
            parent_x, parent_y = parent_y, parent_x
        parent[parent_y] = parent_x
        count[parent_x] += count[parent_y]
        
    # count how many boxes belong to each circuit
    circuits = {}
    for i in range(size):
        root = get_parent(i)
        circuits[root] = circuits.get(root, 0) + 1
    
    sizes = sorted(circuits.values(), reverse=True)

    res1 = sizes[0] * sizes[1] * sizes[2]

print("Part 1: " + str(res1))
print("took %s seconds" % (time.time() - start_time))

# took 0.011965274810791016 seconds
