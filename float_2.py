'''
2. Count Above Threshold
Task:
Given a list of floats and a threshold t, count how many elements are strictly greater than t.

Goal:
Practice comparisons with floats and simple counting.

Function Signature:
def count_above(values: List[float], t: float) -> int:
    ...
Examples:

values	                 t	  Output	    Explanation
[0.5, 1.0, 1.5, 2.0]	1.0	    2   	Only 1.5 & 2.0 > 1.0
[-1.1, -0.5, 0.0, 0.5]	-0.5	2	    -0.5 not > -0.5; 0.0,0.5
[3.1415, 2.718, 1.618]	2.0	    2	    3.1415 & 2.718
'''
from typing import List
def count_above(numbers: List[float], t: float)->int:
    # === Below is out and our Brute-Force ===
    # count=0
    # for i in numbers:
    #     if i>t:
    #         count+=1

    # === Something more efficient would be : ===
    return sum(num>t for num in numbers)

def main():
    numbers=[3.1415, 2.718, 1.618]
    t=2
    print(count_above(numbers, t))

if __name__=="__main__":
    main()
