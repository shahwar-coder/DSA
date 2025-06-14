'''
2. Search with Loop + else
Task:
Write a function check_keyword(sentence: str) -> str that searches for the word "python" in a list of words from the sentence.

If found, return "Found!", else return "Not found."
Use a for-else block.
'''

def check_keyword(sentence: str)->str:
    """Return if python is found in the sentence"""
    words=sentence.split()
    for word in words:
        if word=="python":
            return "Found!"
    else:
        return "Not found."

def main():
    sentence="I love python programming!"
    # sentence="I love trips!"
    print(check_keyword(sentence))

if __name__=="__main__":
    main()
