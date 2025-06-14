'''
1. One-Liner Category
Task:
Write a one-liner if-else statement to assign a value to a variable result.

Rules:

If num is divisible by 5, set result to "Buzz", else set it to "Not Buzz".
'''

num=20
result="Buzz" if num%5==0 else "Not Buzz"
print(result)


# This is wrong:
# result="Buzz" if num%5==0 else result="Not Buzz" # don't write variable name again.
