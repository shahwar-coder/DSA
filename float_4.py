'''
4. Approximate Equality
Task:
Implement a function that, given two floating-point numbers a and b and a tolerance ε, returns True if their absolute difference is at most ε, otherwise False.

Goal:
Understand floating-point comparison and practice using the absolute difference check.

Function Signature:

python
Copy
Edit
def approx_equal(a: float, b: float, eps: float) -> bool:
    ...
Examples:
| `a`         | `b`       | `ε`      | Output  | Explanation |                           |                     |
| ----------- | --------- | -------- | ------- | ----------- | ------------------------- | ------------------- |
| `0.1 + 0.2` | `0.3`     | `1e-9`   | `True`  | \`          | 0.30000000000000004 - 0.3 | ≈ 4e-17 ≤ 1e-9\`    |
| `1.000`     | `1.001`   | `0.0005` | `False` | \`          | 1.000 - 1.001             | = 0.001 > 0.0005\`  |
| `-2.0`      | `-2.0001` | `0.0002` | `True`  | \`          | −2.0 - (−2.0001)          | = 0.0001 ≤ 0.0002\` |

'''

def approx_equal(a: float, b: float, epsilon: float)->bool:
    if epsilon<0:
        raise ValueError("Epsilon must be non negative.")
    difference= abs(a-b)
    return difference<=epsilon

def main():
    try:
        a=1.000
        b=1.001 
        epsilon=0.0005
        print(approx_equal(a, b, epsilon))
    except ValueError as e:
        print(f"Invalid Inputs : {e}")

if __name__=="__main__":
    main()
