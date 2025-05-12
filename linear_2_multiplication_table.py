def table_formation(user_input):
    '''
    To write table for the number.
    '''
    for i in range(1,11):
        print(f"{user_input} x {i} = {user_input*i}")

try:
    user_input = int(input("Enter number for table : "))
    table_formation(user_input)
except ValueError:
    print("Invalid input!")
