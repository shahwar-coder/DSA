'''
🔁 Question: Count Until Ten

Write a function `count_until_ten()` that:

- Starts with a number `n = 1`
- Uses a `while` loop to print numbers from 1 to 10 (inclusive)
- On each loop, print the number and increase it by 1

📌 Expected Output:
1  
2  
3  
...  
10

✅ Use a `while` loop and increment the counter inside the loop.
'''

def count_till_ten():
    n=1
    while n<11:
        print(n)
        n+=1

def main():
    count_till_ten()

if __name__=="__main__":
    main()
