import panda
plot = panda.BambooPlot(
    'Power',
    [16, 8, 4, 2, 1, 1]
)

# Don't change anything above this line
# ===================================
# Growth rates of the trees
growth_rates =  [16, 8, 4, 2, 1, 1]

# Initialize the tree with initial growth rates
tree = growth_rates.copy()

# Create initial arrays
size = len(growth_rates) 
first_arr = [0]
last_arr = [1] 

# Initialize an empty queue
queue = []
max_queue =[]
# print("First Array:", first_arr)
# print("Last Array:", last_arr)

# Main loop
while (size-1 not in queue):
    # Step 1: Pick the largest value from the tree array
    max_index = tree.index(max(tree))
    if len(queue) >= 1 and max_index == queue[-1]:
        max_queue.append(max_index)
        if len(queue) > 2 and ((max_queue[-1]) == max_index):
           print (max_index)
           next_max_value = max(tree[max_index + 1:])
           max_index = 1 + tree.index(next_max_value)
           print("Index of next maximum value:", max_index)
           print("Next maximum value:", next_max_value)
        else:
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
# elements start from infinity so remove first duplicated elements.
queue = queue[2:] 

#code solutiom
# queue = [0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0, 4, 0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 5] 
# [0,1,0,2,0,1,0,3,0,1,0,2,0,1,0,4,0,1,0,2,0,1,0,5] pen-paper

# ====================================
# Dont change anything below this line

# records your solution
plot.simulate(queue)
