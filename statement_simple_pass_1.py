'''
🔷 Building a Skeleton Menu System
You’re designing a command-line application with the following structure:

The menu has options: "1. Add", "2. Delete", "3. View", and "4. Exit".

Each option should be represented as a stub function (add(), delete(), view()) with pass inside them for now.

In the main loop, based on user input, the corresponding function should be called — but since they all have pass, nothing will happen inside yet.

👉 Write this stub-based program that:

Accepts the user input.

Calls the correct function using if-elif-else.

Prints "Exiting..." and breaks the loop if the user enters "4".

🧠 This tests your understanding of:

Using pass in real structural design.

Proper control flow with placeholder logic.
'''

# Skeleton Menu System

def add():
    pass

def delete():
    pass

def view():
    pass

def options():
    print("Menu:\n")
    print("1. Add")
    print("2. Delete")
    print("3. View")
    print("4. Exit")

def menu():
    while True:
        try:
            options()
            option=int(input("Enter option : "))
        except ValueError:
            print("Please enter a valid integer") #helps catch error when other than integer is entered, eg. character, symbols
            continue

        if option==1:
            add()
        elif option==2:
            delete()
        elif option==3:
            view()
        elif option==4:
            print("Exiting...")
            break
        else:
            print("Enter between 1-4 : ")
            continue


def main():
    menu()

if __name__=="__main__":
    main()


# ✅ This structure is a great scaffold for expanding the application later!
