"""  The Core Idea
You build your sorted list one item at a time from left to right. 
For each new item, you pick it up and slide it backward into its correct position among the items you've already sorted.
"""
"""  
key = arr[i] $\rightarrow$ Pick up a number and hold it in your hand.while j >= 0 and key < arr[j]: 
$\rightarrow$ Look to the left. Is that number bigger than the one in your hand?arr[j + 1] = arr[j] $\rightarrow$ 
Yes? Slide that bigger number one slot to the right.j -= 1 $\rightarrow$ Move your eyes to the next 
box on the left.arr[j + 1] = key $\rightarrow$ When you can't go left anymore, drop the number from 
your hand into the empty slot.
"""


# | Step | Sorted Hand    | Next Card | What happens                                                           |
# | ---- | -------------- | --------- | ---------------------------------------------------------------------- |
# | 1    | `[4]`          | `2`       | 2 is smaller than 4, so shift 4 right and insert 2 at front → `[2, 4]` |
# | 2    | `[2, 4]`       | `5`       | 5 is bigger than 4, so it stays at the end → `[2, 4, 5]`               |
# | 3    | `[2, 4, 5]`    | `1`       | 1 is smaller than everything, shift all right → `[1, 2, 4, 5]`         |
# | 4    | `[1, 2, 4, 5]` | `3`       | 3 is smaller than 4 and 5, but bigger than 2 → `[1, 2, 3, 4, 5]`       |

# | Check          | Meaning                                                         |
# | -------------- | --------------------------------------------------------------- |
# | `j >= 0`       | "Have I fallen off the left edge of the array?"                 |
# | `key < arr[j]` | "Is the card I'm holding smaller than the card I'm looking at?" |

# pick up, compare left, slide bigger stuff right, drop.

def insertion_sort(arr):
    n= len(arr)  
    for i in range(1,len(arr)):
        key = arr[i]    
        j = i - 1      
        while j >= 0 and key < arr[j]:              
            arr[j + 1] = arr[j]  
            j -= 1 
        arr[j + 1] = key   
    return arr  
             

###################################################################################################################################
###################################################################################################################################

"""   Let's pass in the list [5, 2, 4]. Here is the exact play-by-play of the computer executing the script:
 Round 1: When i = 1
Line 2 (for i in range(1, len(arr)):)
Computer sets i = 1.

Line 3 (key = arr[i])
Computer looks at arr[1], which is 2. It saves key = 2.

Line 4 (j = i - 1)
Computer calculates 1 - 1. It sets j = 0.

Line 5 (while j >= 0 and key < arr[j]:)
Computer checks: Is 0 >= 0? Yes. Is 2 < arr[0] (which is 5)? Yes. Because both are true, it enters the while loop.

Line 6 (arr[j + 1] = arr[j])
Computer takes the value at arr[0] (5) and copies it into arr[1].
The list now looks like: [5, 5, 4]

Line 7 (j -= 1)
Computer changes j from 0 to -1.

Line 5 (Loop Check Again)
Computer checks: Is -1 >= 0? No! The loop instantly breaks.

Line 8 (arr[j + 1] = key)
Computer calculates j + 1 (-1 + 1 = 0). It places key (2) into arr[0].

The list now looks like: [2, 5, 4]
 Round 2: When i = 2
Line 2
Computer bumps i up to 2.

Line 3
Computer looks at arr[2], which is 4. It saves key = 4.

Line 4
Computer calculates 2 - 1. It sets j = 1.

Line 5 (while...)
Computer checks: Is 1 >= 0? Yes. Is 4 < arr[1] (which is 5)? Yes. It enters the loop.

Line 6
Computer takes the value at arr[1] (5) and copies it into arr[2].
The list now looks like: [2, 5, 5]

Line 7
Computer changes j from 1 to 0.

Line 5 (Loop Check Again)
Computer checks: Is 0 >= 0? Yes. Is 4 < arr[0] (which is 2)? No! (4 is not smaller than 2). The loop breaks.

Line 8 (arr[j + 1] = key)
Computer calculates j + 1 (0 + 1 = 1). It places key (4) into arr[1].
The list now looks like: [2, 4, 5]

The Finish Line
Line 2 * The loop realizes it reached the end of the list (len(arr) is 3, so it stops).
Line 9 (return arr)
The computer hands back the final, perfectly sorted list: [2, 4, 5].
"""




























