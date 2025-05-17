'''
1. Price Banding
Task:
Given a list of integer prices and three fixed bands:

0–500 → "Low"

501–1000 → "Medium"

1001+ → "High"

Return a list of strings where each price is labeled with its band.

Goal:
Practice simple if-elif bucketization.

Function Signature:
```python
def price_band(prices: List[int]) -> List[str]:
    ...
```

Example:
| Input                       | Output                                       |
| --------------------------- | -------------------------------------------- |
| `[199, 999, 499, 1499]`     | `["Low", "Medium", "Low", "High"]`           |
| `[0, 500, 501, 1000, 1001]` | `["Low", "Low", "Medium", "Medium", "High"]` |
'''
from typing import List
def price_category(prices: List[int])->List[str]:
    if not prices:
        raise ValueError("Prices cannot be empty!")
    prices_equivalent=[]
    for p in prices:
        if p < 0:
            raise ValueError("Price cannot be negative!")
        if 0 <= p <= 500:
            prices_equivalent.append("Low")
        elif 501 <= p <= 1000:
            prices_equivalent.append("Medium")
        else:
            prices_equivalent.append("High")
    return prices_equivalent


def main():
    prices=[199, 999, 499, 1499]
    print(price_category(prices))

if __name__=="__main__":
    main()
