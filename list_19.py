'''
3. Sort Numbers by Distance from a Pivot
Task:
You have a list of distinct integers nums and a pivot integer pivot. Sort nums in-place so that numbers nearest to pivot come first. If two numbers are equally distant from pivot, the smaller number (numerically) should come first.

Goal:
Practice writing a key function that measures “distance,” and then breaks ties by comparing the value itself.

# Example 1
nums = [10, 4, 7, 1, 13]
pivot = 8
# Distances from 8:  |10–8|=2, |4–8|=4, |7–8|=1, |1–8|=7, |13–8|=5
# Sort by ascending distance, then by numerical tie-break:
#  distance 1 → 7
#  distance 2 → 10
#  distance 4 → 4
#  distance 5 → 13
#  distance 7 → 1
# Final: [7, 10, 4, 13, 1]

# Example 2
nums = [5, 9, 11, 3]
pivot = 7
# Distances: |5–7|=2, |9–7|=2, |11–7|=4, |3–7|=4
# Ties for distance 2 → pick smaller first: 5 then 9
# Ties for distance 4 → pick smaller first: 3 then 11
# Final: [5, 9, 3, 11]
'''
from typing import List
def sort_by_distance(nums: List[int], pivot: int)->List[int]:
    """
    Sorts the list nums in-place by distance from pivot, then by value if distances tie.
    """
    nums.sort(key=lambda num: (abs(num-pivot), num))
    # We have:
        # 1. Priority Sorting based on distance and in ascending order (+ in front)
        # 2. Secondary Sorting will come in play when from 1st priority sorting something is same and cannot be sorted, here 'distance can be same'.
        # - abs : gives the absolute distance (we sort by it)
        # - num : we sort by num itself, and since no negative , defaultly we sort in ascending.
    return nums

def main():
    nums = [10, 4, 7, 1, 13]
    pivot = 8

    # nums = [5, 9, 11, 3]
    # pivot = 7
    print(sort_by_distance(nums, pivot))

if __name__=="__main__":
    main()
