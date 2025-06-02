'''
1. Sort Words by Their Last Character
Task:
You have a list of non-empty strings words. Sort this list in-place so that the words appear in ascending order of their last character. If two words share the same last character, they should maintain their current relative order (i.e. use Python’s stable sort).

Goal:
Practice writing a custom key function that extracts the last character, and understand how stability preserves original ordering for ties.

# Example 1
words = ["apple", "banana", "cherry", "date", "fig"]
# Last characters:  e,      a,       y,     e,   g
# Sorted by last char → ['banana', 'apple', 'date', 'fig', 'cherry']
# Explanation:
#  - 'banana' ends with 'a'
#  - 'apple' ends with 'e' and comes before 'date' (also ends with 'e') because 'apple' appeared first originally.
#  - 'date' ends with 'e'
#  - 'fig' ends with 'g'
#  - 'cherry' ends with 'y'

# Example 2
words = ["alpha", "delta", "beta", "gamma"]
# Last chars:  a,      a,      a,     a
# All end with 'a' → stable sort keeps original order:
# ['alpha', 'delta', 'beta', 'gamma']
'''
from typing import List
def sort_by_last_character(words: List[str])->List[str]:
    """Sort the list of words in-place based on the last character and return it."""
    words.sort(key=lambda word: word[-1]) # Extract last character of each word via lambda and sort using it as a key.
    return words

def main():
    words = ["apple", "banana", "cherry", "date", "fig"]
    print(sort_by_last_character(words))

if __name__=="__main__":
    main()
