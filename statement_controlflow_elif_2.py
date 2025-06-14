'''
3. Movie Ticket Pricing
Task:
Write a function ticket_price(age: int) -> str that returns the ticket price category:

age < 0 → raise ValueError

age <= 3 → "Free"

age <= 12 → "Child: ₹100"

age <= 59 → "Adult: ₹200"

age >= 60 → "Senior: ₹150"

Rules:

Use if, elif, else.

Avoid unnecessary checks — try to use efficient branching like how elif is supposed to be used.
'''

def ticket_price(age: int)->str:
    "Return the ticket price based on age"
    if age<0:
        raise ValueError("Age  cannot be negative.")
    elif age<=3:
        return "Free"
    elif age<=12:
        return "Child: 100"
    elif age<=59:
        return "Adult: 200"
    elif age>=60:
        return "Senior: 150"

def main():
    age=4
    print(ticket_price(age))

if __name__=="__main__":
    main()
