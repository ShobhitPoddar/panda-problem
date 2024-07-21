// Growth rates of the trees
const growthRates = [16, 8, 4, 2, 1, 1];

// Initialize the tree with initial growth rates
let tree = [...growthRates];

// Create initial arrays
const size = growthRates.length;
let firstArr = [0];
let lastArr = [1];

// Initialize an empty queue
let queue = [];

// Main loop
while ((queue.indexOf(size - 1) === -1) || (JSON.stringify(lastArr) !== JSON.stringify(firstArr))) {
    // Step 1: Pick the largest value from the tree array
    const maxIndex = tree.indexOf(Math.max(...tree));
    if (queue.length >= 1 && maxIndex === queue[queue.length - 1]) {
        queue.push(maxIndex + 1);
    } else {
        queue.push(maxIndex);
    }
    // Step 3: Set the picked value to 0 in the tree array
    tree[maxIndex] = 0;

    // Step 4: Add the growth rates index value to the tree after every loop
    for (let i = 0; i < tree.length; i++) {
        tree[i] += growthRates[i];
    }

    // Update firstArr and lastArr after the loop
    if (queue.length > size) {
        firstArr = queue.slice(0, size);
        lastArr = queue.slice(-size);
    }
}

console.log("First Array:", firstArr);
console.log("Last Array:", lastArr);
console.log("Queue:", queue);
