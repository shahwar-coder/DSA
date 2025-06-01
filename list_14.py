'''
2. Most Frequent Item (Tie-Breaker by First Appearance)
Task:
Given a list of strings words, find and return the string that appears most often. If there’s a tie, return whichever of the tied words appears earliest in the original list. Use count() to compute frequencies.

Goal:
Practice scanning with count() and tie-breaking logic.

# Example 1
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
# Frequencies: apple=3, banana=2, cherry=1 → return "apple"

# Example 2
words = ["dog", "cat", "bird", "cat", "dog"]
# Frequencies: dog=2, cat=2, bird=1
# Tie between "dog" and "cat", but "dog" appears earlier (index 0 vs. index 1) → return "dog"

# Example 3
words = []
# No words → return "" (empty string) or handle as desired.
'''

from typing import List
from collections import Counter
def most_frequent(words: List[str])->str:
    """
    Return the element which occurs the most in the list.
    In case of a tie, return the one that appears first.
    """
    if not words:
        return ""
    frequencies=Counter(words)
    max_freq=max(frequencies.values())
    # return [key for key, val in frequencies.items() if val == max_freq] # Avoid comprehension style returning as it will indulge a list not a single value return
    # Could have traverse 'frequencies' with key and val, matched val and returned key
    # BUT to be avoided, "as issue of ORDER preservance" , dicts might not preserve order.
    for word in words:
        if frequencies[word]==max_freq:
            return word

def main():
    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    print(most_frequent(words))

    # words=[]
    # print(most_frequent(words))

if __name__=="__main__":
    main()
