'''
(Don't use simple palindrome check, we need to learn corresponding check while we traverse)
You're given a list of integers nums. Check if each element at the front half of the list is equal to its mirrored element from the end.

Return True if all such mirror pairs are equal, otherwise False.

You only need to compare the first half with the mirrored second half — do not reverse or modify the list.

Examples:
mirror_pairs([1, 2, 2, 1]) → True
mirror_pairs([1, 2, 3, 2, 1]) → True
mirror_pairs([5, 6, 7, 8, 9]) → False
mirror_pairs([]) → True  # empty list is trivially valid
mirror_pairs([1]) → True

'''
from typing import List
def mirror_pairs(nums: List[int])->bool:
    return all(nums[i]==nums[~i] for i in range(len(nums)//2))
    # Loop till half only
    # Then compare ith and ~ith elements (corresponding) 

def main():
    nums=[1, 2, 3, 2, 1]
    print(mirror_pairs(nums))

if __name__=="__main__":
    main()


"""
🔍 Mirror Pair Check — Explanation & FAQs

👉 Key Line:
    return all(nums[i] == nums[~i] for i in range(len(nums) // 2))

---

📌 What does this line do?
- Iterates only through the first half of the list.
- `~i` is bitwise NOT in Python, which equals `-i - 1`.
  - So `~0 = -1` (last item), `~1 = -2` (second last), etc.
- Compares each element from the front with its mirrored element from the end.
- `all(...)` ensures all such pairs are equal.

---

❓ Q1: Why not use `nums[::-1]` to check for palindrome?
✅ A: `nums[::-1]` creates a full reversed copy of the list — O(n) space.
    This solution is more efficient — it doesn't reverse or copy the list.

---

❓ Q2: What does `~i` do, and why is it used here?
✅ A: In Python, `~i == -i - 1`:
    - `~0 = -1` → last element
    - `~1 = -2` → second last
    It allows symmetric comparison without computing length or using extra math.

---

❓ Q3: When should I prefer this approach?
✅ A: Use it when:
    - You only need to compare mirror pairs.
    - You want a space-efficient solution.
    - You're working with large datasets.

---

❓ Q4: Is this approach data type agnostic?
✅ A: Yes. It works with:
    - Integers: [1, 2, 3, 2, 1]
    - Strings: ['a', 'b', 'b', 'a']
    - Booleans, None, etc.
    As long as elements are comparable using `==`.

---

❓ Q5: Why is this approach scalable?
✅ A:
    - Only checks n/2 elements → O(n/2)
    - Uses a generator → no extra memory
    - Doesn't modify the original list

---
"""
