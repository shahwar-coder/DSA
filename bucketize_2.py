'''
2. Custom Range Buckets
Task:
You’re given a sorted list of bucket edges (integers) and a list of values. Each bucket is half-open:
[edges[0], edges[1]), [edges[1], edges[2]), …, [edges[-1], ∞)
Return a list of bucket‐index integers for each value.

Goal:
Practice mapping values into buckets via linear scan.

Function Signature:
def value_to_bucket(values: List[int], edges: List[int]) -> List[int]:
    ...
Examples:
| `values`          | `edges`        | Output      | Explanation                                   |
| ----------------- | -------------- | ----------- | --------------------------------------------- |
| `[10, 50, 75]`    | `[0, 40, 60]`  | `[0, 1, 1]` | 10 in \[0,40)→0; 50,75 in \[40,60)→1          |
| `[100, 200, 300]` | `[50,150,250]` | `[1, 1, 2]` | 100→\[50,150) bucket 1; 300→\[250,∞) bucket 2 |


# ==================== Elaborate the problem =========================


🪣 What does bucket mean here?
Imagine you have boxes (buckets), and each box can hold a range of numbers.
Your job is to put each number into the correct box.

🧱 Buckets are made from a list of numbers called edges:
Each edge marks the start of a bucket.

The buckets look like this (mathematically):
[edges[0], edges[1]), [edges[1], edges[2]), ..., [edges[-1], ∞)

Let's say:
edges = [0, 40, 60]

Then the buckets are:

Bucket 0: [0, 40) → includes numbers 0 to 39
Bucket 1: [40, 60) → includes numbers 40 to 59
Bucket 2: [60, ∞) → includes 60 and anything bigger

Example:
values = [10, 50, 75]
edges  = [0, 40, 60]

What bucket does each number go in?

10 goes in [0, 40) → Bucket 0

50 goes in [40, 60) → Bucket 1

75 goes in [60, ∞) → Bucket 2

So, answer = [0, 1, 2]

✅ But the problem says:
[10, 50, 75] with [0, 40, 60] → [0, 1, 2]

'''
from typing import List
def bucket_indices(values: List[int], edges: List[int])->List[int]:
    final_bucket_indices=[]
    if not values:
        raise ValueError("Values cannot be empty!")
    for val in values:
        val_placed=False
        for edge_index in range(len(edges)-1):
            if edges[edge_index] <= val < edges[edge_index+1]: #<= , < (here no <=, because should not be included)
                final_bucket_indices.append(edge_index)
                val_placed=True
                break
        if not val_placed and val < edges[0]:
            final_bucket_indices.append(-1)
        if not val_placed and val > edges[-1]:
            final_bucket_indices.append(len(edges)-1)
    return final_bucket_indices

def main():
    try:
        values = [10, 50, 75]
        edges  = [0, 40, 60]
        print(bucket_indices(values, edges))
    except ValueError as e:
        print("Invalid Inputs : ", e)

if __name__=="__main__":
    main()


# Below Solution is using concept of Bisect, to be re-visited.

'''
import bisect
from typing import List

def bucket_indices_bisect(values: List[int], edges: List[int]) -> List[int]:
    """
    edges must be sorted. Returns bucket index k for each v in values,
    where bucket k covers [edges[k], edges[k+1]) (and k = len(edges)-1 covers [edges[-1], ∞)).
    """
    if not edges:
        raise ValueError("Edges cannot be empty")

    result = []
    for v in values:
        # bisect_right returns insertion point in range [0..len(edges)]
        idx = bisect.bisect_right(edges, v)
        # bucket is idx-1, but clamp to [0..len(edges)-1]
        k = max(0, min(idx - 1, len(edges) - 1))
        result.append(k)
    return result

# --- Examples ---
edges = [0, 40, 60]
values = [10, 50, 75, -5]
print(bucket_indices_bisect(values, edges))
# Explanation:
# 10 → bisect_right([0,40,60],10)=1 → bucket=0
# 50 → bisect_right(...,50)=2 → bucket=1
# 75 → bisect_right(...,75)=3 → bucket=2
# -5 → bisect_right(...,-5)=0 → idx-1=-1 → clamp to 0 → bucket=0
# ⇒ [0, 1, 2, 0]

'''
