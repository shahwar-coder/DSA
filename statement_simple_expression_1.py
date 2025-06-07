'''
Title: In-Place Doubling with Side Effects

You are given a list of integers. Your task is to double only the even numbers in the list in-place, such that the list is updated with new values.

However, you are not allowed to use return statements or list comprehensions.

You must use a helper function that performs the update as a side effect, and this helper must be invoked in a way that does not store any return value.
Input: [1, 2, 3, 4, 5]  
Output: [1, 4, 3, 8, 5]
'''
from typing import List

def double_even_numbers(nums: List[int]) -> None:
    """
    Doubles even numbers in the list in-place (no return).
    """
    for i, n in enumerate(nums):
        if n % 2 == 0:
            nums[i] = n * 2  # Update even element at index i

def main():
    nums = [1, 2, 3, 3, 4, 5, 6]
    double_even_numbers(nums)  # Modify list in-place
    print(nums)  # Output: [1, 4, 3, 3, 8, 5, 12]

if __name__ == "__main__":
    main()


"""
📌 Title: In-Place Doubling with Side Effects

🧠 Objective:
- Perform in-place update of even numbers (double their values).
- Must **not use** return statements or list comprehensions.
- Must use **side effects** (mutating the original list).

✅ Key Features:
- Uses `enumerate()` to loop with index.
- Mutates the list directly using `nums[i] = ...`
- No list creation, no returning new lists.

💡 Why it's important:
- Demonstrates how to safely mutate a list during iteration.
- Reinforces idea of **side effects** — modifying data passed by reference.
- Encourages clear separation between transformation logic and output/printing.

🔍 Output for [1, 2, 3, 3, 4, 5, 6]:
    => [1, 4, 3, 3, 8, 5, 12]

🎯 Skills practiced:
- In-place updates
- Function behavior without `return`
- Readable and maintainable code structure
"""

