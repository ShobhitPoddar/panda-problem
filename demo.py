# Growth rates of the trees
growth_rates =  [2001, 1999, 1000]

# Initialize the tree with initial growth rates
tree = growth_rates.copy()

# Create initial arrays
size = len(growth_rates) 
first_arr = [0] * size
last_arr = [1] * size

# Initialize an empty queue
queue = []

# print("First Array:", first_arr)
# print("Last Array:", last_arr)

# Main loop
while (size-1 not in queue):
    # Step 1: Pick the largest value from the tree array
    max_index = tree.index(max(tree))
    if len(queue) >= 1 and max_index == queue[-1]:
        max_index = max_index + 1
        # print(max_index)
    # Step 2: Save the index value in the queue
    queue.append(max_index)
    # Step 3: Set the picked value to 0 in the tree array
    tree[max_index] = 0 
    # print("Tree :" + str(tree))
    # Step 4: Add the growth rates index value to the tree after every loop
    for i in range(len(tree)):
        # print("Tree :" + str(tree))
        tree[i] += growth_rates[i]
        # print("Tree :" + str(tree))
        # print("Queue :" + str(queue))

    # Update first_arr and last_arr after the loop
    if (len(queue)>size):
     first_arr = queue[:size]
     last_arr = queue[-size:]

print("First Array:", first_arr)
print("Last Array:", last_arr)
print("Queue:", queue)


