# 🧠 PROBLEM STATEMENT:
# Given three integers `left`, `right`, and `k`, count how many numbers 
# between `left` and `right` (inclusive) are divisible by `k`.
#
# ✅ Input:
# - Integers: left, right (range boundaries), and k (divisor)
#
# ✅ Output:
# - Print the count of numbers divisible by k in the range [left, right]
#
# 🧪 Examples:
# >>> count_numbers_divisible_by_k(1, 10, 2)
# 5
# (Numbers divisible by 2 are: 2, 4, 6, 8, 10)
#
# >>> count_numbers_divisible_by_k(5, 15, 3)
# 4
# (Numbers divisible by 3 are: 6, 9, 12, 15)

def count_numbers_divisible_by_k(left, right, k):
    """
    Return count of numbers div by k in the given range
    """
    count = right//k - (left-1)//k
    return count

def main():
    left = 10
    right = 25
    k = 5
    print(count_numbers_divisible_by_k(left,
                                       right,
                                       k))
    
if __name__=="__main__":
    main()


'''
# Alternative is very powerful that you should have a strong imagination for it:
# count = (right // k) - ((left - 1) // k)

====================

✅ Understanding: Count of Numbers Divisible by `k` in a Range [left, right]

🔍 Core Idea:
- right // k → gives the number of integers divisible by k from 1 to right.
- (left - 1) // k → gives the number of integers divisible by k before the range, i.e., from 1 to left - 1.
- The difference gives the count of numbers divisible by k in the range [left, right].

Formula:
    count = right // k - (left - 1) // k

📦 Why This Works:
- Rather than looping through each number to check if it’s divisible by k, we directly compute how many such numbers exist using integer division.
- Much faster and efficient for large ranges (O(1) time complexity).

🧠 Example:

    left = 10
    right = 25
    k = 5

    Step 1: Numbers divisible by 5 from 1 to 25 → 5, 10, 15, 20, 25 → 25 // 5 = 5
    Step 2: Numbers divisible by 5 from 1 to 9   → only 5            → 9 // 5 = 1
    Step 3: Final count = 5 - 1 = 4

✅ So the divisible numbers in [10, 25] are: 10, 15, 20, 25

This is a commonly used optimization pattern in range-based counting problems.
'''
