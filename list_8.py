'''
2. Remove All Occurrences
Task:
Given a list of strings words and a target string t, remove every occurrence of t from words using repeated calls to remove(). Return the cleaned list.

Goal:
Practice looping with remove() to delete multiple matches, and avoid skipping elements.

# Example 1
words = ["apple", "banana", "apple", "cherry", "apple"]
t = "apple"
# After removal: ["banana", "cherry"]

# Example 2
words = ["x", "y", "z"]
t = "x"
# After removal: ["y", "z"]

# Example 3
words = ["a", "a", "a"]
t = "a"
# After removal: []
'''
from typing import List, TypeVar
T=TypeVar('T')
def remove_all_occurrences(elements: List[T], t: T)->List[T]:
    """
    Remove all occurrences of a specific element
    """
    unique_collection=[elem for elem in elements if elem!=t]
    return unique_collection

def main():
    elements = ["apple", "banana", "apple", "cherry", "apple"]
    t = "apple"
    print(remove_all_occurrences(elements, t))

if __name__=="__main__":
    main()
