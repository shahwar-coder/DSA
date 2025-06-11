'''
🔷 NumPy Indexing Insight
Given NumPy Array:

import numpy as np

data = np.array([
    [100, 200, 300],
    [400, 500, 600],
    [700, 800, 900]
])

Your tasks:

What values will col and row contain?

Why do data[..., 1] and data[:, 1] behave the same way here?

Why does data[1, ...] return something different from data[..., 1]?

📘 This tests:

Your understanding of dimensional slicing,

How ellipsis adapts to dimensions automatically,

And how to visualize array indexing clearly.
'''

import numpy as np

data = np.array([
    [100, 200, 300],
    [400, 500, 600],
    [700, 800, 900]
])

col = data[..., 1]
row = data[1,...]

print(col) # [200 500 800]
print(row) # [400 500 600]


# What values will col and row contain?
# => Values are : col = [200 500 800] , row = [400 500 600]
# => col = data[..., 1] → selects the second column from each row → [200 500 800]
# => row = data[1, ...] → selects the entire second row → [400 500 600]

# Why do data[..., 1] and data[:, 1] behave the same way here?
# => data[:,1] and data[...,1] will behave the same way, as "it is 2D array and ... is expanded to :" for the remaining axes.
# => They both will return second column here.

# Why does data[1, ...] return something different from data[..., 1]?
# => They are different as one deals with col and the other with row.
# => data[1, ...] → fixed row, variable column, data[..., 1] → variable row, fixed column

