'''
2. Reverse Each Sub‐segment of Length k
Task:
Given a list of integers nums and a positive integer k such that k evenly divides len(nums), break nums into consecutive sub‐segments of length k and reverse each sub‐segment in place. Return the final list.

# Example 1
nums = [1, 2, 3, 4, 5, 6]
k = 2
#  Sub‐segments: [1,2], [3,4], [5,6]
#  Reverse each: [2,1], [4,3], [6,5]
#  Result: [2, 1, 4, 3, 6, 5]

# Example 2
nums = [10, 20, 30, 40, 50, 60, 70, 80]
k = 4
#  Sub‐segments: [10,20,30,40], [50,60,70,80]
#  Reverse each: [40,30,20,10], [80,70,60,50]
#  Result: [40, 30, 20, 10, 80, 70, 60, 50]

# Example 3
nums = [5, 10]
k = 1
#  Sub‐segments of length 1 remain [5], [10] → no actual change
#  Result: [5, 10]
'''


from typing import List
def reverse_sub_segments(nums: List[int], k: int)->List[int]:
    """
    Divide the list into segments of size k and reverse each segment.
    Assumes k divides len(nums) exactly.
    """
    assert k>0 and len(nums)%k == 0, "k must be positive and divide len(nums)"
    result=[]
    for i in range(0,len(nums),k):
        result.extend(reversed(nums[i:i+k]))
    return result

def main():
    nums = [1, 2, 3, 4, 5, 6]
    k = 2

    # nums = [10, 20, 30, 40, 50, 60, 70, 80]
    # k = 4

    # nums = [5, 10]
    # k = 1
    
    print(reverse_sub_segments(nums, k))

if __name__=="__main__":
    main()

# ====== Works but above is more functional and safe as reversed() is used over reverse()
# from typing import List
# def reverse_sub_segments(nums: List[int], k: int)->List[int]:
#     """
#     Divide the list into segments of size k and reverse each segment.
#     Assumes k divides len(nums) exactly.
#     """
#     assert k>0 and len(nums)%2 == 0, "k must be positive and divide len(nums)"
#     sub_segments=[]
#     result=[]
#     for i in range(0,len(nums),k):
#         sub_segments.append(nums[i:i+k])
#     for sub_segment in sub_segments:
#         sub_segment.reverse()
#         result.extend(sub_segment)
#     return result

# def main():
#     nums = [1, 2, 3, 4, 5, 6]
#     k = 2

#     # nums = [10, 20, 30, 40, 50, 60, 70, 80]
#     # k = 4

#     # nums = [5, 10]
#     # k = 1
    
#     print(reverse_sub_segments(nums, k))

# if __name__=="__main__":
#     main()

