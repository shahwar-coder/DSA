'''
2. Day Type
Task:
Write a function day_type(day: str) -> str that returns:

"Weekend" if day is "Saturday" or "Sunday"

"Weekday" if it's "Monday" to "Friday"

"Invalid day" for anything else

Case-sensitive match is fine for now.
'''

# ====== This solution is faster as set is used ==========
weekdays={"monday", "tuesday", "wednesday", "thursday", "friday"}
weekends={"saturday", "sunday"}
def day_type(day: str)->str:
    "Return day type"
    if day in weekends:
        return "Weekend"
    elif day in weekdays:
        return "Weekday"
    else:
        return "Invalid day"

def main():
    day="wednesday"
    print(day_type(day))
    # day="saturday"
    # day="zombieday"

if __name__=="__main__":
    main()

# ====== Below is same solution but O(n) as lists getting used ===============

# days=["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
# def day_type(day: str)->str:
#     "Return day type"
#     if day not in days:
#         return "Invalid day"
#     elif day in days[5:]:
#         return "Weekend"
#     else:
#         return "Weekday"

# def main():
#     day="wednesday"
#     print(day_type(day))
#     # day="saturday"
#     # day="zombieday"

# if __name__=="__main__":
#     main()
