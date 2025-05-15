'''
Given a list of integers, return the first number that repeats.
If no number repeats, return -1.
'''
from typing import List
def first_repeating(numbers: List[int])->int:
    seen=set()
    for num in numbers:
        if num in seen:
            return num
        seen.add(num)
    return -1

def main():
    try:
        numbers=[1,2,3,2,1]
        print(first_repeating(numbers)) # first one repeating is 2 here.
    except ValueError:
        print("Invalid Input!")

if __name__=="__main__":
    main()
