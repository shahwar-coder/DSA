'''
1. Maintain Sorted Order
Task:
Given a sorted list of integers sorted_nums and a new integer x, insert x into sorted_nums at the correct position so that the list remains sorted. Use insert().

Goal:
Practice finding the right index and using insert() to maintain sorted order.

# Example 1
sorted_nums = [1, 3, 5, 7]
x = 4
# After insertion: [1, 3, 4, 5, 7]

# Example 2
sorted_nums = [10, 20, 30]
x = 5
# After insertion: [5, 10, 20, 30]

# Example 3
sorted_nums = [2, 4, 6]
x = 8
# After insertion: [2, 4, 6, 8]
'''

from typing import List
def keep_sorted(sorted_numbers: List[int], x: int)->List[int]:
    """
    Insert x into sorted_numbers so the list remains sorted (in‐place).

    We initialize index = len(sorted_numbers) to default to “append to the end”,
    then scan from the front and break early when we find the first element > x.
    """
    index=len(sorted_numbers)
    for i, number in enumerate(sorted_numbers):
        if x<number:
            index=i
            break
            # core is : if 'x' is always greater than numbers in list we never visit "index=i, break"
            # so when eg, x=8 is compared in [2,4,6] => i remain at 2 at max, bcz i moves 0->1->2 that's it, but index=len(list) = 3 here, so it helps place at last. 
    sorted_numbers.insert(index, x) # at that index we should put and rest will automatically shift towards right.
    return sorted_numbers

def main():
    # sorted_numbers = [1, 3, 5, 7]
    # x=4

    sorted_numbers=[2,4,6]
    x=8

    print(keep_sorted(sorted_numbers, x))

if __name__=="__main__":
    main()
