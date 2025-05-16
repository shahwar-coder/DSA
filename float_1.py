'''
1. floats_sum and Round Floats
Task:
Given a list of floats, compute their floats_sum and round the result to k decimal places.

Goal:
Practice basic iteration, floating-point arithmetic, and Python’s round() behavior.

Function Signature:
def floats_sum_and_round(values: List[float], k: int) -> float:
    ...

Examples:

| values                   | k | Output | Explanation                                 |
|--------------------------|:-:|--------|---------------------------------------------|
| `[1.234, 2.345, 3.456]`   | 2 | `7.04` | `1.234 + 2.345 + 3.456 = 7.035` → round → 7.04 |
| `[0.1, 0.2, 0.3]`         | 1 | `0.6`  | `0.1 + 0.2 + 0.3 = 0.6000000000000001` → 0.6 |
| `[-1.5, 2.25, -0.75]`     | 3 | `0.000`| `-1.5 + 2.25 + (-0.75) = 0.0` → formatted as 0.000 |
'''
from typing import List
from math import fsum
def sum_and_round(float_numbers: List[float], k: int)->float:
    if k<0:
        raise ValueError("k must be greater than 0")
    floats_sum=fsum(float_numbers)
    return round(floats_sum, k)

def main():
    try:
        float_numbers=[1.234, 2.345, 3.456]
        k=2
        # k=-4
        print(sum_and_round(float_numbers, k))
    except ValueError as e:
        print("Invalid Inputs : ", e)

if __name__=="__main__":
    main()
