'''
5. Count Set Bits in Range
Problem:
Given a non-negative integer n, return a list counts of length n+1 where counts[i] is the number of 1 bits in the binary representation of i.

Goal: Practice bitwise operations and dynamic programming.

Constraints:

0 ≤ n ≤ 10^5

Overall time O(n), extra space O(n).

Examples:
Input:  n = 5
Output: [0, 1, 1, 2, 1, 2]
# Binary: 0→0, 1→1, 2→10, 3→11, 4→100, 5→101
'''
from typing import List
def count_bits(number: int)->List[int]:
    output_list=[]
    for i in range(number+1):
        output_list.append(i.bit_count())
        # output_list.append(bin(i).count('1')) # if you decide to convert to bin, 
    return output_list

def main():
    try:
        number=5
        print(count_bits(number))
    except ValueError:
        print("Invalid Input!")

if __name__=="__main__":
    main()
