'''
Case 1: Best Optimal Use
'''
for x in arr:
    best = max(best, x)


'''
Case 1: Bad use
'''
for i in range(n):
    best = max(arr[:i])   # BAD

# | Pattern                               | Complexity                                  |
# | ------------------------------------- | ------------------------------------------- |
# | `max(a, b)` inside loop               | **O(n)** ✔                                  |
# | `max(arr[i])` (single element)        | **O(n)** ✔                                  |
# | `max(arr[:i])` or max over big slices | **O(n²)** ❌                                 |
# | `sum(arr)` inside loop                | **O(n²)** ❌ (because sum scans whole array) |

