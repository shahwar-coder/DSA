'''
4. Balanced Brackets
Task:
Given a string containing only '(' and ')', determine if the parentheses are balanced using a list as a stack (append() + pop()).

Goal:
Apply pop() in a real DSA context—stack-based parentheses matching.

# Example 1
s = "()()"
# Output: True

# Example 2
s = "(()())"
# Output: True

# Example 3
s = "(()"
# Output: False

# Example 4
s = ")("
# Output: False
'''
def is_authentic_braces(s: str)->bool:
# ===
# ===

def main():
    # s="()()"
    # Output: True
    # s = "(()())"
    # Output: True
    # s = "(()"
    # Output: False
    s = ")("
    # Output: False
    print(is_authentic_braces(s))

if __name__=="__main__":
    main()
