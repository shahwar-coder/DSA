"""
Q. How do you build a prefix-sum array?
Ans:
Set prefix[0] = arr[0].
For every i > 0:
prefix[i] = prefix[i-1] + arr[i]
"""

# Example in Python:
arr = [2, 4, 6, 1]

prefix = [0] * len(arr)
prefix[0] = arr[0]

for i in range(1, len(arr)):
    prefix[i] = prefix[i-1] + arr[i]

print("Array:         ", arr)
print("Prefix Sum:    ", prefix)
# Example: prefix[2] = prefix[1] + arr[2] → 6 + 6 = 12
