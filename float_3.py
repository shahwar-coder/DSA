'''
3. Find Maximum with Precision
Task:
From a list of floats, return the maximum value rounded to p decimal places.

Goal:
Combine use of max() and round(), and understand floating-point precision.

Function Signature:
def max_with_precision(values: List[float], p: int) -> float:
    ...
Examples:

values	                    p	Output	    Explanation
[1.9999, 2.0001, 2.0000]	3	2.000	    max is 2.0001 → round to 3 places → 2.000
[0.1234, 0.5678, 0.5555]	2	0.57	    max=0.5678 → round→0.57
[-0.1, -0.01, -0.001]	    4	-0.0010	    max= -0.001
'''
from typing import List
def max_with_precision(numbers: List[float], p: int)->float:
    if not isinstance(p, int) or p < 0:
        raise ValueError("Precision p should be a non negative integer.")
    if len(numbers)==0:
        raise ValueError("List cannot be empty.") # imp to raise for empty list as max may not work with empty lists.
    return round(max(numbers), p)

def main():
    try:
        numbers=[1.9999, 2.0001, 2.0000]
        p=3 #precision
        print(max_with_precision(numbers, p))
    except ValueError as e:
        print(f"Invalid Inputs : {e}")

if __name__=="__main__":
    main()
