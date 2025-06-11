'''
2. Truthy Filter
Task:
Write a function filter_truthy(items: List[Any]) -> List[Any] that takes a list of arbitrary values and returns a new list containing only those items that are truthy (i.e., when used in an if condition evaluate to True).

You must use a for loop and an if statement—no list comprehensions allowed.

# Example 1
print(filter_truthy([0, 1, "", "hello", [], [0], None, True]))  
# Output: [1, "hello", [0], True]

# Example 2
print(filter_truthy([False, None, 0.0, {}, set()]))  
# Output: []
'''

# Comprehensions not allowed, we will do it with if

from typing import Any, List
def filter_truthy(values: List[Any])->None:
    """Return a the list with only truthy values"""
    truth: List[Any]=[]
    for val in values:
        if val:
            truth.append(val)
    return truth

def main():
    values = [0, 1, "", "hello", [], [0], None, True]
    print(filter_truthy(values))

if __name__=="__main__":
    main()

'''
- Never Never Never , remove dynamically anything from the list or any iterable we are iterating forward, eg, in a loop.
- Never remove elements from a list you’re iterating forwards—it almost always leads to bugs.
- If you walk forwards and del or pop elements, the remaining items shift left and you’ll skip elements or go out of bounds.
- If at all it is mandatory to not create new list then use backward traversal.
- Why Backwards?
    - If you walk forwards and del or pop elements, the remaining items shift left and you’ll skip elements or go out of bounds.
    - If you walk backwards, each removal only affects “earlier” indices you’ve already processed.

- BUT , to be honest, simple forward and append instead of backward and del/pop is far better.
    '''


# from typing import Any, List
# def filter_truthy(values: List[Any])->None:
#     """Return a the list with only truthy values"""
#     for i,val in enumerate(values):
#         if not val:
#             values.pop(i)
#             i-=1
#     # interestingly we do not return anything WHY? -> As we mutated original list we can print it in main section directly.

# def main():
#     values = [0, 1, "", "hello", [], [0], None, True]
#     filter_truthy(values) # I made it not to return anything (just logic execution and changes to original list)
#     print(values)

# if __name__=="__main__":
#     main()
