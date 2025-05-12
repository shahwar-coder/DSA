'''
✅ 3. Find First Row with All Truthy Values in Boolean Matrix
Problem:
Given a 2D matrix (list of lists) of boolean values, return the index of the first row where all values are True. Return -1 if none.

Input:
[[True, False], [True, True], [False, True]]
Output:
1
'''

def find_index_all_true(matrix):
    for index,row in enumerate(matrix):
        if all(row):
            return index
    return -1 # not None , since we intend to return int for correct cases so for negative cases : -1

def main():
    try:
        # imagine input is given.
        matrix=[[True, False], 
                [False, False],
                [True, True],
                [False, True]]
            # if inputs are taken from the user follow following steps:
            # 1. Take rows
            # 2. Split and convert to list 
            # 3. write and call a function which can convert content of list having "True"/"False" as True/False
            # 4. call `find_index_all_true`
        print(find_index_all_true(matrix))
    except Exception:
        print("Invalid Inputs!")

if __name__=="__main__":
    main()
