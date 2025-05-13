'''
✅ 5. Minimum Flips to Make All True
Problem:
You are given a list of booleans. In one operation, you can flip a boolean and all values after it. Return the minimum number of operations to make all values True.

Input:
[False, False, True, False]
Output:
3
'''

def count_flips(bools: list)->int:
    flips=0
    for i in range(len(bools)):
        if not bools[i]: # if False found
            print("Checking in : ", bools[i:])
            for j in range(i,len(bools)):
                bools[j]=not bools[j]
            print("Updated bools : ", bools)
            flips+=1
            if all(bools):
                return flips
    return flips

def main():
    try:
        bools=[True, False, True, False]
        print(count_flips(bools))
    except Exception:
        print("Something went wrong!")

if __name__=="__main__":
    main()
