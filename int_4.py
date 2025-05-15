'''
Given a 32-bit signed integer n (which may be negative), return the integer formed by reversing its decimal digits, while preserving its sign.

Goal: Practice modular arithmetic, handling negative numbers, and edge-case thinking.


You may assume that reversing n will not overflow this range in any test case.

Examples:
Input:  n = 123
Output: 321
# Explanation: digits reversed from 1-2-3 to 3-2-1

Input:  n = -450
Output: -54
# Explanation: digits reversed from 4-5-0 to 0-5-4, drop leading zero → 54, preserve sign → -54

Input:  n = 1000
Output: 1
# Explanation: digits reversed from 1-0-0-0 to 0-0-0-1 → drop leading zeros → 1
'''

def reverse_number(number: int)->int:
    if number<0:
        is_negative=True
        number=abs(number)
    else:
        is_negative=False

    rev_number=0
    loop_run=0
    while number:
        rev_number=rev_number*10 + (number%10)
        print("rev number now : ", rev_number) # this print is for debugging.
        number//=10
    return -rev_number if is_negative else rev_number 

def main():
    try:
        number=int(input())
        print(reverse_number(number))
    except ValueError as e:
        print(f"Invalid Inputs! {e}")

if __name__=="__main__":
    main()
