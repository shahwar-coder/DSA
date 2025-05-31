'''
4. 🔁 All Indexes of a Word Using index()
Task:
Write a function that returns all indices where a given word appears in a list.
Use only the index() method in a loop — no list comprehension or enumerate allowed.

# Example
words = ['hi', 'hello', 'hi', 'hey', 'hi']
target = 'hi'
# Output: [0, 2, 4]

# Example
target = 'bye'
# Output: []
'''
# This can be done via easy list comprehension combined with enumerate (already. solved something like this earlier)
# But here if at all we have to do using index, then this brainy thing we do.
from typing import List, TypeVar
T=TypeVar("T")
def indices_of_all_occurrences(words: List[T], target: T)->List[int]:
    """
    Return all the indices of the occurrences of the target, if not found, return []
    """
    index=0
    indices=[]
    while True:
        try:
            index=words.index(target,index)
            indices.append(index)
            index+=1
        except ValueError:
            break
    return indices

def main():
    words = ['hi', 'hello', 'hi', 'hey', 'hi']
    target = 'hi'
    print(indices_of_all_occurrences(words, target))

if __name__=="__main__":
    main()
