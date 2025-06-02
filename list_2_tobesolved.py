'''
4. Merge K Sorted Lists
Task:
You’re given a list of k sorted integer lists, lists = [L₀, L₁, …, Lₖ₋₁]. Merge them into a single sorted list result by first extending result with each Li in turn, then performing a single in-place sort() at the end.

Goal:
Practice using extend() to accumulate multiple sorted sequences, and then efficiently restoring global order with one sort.

# Example 1
lists = [[1, 4, 9], [2, 6], [3, 5, 7]]
# Step 1: result = []; 
#   extend([1,4,9]) → [1,4,9]
#   extend([2,6])   → [1,4,9,2,6]
#   extend([3,5,7]) → [1,4,9,2,6,3,5,7]
# Step 2: result.sort()
# Final: [1,2,3,4,5,6,7,9]

# Example 2
lists = [[], [10, 20], [5]]
# Flatten then sort → [5,10,20]

# Example 3
lists = [[-1, 0], [-3, 3], [2]]
# Flatten then sort → [-3,-1,0,2,3]
'''
