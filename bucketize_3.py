'''
3. Fixed-Width Buckets
Task:
Given a list of non-negative integers and a bucket width w, assign each number to bucket index k = value // w. Return the list of indices.

Goal:
Practice integer division bucketization.

Function Signature:
def fixed_width_bucket(values: List[int], w: int) -> List[int]:
    ...

Example:
| `values`           | `w`  | Output        | Explanation               |
| ------------------ | ---- | ------------- | ------------------------- |
| `[0, 1, 2, 5, 9]`  | `5`  | `[0,0,0,1,1]` | 0–4→0, 5–9→1              |
| `[10, 25, 30, 31]` | `10` | `[1,2,3,3]`   | 10–19→1, 20–29→2, 30–39→3 |
'''
from typing import List
def fixed_width_bucket(values: List[int], w: int)->List[int]:
    if not values:
        raise ValueError("Values cannot be empty")
    if w<=0:
        raise ValueError("Width should be non-zero positive number.")
    final_bucket=[]
    for val in values:
        final_bucket.append(val//w)
    return final_bucket

def main():
    try:
        values=[0,1,2,5,9]
        w=5 # width
        print(fixed_width_bucket(values, w))
    except ValueError as e:
        print("Invalid Inputs", e)

if __name__=="__main__":
    main()
