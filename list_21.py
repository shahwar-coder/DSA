'''
1. Mirror Around the Center
Task:
You receive a list of integers nums of even length. Transform it so that the second half of the list becomes a “mirror” of the first half in reverse order. In other words, for an even‐length list, overwrite every element in the second half with the corresponding element from the first half, but in reverse order.

If nums = [a, b, c, d], after transformation it becomes [a, b, b, a].

If nums = [1, 2, 3, 4, 5, 6], after transformation it becomes [1, 2, 3, 3, 2, 1].

# Example 1
nums = [10, 20, 30, 40]
#  First half → [10, 20], second half replaced by [20, 10]
#  Result: [10, 20, 20, 10]

# Example 2
nums = [5, 7, 9, 11, 13, 15]
#  First half → [5, 7, 9], second half replaced by [9, 7, 5]
#  Result: [5, 7, 9, 9, 7, 5]

# Example 3
nums = []
#  (Empty list remains empty)
'''

from typing import List
def mirror(nums: List[int])->List[int]:
    """
    Return a list where the second half mirrors the first half in reverse.
    Only even-length lists are valid inputs.
    """
    assert len(nums)%2 == 0, "List length must be even" # Helps in early failure
    mirror_position=len(nums)//2
    first_half=nums[:mirror_position]
    second_half=first_half[::-1] # not using reverse as it changes original list, but we want first half to concatenate later.
    return first_half+second_half

def main():
    # Below is proper way to form tests 
    assert mirror([10, 20, 30, 40]) == [10, 20, 20, 10]
    assert mirror([5, 7, 9, 11, 13, 15]) == [5, 7, 9, 9, 7, 5]
    assert mirror([]) == []
    print("✅ All test cases passed.")

if __name__=="__main__":
    main()
