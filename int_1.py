'''
1. Sum of Digits
Problem:
Given a non-negative integer n, compute the sum of its decimal digits.

Goal: Practice converting an integer to its digits and simple aggregation.

Constraints:

0 ≤ n < 10^18

Time complexity: O(d) where d = number of digits.

Examples:

Input:  n = 12345
Output: 15
# Explanation: 1 + 2 + 3 + 4 + 5 = 15

Input:  n = 0
Output: 0
'''

def sum_of_digits(number: str)->int:
    sanitised_number=number.strip()
    if not sanitised_number.isdigit(): # is digit will check if all the digits are integers
        raise ValueError("Input must be non negative integer.")
    return sum(map(int, sanitised_number)) # number here is a string (can be viewed as list of some sort, hence works!)
                                 # sum() : can take map generator, no need to wrap under list.

def main():
    try:
        number=input() #input will be str and we will keep it str here.
        print(sum_of_digits(number))
    except ValueError as e:
        print(f"Invalid Input! {e}")

if __name__=="__main__":
    main()
