'''
Using sum() inside a loop, is really a bad idea
'''

for i in range(n):
    total = sum(arr)   # O(n)
# n * O(n) = O(n²)

'''
🚀 How to avoid this?
Use prefix sum or sliding window, both give O(n) instead of O(n²).
'''
# Example:
window_sum = sum(arr[:k])
for i in range(k, n):
    window_sum += arr[i] - arr[i-k]
