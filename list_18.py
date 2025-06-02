'''
2. Sort Tuples by Second Element Then First (Reverse Tiebreak)
Task:
Given a list of 2-tuples (x, y), where x and y are integers, sort in-place so that tuples are ordered by their second element y ascending, and if two tuples share the same y, the one with the larger first element x should come first.

Goal:
Learn how to build a key (or use a tuple with negative values) to handle tie-breaking in the reverse direction.

# Example 1
pairs = [(1, 2), (3, 1), (2, 2), (4, 1)]
# We want to sort by second element, then by larger first element if tied:
# Pairs with y=1: (3,1) and (4,1) → order them by x descending → (4,1), (3,1)
# Pairs with y=2: (1,2) and (2,2) → order by x descending → (2,2), (1,2)
# Final sorted: [(4,1), (3,1), (2,2), (1,2)]

# Example 2
pairs = [(0,0), (0,1), (1,0), (1,1)]
# y=0 group: (1,0) then (0,0)
# y=1 group: (1,1) then (0,1)
# Final: [(1,0), (0,0), (1,1), (0,1)]
'''
# Sort by key , if tie , break it furter.
from typing import List, Tuple
def sort_by_second_then_desc_first(pairs: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """Sort by second element ascending, then by first element descending (in-place)."""
    pairs.sort(key= lambda pair: (pair[1], -pair[0])) # so the first part is priority sorting and the next will be used for sorting when something is equal in first sorting. It's a power tool. And '-' sinifies and initiates a reverse/descending order.
    return pairs

def main():
    pairs = [(1, 2), (3, 1), (2, 2), (4, 1)]
    print(sort_by_second_then_desc_first(pairs))

if __name__=="__main__":
    main()



'''
✅ Tuple Sorting — Key-Based Sorting with Tie-Breaker Logic
❓ 1. Why do we use pair[1] as the first element in the sort key?
Answer:
We use pair[1] to sort the list in ascending order based on the second element of each tuple. This is the primary sort criterion.

❓ 2. Why do we use -pair[0] (the negative of the first element)?
Answer:
We use -pair[0] to achieve descending order sorting of the first element. Python’s sort() function sorts in ascending order by default, so by negating the number, we effectively reverse the sort for that component.

❓ 3. What does sort(key=lambda pair: (pair[1], -pair[0])) mean overall?
Answer:
This tells Python to:

Sort primarily by the second element of the tuple (pair[1]) in ascending order.

If two tuples have the same second element, then sort by the first element (pair[0]) in descending order.

This is an example of lexicographical tuple sorting where multiple levels of sorting logic are combined in one expression.

❓ 4. Why is it better to use a single .sort() call with a tuple key instead of calling .sort() twice?
Answer:
Calling .sort() twice can override the result of the previous sort unless you're careful. Although Python’s .sort() is stable (preserves order when values are equal), using a single sort() with a compound key is more efficient, concise, and reliable. It performs all necessary comparisons in one pass, making it the preferred and professional approach.
'''
