'''
2. Count Digits
Problem:
Given a positive integer n, return the number of digits in its decimal representation without converting it to a string.

Goal: Practice repeated division / logarithms on int.

Constraints:

1 ≤ n < 10^18

Aim for O(log₁₀ n) time.

Examples:
Input:  n = 7
Output: 1

Input:  n = 1000
Output: 4
'''

def count_digits(number: int)->int:
    """
    Return int : count of digits in the number, 
    Note: Converting to string is restricted.
    """
    count=0

    if number < 0:
        raise ValueError("Number must be positive!")

    if 0 <= number <= 10:
        return 1

    while number!=0:
        count += 1
        number//=10
    return count

def main():
    try:
        number=int(input().strip()) # counting from string is prohibited.
        print(count_digits(number))
    except ValueError as e:
        print("Invalid Inputs! : ", e)

if __name__=="__main__":
    main()
