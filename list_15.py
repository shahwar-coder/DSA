'''
. Filter Unique Values
Task:
Given a list of integers nums, return a new list containing only those elements that appear exactly once (i.e. “unique” values). Use count() to filter.

Goal:
Practice using count() in a list comprehension or loop to pick out items with frequency 1.
# Example 1
nums = [1, 2, 2, 3, 4, 4, 5]
# Frequencies: 1→1, 2→2, 3→1, 4→2, 5→1
# Unique values: [1, 3, 5]

# Example 2
nums = [7, 7, 7]
# Frequencies: 7→3 → no unique values → return []

# Example 3
nums = []
# Empty input → return []

'''
from typing import List
from collections import Counter
def unique_nums(nums: List[int])->List[int]:
    """
    Return all the unique numbers in the list, if no unique (occurring once) the return []
    """
    frequencies=Counter(nums)
    return [key for key, val in frequencies.items() if val==1]

def main():
    nums = [1, 2, 2, 3, 4, 4, 5]
    print(unique_nums(nums))

if __name__=="__main__":
    main()
