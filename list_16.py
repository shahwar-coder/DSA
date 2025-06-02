'''
4. Anagram Checker with Count
Task:
Write a function that takes two strings s1 and s2 (both containing only lowercase letters) and returns True if they are anagrams of each other, otherwise False. You must use list.count() on the list of characters to verify that each unique character in s1 appears exactly the same number of times in s2 (and that lengths match). Do not sort or use collections.Counter.

Goal:
Practice verifying equal multisets by comparing individual count() results.

# Example 1
s1 = "listen"
s2 = "silent"
# Both have the same letters and frequencies → True

# Example 2
s1 = "triangle"
s2 = "integral"
# True

# Example 3
s1 = "apple"
s2 = "pale"
# Different lengths or letter counts → False

# Example 4
s1 = ""
s2 = ""
# Empty strings → True (two empty “multisets” are trivially anagrams)
'''
from collections import Counter
def anagram(s1: str, s2: str)->bool:
    """
    Return True if anagrams else False
    """
    freq1=Counter(s1)
    freq2=Counter(s2)
    return freq1==freq2

def main():
    s1 = "listen"
    s2 = "silent"

    # s1 = ""
    # s2 = ""
    print(anagram(s1, s2))

if __name__=="__main__":
    main()


    # ===============================


# If to be done usning count()
'''
def anagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    for char in set(s1):  # only check each unique char once
        if s1.count(char) != s2.count(char):
            return False
    return True
'''
