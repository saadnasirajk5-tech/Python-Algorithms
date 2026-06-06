""" Selection Sort  The Lazy Perfectionist
Imagine you have a messy stack of exam papers. Instead of going through them in order, you scan the entire stack
to find the easiest one, place it at the top, then scan the remaining papers for the next easiest, and so on. That's Selection 
Sort in a nutshell. 
The Core Idea (in 3 steps)
1.
Find the smallest element in the unsorted part of the list.
2.
Swap it with the first element of that unsorted part (so it goes into its final position).
3.
Repeat for the rest of the list.
It's "lazy" because it doesn't worry about shifting things around — it just selects the minimum and places it.
And it's a "perfectionist" because after each pass, the position i is permanently sorted — no more touching it!
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i 
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j 
        arr[i],arr[min_idx]  = arr[min_idx], arr[i] 
    return arr 

print(selection_sort([64, 34, 25, 12, 22, 11, 90])) 


"""Let's trace it on [64, 25, 12, 22, 11]:

Pass (i)	Array state	min_idx	After swap
i=0	[64, 25, 12, 22, 11]	4	[11, 25, 12, 22, 64] 
i=1	[11, 25, 12, 22, 64]	2	[11, 12, 25, 22, 64] 
i=2	[11, 12, 25, 22, 64]	3	[11, 12, 22, 25, 64] 
i=3	[11, 12, 22, 25, 64]	3	[11, 12, 22, 25, 64] 
i=4	[11, 12, 22, 25, 64]	4	[11, 12, 22, 25, 64] """


##########################################################################################################################################
##########################################################################################################################################















