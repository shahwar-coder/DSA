'''
append() : good/efficient if used inside a loop
'''

result = []
for x in arr:
    result.append(x * 2)


'''
"+" : really bad inside a loop if we are doing something like:
'''
result = []
for x in arr:
    result = result + [x]    # O(n) each time! → O(n²)

