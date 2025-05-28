'''
1. 📍 Find the Second 'red'
Task:
You are given a list of colors. Find the second occurrence of the color "red" and return its index.
If "red" appears only once or not at all, return "Not found".

# Example
colors = ['blue', 'red', 'green', 'red', 'yellow']
# Output: 3

# Example
colors = ['red', 'blue', 'green']
# Output: "Not found"
'''

from typing import List, Union
def second_index(colors: List[str])->Union[int, str]:
    """
    Return the index of the second occurrence of "red" in `colors`.
    If fewer than two occurrences, return "Not found".
    """
    try:
        first_red=colors.index("red")
        second_red=colors.index("red", first_red+1)
    except:
        return "Not Found"
    return second_red

def main():
    # colors = ['blue', 'red', 'green', 'red', 'yellow']
    # print(second_index(colors))

    # colors = ['red', 'blue', 'green']
    # print(second_index(colors))

    colors = ['blue', 'green', 'violet']
    print(second_index(colors))

if __name__=="__main__":
    main()

