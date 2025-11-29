"""
Q. Why does prefix sum work mathematically?
Ans:
prefix[R] includes all values from 0→R.
prefix[L-1] includes 0→L-1.
Subtracting removes the earlier part, leaving L→R.
"""

# Example in Python:
arr = [3, 5, 2, 8, 1]   # indices: 0  1  2  3  4

# Build prefix sum
prefix = [0] * len(arr)
prefix[0] = arr[0]
for i in range(1, len(arr)):
    prefix[i] = prefix[i-1] + arr[i]

# Query sum from L=1 to R=3 → elements = 5 + 2 + 8 = 15
L, R = 1, 3
range_sum = prefix[R] - (prefix[L-1] if L > 0 else 0)

print("Array:       ", arr)
print("Prefix Sum:  ", prefix)
print(f"Sum {L}→{R}:", range_sum)
# Explanation:
# prefix[3] = sum(0→3)
# prefix[0] = sum(0→0)
# prefix[3] - prefix[0] = (0→3) - (0→0) = (1→3)
