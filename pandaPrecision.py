import panda
plot = panda.BambooPlot(
    'Precision',
    [2001, 1999, 1000]
)

# Don't change anything above this line
# ===================================

# generate your solution as a list of indices
# Optimal coded solution
queue = [0,1,0,2]

# ====================================
# Dont change anything below this line

# records your solution
plot.simulate(queue)
