import panda
import itertools
plot = panda.BambooPlot(
    'MoreOdds',
    [9, 7, 7, 5, 5, 3, 3, 3]
)

# Don't change anything above this line
# ===================================

# generate your solution as a list of indices
queue = [0,1,2,3,0,4,1,2,0,5,6,7]

# ====================================
# Dont change anything below this line

# records your solution
plot.simulate(queue)
