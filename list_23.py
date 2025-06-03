'''
3. Check Palindrome List
Task:
Write a function that determines whether a list of values nums reads the same forwards and backwards (i.e., is a palindrome). Return True if it is, False otherwise. The input list may contain any data type (integers, strings, etc.).

# Example 1
nums = [1, 2, 3, 2, 1]
#  Forward: [1,2,3,2,1], Reverse: [1,2,3,2,1] → palindrome → True

# Example 2
nums = ['a', 'b', 'b', 'a']
#  Forward and reverse match → True

# Example 3
nums = [1, 2, 3, 4]
#  Forward: [1,2,3,4], Reverse: [4,3,2,1] → not a palindrome → False

# Example 4
nums = []
#  Empty list → True (trivially a palindrome)
'''

from typing import List, TypeVar
T=TypeVar("T")
def is_palindrome(nums: List[T])->bool:
    """Return Palindrome or No"""
    rev_nums=nums[::-1]
    return nums==rev_nums

def main():
    nums = [1, 2, 3, 2, 1]
    # nums = ['a', 'b', 'b', 'a']
    print(is_palindrome(nums))

if __name__=="__main__":
    main()
