'''
=>>Group Anagrams
Task:
Given a list of lowercase strings words, group them into lists of anagrams. Return a list of these groups, where each group is a list of words that are anagrams of one another. Build each group by using append(). The order of groups and the order within each group does not matter.

Goal:
Practice using append() on lists stored in a dictionary to build nested lists.

# Example 1
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# One possible output:
# [
#   ["eat", "tea", "ate"],
#   ["tan", "nat"],
#   ["bat"]
# ]

# Example 2
words = ["a", "b", "c", "a"]
# One possible output:
# [
#   ["a", "a"],
#   ["b"],
#   ["c"]
# ]

# Example 3
words = []
# You should produce: []

'''

from typing import List
from collections import defaultdict # `defaultdict` : auto-creates a list for new keys.

def group_anagrams(words: List[str])->List[List[str]]:
    """
    Group words in list of anagrams.
    """
    # dict -> key (tuple characters) , value (list of words), this dict is empty at the beginning.
    grouped_words=defaultdict(list)
    for word in words:
        key=tuple(sorted(word))
        grouped_words[key].append(word) # Append the original word to the list corresponding to its anagram signature
    return list(grouped_words.values()) # drops the key and only return values/lists

def main():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(words))

if __name__=="__main__":
    main()
