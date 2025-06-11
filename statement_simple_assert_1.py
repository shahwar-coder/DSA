'''
🔷 Assertion for Input Constraints
You are writing a function that calculates the square root of a number, but it must only accept non-negative inputs.

def safe_sqrt(n):
    # TODO: add assertion here
    return n ** 0.5

print(safe_sqrt(9))    # valid
print(safe_sqrt(-1))   # should not be allowed


Tasks:

Add a meaningful assert inside the function to enforce input constraint.
What will happen if the user passes -1?
Why is using assert a better option during development than letting the math operation silently crash?

'''

def safe_sqrt(n):
    assert n>=0, "The number is not non negative!"
    return n ** 0.5

print(safe_sqrt(9))    # valid # 3.0
print(safe_sqrt(-1))   # AssertionError will rise

# ✅ Explanation:
# - If a negative number is passed, the assertion fails and an AssertionError is raised with the custom message.
# - This prevents the function from silently performing an invalid or undefined operation.
# - Assertions are useful during development to catch logical bugs early and clearly.
# - Example: `safe_sqrt(-1)` immediately stops execution with a clear message, instead of allowing a cryptic runtime crash later.
