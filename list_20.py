'''
4. Sort People by Multiple Attributes Using Chained Stability
Task:
You have a list of dictionaries people, each with keys "name" (string), "age" (int), and "salary" (int). Sort in-place so that:

Primary order is by increasing salary.

Secondary order (tie-break) is by decreasing age.

Tertiary order (tie-break if both salary and age match) is by alphabetical name (A→Z).

You must achieve this with two or three calls to list.sort(), leveraging Python’s stable sort—i.e., sort by the least‐significant key first, then by the next, etc., so that earlier stability preserves correct order.

Goal:
Learn how to order by multiple criteria using stable, in-place sorts, rather than building a single complex key tuple.

# Example 1
people = [
    {"name": "Alice", "age": 30, "salary": 50000},
    {"name": "Bob",   "age": 25, "salary": 40000},
    {"name": "Carl",  "age": 30, "salary": 40000},
    {"name": "Dana",  "age": 25, "salary": 50000},
    {"name": "Eve",   "age": 30, "salary": 50000}
]
# We want:
#  1) salary ascending: 40000 group → [Bob, Carl], then 50000 → [Alice, Dana, Eve]
#  2) within 40000, age descending: Carl (30) before Bob (25)
#     within 50000, age descending: Alice (30), Eve (30), then Dana (25)
#  3) within same salary & age, name ascending: for Alice/Eve both age 30→ sort by name → "Alice" before "Eve"
# Final sorted order:
# [
#   {"name": "Carl",  "age": 30, "salary": 40000},
#   {"name": "Bob",   "age": 25, "salary": 40000},
#   {"name": "Alice", "age": 30, "salary": 50000},
#   {"name": "Eve",   "age": 30, "salary": 50000},
#   {"name": "Dana",  "age": 25, "salary": 50000}
# ]

# Example 2
people = [
    {"name": "X", "age": 40, "salary": 30000},
    {"name": "Y", "age": 40, "salary": 30000},
    {"name": "Z", "age": 50, "salary": 30000}
]
# 1) salary all same → no change
# 2) age descending: Z (50), then X (40), Y (40)
# 3) within age 40, tie-break by name: "X" before "Y"
# Final:
# [
#   {"name": "Z", "age": 50, "salary": 30000},
#   {"name": "X", "age": 40, "salary": 30000},
#   {"name": "Y", "age": 40, "salary": 30000}
# ]

# Example 3
people = []
# After sorting: []
'''
from typing import List, Dict
def ultimate_sort(people: List[Dict])->List[Dict]:
    """
    Return the sorted list, after primary, secondary and tertiary sorts.
    """
    people.sort(key=lambda person: (person['salary'], -person['age'], person['name']))
    return people

    # PRIMARY: sort by increasing salary (+)
    # SECONDARY: (tie-break): sort by decreasing age (-).   
    # TERTIARY: (tie-break): sort by name (alphabetical order so '+')
    # Note : Sequentially Primary, Secondary, Tertiary....
    # Note: + : Ascending order, - : descending order.

def main():
    people = [
        {"name": "Alice", "age": 30, "salary": 50000},
        {"name": "Bob",   "age": 25, "salary": 40000},
        {"name": "Carl",  "age": 30, "salary": 40000},
        {"name": "Dana",  "age": 25, "salary": 50000},
        {"name": "Eve",   "age": 30, "salary": 50000}
    ]
    print(ultimate_sort(people))

if __name__=="__main__":
    main()

