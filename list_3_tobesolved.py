'''
5. Flatten Digits with a Generator
Task:
Write a function that, given a list of non-negative integers nums, returns a flat list of all their decimal digits in order. Use list.extend() with a generator expression to add each digit.

Goal:
Practice using extend() to consume a generator rather than a concrete iterable.

# Function signature
def flatten_digits(nums: List[int]) -> List[int]:
    ...

# Example 1
nums = [12, 305, 7]
# Process:
#   "12"  → digits 1, 2
#   "305" → digits 3, 0, 5
#   "7"   → digit  7
# Output: [1, 2, 3, 0, 5, 7]

# Example 2
nums = [0, 9, 10]
# Process:
#   "0"  → digits 0
#   "9"  → digits 9
#   "10" → digits 1, 0
# Output: [0, 9, 1, 0]

# Example 3
nums = []
# Output: []
'''
