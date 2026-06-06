"""  The Core Idea
You build your sorted list one item at a time from left to right. 
For each new item, you pick it up and slide it backward into its correct position among the items you've already sorted.
"""

# | Step | Sorted Hand    | Next Card | What happens                                                           |
# | ---- | -------------- | --------- | ---------------------------------------------------------------------- |
# | 1    | `[4]`          | `2`       | 2 is smaller than 4, so shift 4 right and insert 2 at front → `[2, 4]` |
# | 2    | `[2, 4]`       | `5`       | 5 is bigger than 4, so it stays at the end → `[2, 4, 5]`               |
# | 3    | `[2, 4, 5]`    | `1`       | 1 is smaller than everything, shift all right → `[1, 2, 4, 5]`         |
# | 4    | `[1, 2, 4, 5]` | `3`       | 3 is smaller than 4 and 5, but bigger than 2 → `[1, 2, 3, 4, 5]`       |


































