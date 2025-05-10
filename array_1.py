# https://www.geeksforgeeks.org/problems/wave-array-1587115621/0
arr = [1,2,3,4,5]
def convertToWave(arr):
    for index in range(0, len(arr), 2):
        if index<len(arr)-1:
            if arr[index] < arr[index+1]:
                temp = arr[index]
                arr[index] = arr[index+1]
                arr[index+1] = temp
            print(arr)
convertToWave(arr)


# =============================================

from typing import List
class Solution:
    def convertToWave(self, arr : List[int]) -> None:
        for index in range(0, len(arr), 2):
            if index<len(arr)-1:
                if arr[index] < arr[index+1]:
                    temp = arr[index]
                    arr[index] = arr[index+1]
                    arr[index+1] = temp
        return arr

