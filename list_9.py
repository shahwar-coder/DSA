'''
4. Deduplicate In-Place
Task:
Given a list of integers nums, remove all duplicates in-place so that each value appears only once, preserving the first occurrence order. You must use remove() (you may not create a new list via comprehension).

Goal:
Practice in-place mutation with remove(), careful looping, and index management.

# Example 1
nums = [1, 2, 1, 3, 2, 4]
# After dedup: [1, 2, 3, 4]

# Example 2
nums = [5, 5, 5, 5]
# After dedup: [5]

# Example 3
nums = []
# After dedup: []
'''
# NOTE: I am not using forcible remove or index management because it will be unnecarry bit more thinking, rather using set for keeping record and faster search in it and list result to store in order the desired items.
from typing import List
def remove_duplicates(nums: List[int])->List[int]:
    """
    Return a new list preserving the first occurrence of each element from `nums`.
    Uses a set for O(1) membership tests.
    """
    # seen=[] #list traversals slow, sets traversal fast but no order, dicts would be good, eg using fromkeys, bcz keys cannot be duplicated
    seen_set = set()
    result: List[int] = []
    for num in nums:
        if num not in seen_set:
            seen_set.add(num) #O(1) #helps making traversal faster
            result.append(num) #O(1) #helps keeping the order
    return result

def main():
    nums = [1, 2, 1, 3, 6, 2, 4, 3, 5, 3]
    print(remove_duplicates(nums))

if __name__=="__main__":
    main()
