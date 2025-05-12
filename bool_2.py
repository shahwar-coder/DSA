'''
🟢 2. Count Truthy Elements
Problem:
Given a list of values (of any data types), count how many of them are truthy, i.e., bool(value) evaluates to True.

Examples:
Input: [0, "", "hello", [], [1], {}, None, 1, True]  
Output: 4
'''

from typing import List
import ast  

def take_out_literals(tokens: List)->List:
    for token in tokens:
        ast_token=ast.literal_eval(token)
        ast_mixed_list.append(ast_token)
    return ast_mixed_list


def count_truthy_values(mixed_list: List)->int:
    count=0
    for i in mixed_list:
        if i:
            count+=1
    return count

try:
    tokens=input()
    mixed_list=tokens.split(" ")
    # func call
except Exception:
    print("Invalid Inputs!")
