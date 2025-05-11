'''
1. Check Alternating Boolean List
Problem:
Given a list of boolean values (True and False), determine if the list alternates between True and False without any consecutive duplicates.

Input:
[True, False, True, False, True]

Output:
True

Input:
[True, True, False]

Output:
False
'''

# ================ [9.5/10] ==================
from typing import List
def is_alternate(bools: List[bool]) -> bool:
    for i in range(len(bools)-1):
        if bools[i]==bools[i+1]:
            return False
    return True

def parse_bools(bools: List[str])->List[bool]:
    parsed_bools=[]
    for b in bools:
        lowered_bool=b.strip().lower()
        if lowered_bool == "true":
            parsed_bools.append(True)
        elif lowered_bool == "false":
            parsed_bools.append(False)
        else:
            raise ValueError(f"Invalid boolean value {b}")
    return parsed_bools


if __name__=="__main__":
    try:
        tokens=input("Enter bools separated by spaces: ")
        bools=tokens.split()
        parsed_bools=parse_bools(bools)
        print(is_alternate(parsed_bools))
    except Exception:
        print("Invalid Input!")




# ================ [7/10] ==================

# def is_alternate(list_of_bools):
#     for index in range(len(list_of_bools)-1):
#         print(f"Taking {list_of_bools[index]} and {list_of_bools[index+1]} = {list_of_bools[index] + list_of_bools[index+1]}")
#         if list_of_bools[index] + list_of_bools[index+1] != 1:
#             return False
#     return True

# def take_correct_bools_instead_of_strings(list_of_str_bools):
#     list_of_actual_bools=[]
#     for i in list_of_str_bools:
#         if i == "True":
#             list_of_actual_bools.append(True)
#         elif i == "False":
#             list_of_actual_bools.append(False)
#     return list_of_actual_bools

# try:
#     streak_of_bools = input()
#     list_of_str_bools = streak_of_bools.split(" ")
#     list_of_bools = take_correct_bools_instead_of_strings(list_of_str_bools)
#     print(is_alternate(list_of_bools))
# except ValueError:
#     print("Invalid Input!")
