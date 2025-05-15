'''
4. Two-Sum with Integers
Problem:
Given a list of distinct integers nums and a target T, return any pair of indices (i, j) such that nums[i] + nums[j] == T, or (-1, -1) if none exists.

Goal: Practice hashing with integer keys.

Constraints:

2 ≤ len(nums) ≤ 10^5

-10^9 ≤ nums[i], T ≤ 10^9

Expected O(n) time, O(n) extra space.

Examples:
Input: nums = [2, 7, 11, 15], T = 9
Output: (0, 1)
# Because nums[0] + nums[1] = 2 + 7 = 9

Input: nums = [1, 2, 3], T = 7
Output: (-1, -1)
'''
# Correct and efficient as there is a use of dict/hash-map replacing multiple for loops. 
from typing import List
def two_sum(nums: List[int], T: int)->tuple:
    seen=dict()
    for i,num in enumerate(nums):
        complement = T - num
        if complement in seen:
            return (seen[complement], i) # seen compliment index will naturally come before the i th index, that's why the order.
        seen[num]=i
    return (-1, -1)

def main():
    try:
        nums = [2, 7, 11, 15]
        T = 9
        print(two_sum(nums, T))
    except ValueError as e:
        print(f"Invalid Inputs! {e}")

if __name__=="__main__":
    main()


# Correct but not very efficient.
# from typing import List
# def two_sum(nums: List[int], T: int)->tuple:
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if i!=j:
#                 if nums[i]+nums[j]==T:
#                     return (i,j)
#     return (-1,-1)

# def main():
#     try:
#         nums = [2, 7, 11, 15]
#         T = 9
#         print(two_sum(nums, T))
#     except ValueError as e:
#         print(f"Invalid Inputs! {e}")

# if __name__=="__main__":
#     main()
