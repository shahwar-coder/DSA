'''
Q. What is the common loop structure for fixed-window problems?
Ans:
Build the first window, then from i=k to n-1 update the window by:
   subtracting arr[i-k],
   adding arr[i].
'''
# Example:
# For i in range(k, n):
#   sum += arr[i] - arr[i-k]
# ============================
# Example Explanation:

# arr = [4, 2, 1, 7, 3]
# k = 3

# STEP 1 — Build the first window:
# Window = [4, 2, 1]
# Sum = 4 + 2 + 1 = 7

# We now slide the window using:
# for i in range(k, n):

# ------------------------------
# Iteration 1 → i = 3
# New element entering  = arr[3] = 7
# Element leaving       = arr[0] = 4

# Apply formula:
# window_sum = 7 + 7 - 4 = 10

# New window = [2, 1, 7]
# New sum    = 10
# ------------------------------

# Iteration 2 → i = 4
# New element entering  = arr[4] = 3
# Element leaving       = arr[1] = 2

# Apply formula:
# window_sum = 10 + 3 - 2 = 11

# New window = [1, 7, 3]
# New sum    = 11
# ------------------------------

# Final Summary:
# Start:    [4,2,1] → 7
# Slide #1: [2,1,7] → 10
# Slide #2: [1,7,3] → 11
