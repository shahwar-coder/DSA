'''
Given a positive integer n, return the sum of its decimal digits without converting the integer to a string.

Goal: Practice repeated division and modulus on int.

Constraints:

1 ≤ n < 10^18

Time complexity should be O(log₁₀ n).

Input:  n = 123456789
Output: 45
# Explanation: 1+2+3+4+5+6+7+8+9 = 45
'''

def sum_digits(number: int) -> int:
    """
    Return the sum of decimal digits in `number`.
    Raises ValueError if `number` is negative.
    """
    if number < 0:
        raise ValueError("Number must be non-negative!")

    total = 0
    # Special case: if number is 0, sum of digits is 0
    if number == 0:
        return 0

    # Repeatedly extract last digit and add it
    while number != 0:
        total += number % 10
        number //= 10

    return total

def main():
    try:
        n = int(input().strip())  # reading as int; string conversion prohibited
        print(sum_digits(n))
    except ValueError as e:
        print("Invalid Input! :", e)

if __name__ == "__main__":
    main()
