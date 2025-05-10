'''
if input is even print 2,4,6,...
if input is odd print 1,3,5,...
'''

def printEvenOdd(user_input):
    if user_input%2==0:
        start=2
    else:
        start=1
    for i in range(start,11,2):
            print(i)

try:
    user_input = int(input("Enter integer : "))
    printEvenOdd(user_input)

except ValueError:
    print("Invalid integer input!")