'''
3. Build a Stack with Middle Insertion
Task:
Simulate a “double‐ended” stack where you:

push_front(x) uses insert(0, x)

push_back(x) uses append(x)

Given a sequence of operations, return the final list.

Goal:
Practice using insert() at index 0 to add to the front of a list.

# Example 1
ops = [("push_back", 1), ("push_front", 2), ("push_back", 3), ("push_front", 4)]
# Simulate:
#   [] → append(1) → [1]
#   insert(0,2) → [2,1]
#   append(3) → [2,1,3]
#   insert(0,4) → [4,2,1,3]
# Final: [4, 2, 1, 3]

# Example 2
ops = [("push_front", 5)]
# Final: [5]
'''
from typing import List, Tuple
def push_back(final: List[int], inserting_num: int)->None:
    final.append(inserting_num)
    # return final # not needed as final is already mutated in place, just return None (meaning nothing)

def push_front(final: List[int], inserting_num: int)->None:
    final.insert(0,inserting_num)
    # return final

def list_formation(ops: List[Tuple[str, int]])->List[int]:
    """Simulate a double-ended stack given a list of push operations."""
    final=[]
    for op in ops:
        op_str, inserting_num = op
        if op_str=="push_back":
            push_back(final, inserting_num)
        elif op_str=="push_front":
            push_front(final, inserting_num)
        else:
            raise ValueError(f"Unknown Operation: {op_str}")
    return final

def main():
    try:
        ops = [("push_back", 1), ("push_front", 2), ("push_back", 3), ("push_front", 4)]
        print(list_formation(ops))
    except ValueError as e:
        print(f"Error : {e}")

if __name__=="__main__":
    main()
