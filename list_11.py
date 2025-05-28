'''
2. 🧠 Search Within a Sublist
Task:
Given a list of numbers, find the index of the number 9, but only consider elements between index 3 and 7 (inclusive of index 3, exclusive of 7).
If 9 is not found in that range, return "Missing".

# Example
nums = [1, 2, 9, 3, 9, 4, 5, 6]
# Output: 4  (since index 4 has 9, and it's between 3 and 7)

# Example
nums = [1, 2, 3, 4, 5, 6]
# Output: "Missing"
'''

from typing import List, Union
def sub_search(nums: List[int])->Union[int, str]:
    """
    Return a number's index if it is between 3 and 7 , else return "Missing"
    """
    try:
        return nums.index(9,3,7)
    except ValueError:
        return "Missing"

def main():
    nums = [1, 2, 9, 3, 9, 4, 5, 6]
    print(sub_search(nums)) # 4

if __name__=="__main__":
    main()
