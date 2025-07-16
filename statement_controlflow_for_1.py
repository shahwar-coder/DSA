'''
🔁 Question: Find Uppercase Words

Write a function `find_uppercase(words)` that:

- Takes a list of strings `words` as input
- Iterates through the list
- Returns a new list containing only the words that are in **ALL uppercase**

📌 Example:
print(find_uppercase(['Hello', 'WORLD', 'PYTHON', 'is', 'Great']))  
# Output: ['WORLD', 'PYTHON']

✅ Use a `for` loop and string method `.isupper()` to check if a word is uppercase.
'''

from typing import List
def find_uppercase(words: List[str])->List[str]:
    """Return uppercase words from the list"""
    new_list=[]
    for word in words:
        if word.isupper():
            new_list.append(word)
    return new_list

def main():
    words=['Hello', 'WORLD', 'PYTHON', 'is', 'Great']
    print(find_uppercase(words))

if __name__=="__main__":
    main()

'''
- If one liner is allowed, the solution would be :
- return [word for word in words if word.isupper()]
'''
