'''
//////////-----HELPFUL POWER TOOL FOR GETTING MIRRORED INDEX-----/////////
### 🧠 Explanation: Using `~i` for Mirrored Index Comparison

The bitwise NOT operator `~` in Python is used as a concise way to get the mirrored index from the end of a list.

- `~i` is equivalent to `-i - 1`
- This gives the **reverse index** without needing to reverse the list
- It's especially helpful for checking symmetry (e.g., palindromes)

For example:

```python
nums = [1, 2, 3, 2, 1]
for i in range(len(nums) // 2):
    if nums[i] != nums[~i]:  # ~i = -i - 1
        return False
return True
'''
