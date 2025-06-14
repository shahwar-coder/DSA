'''
3. Age Group Assigner
Task:
Write a function assign_group(age: int) -> str that returns:

"Infant" if age ≤ 2

"Child" if age ≤ 12

"Teen" if age ≤ 19

"Adult" if age ≤ 59

Else → "Senior"

Requirements:

Use if, elif, and else properly

You must not write multiple ifs; use a proper if-elif-else chain to avoid redundant checks.
'''

def assign_group(age: int) -> str:
    """Return age group based on age."""
    if age <= 2:
        return "Infant"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teen"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"

def main():
    age = int(input("Enter age: "))
    group = assign_group(age)
    print("Age Group:", group)

if __name__ == "__main__":
    main()


