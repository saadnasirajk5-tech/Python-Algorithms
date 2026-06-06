"""   Without this variable, the computer would keep checking the list over and over again, even if the list was already sorted.
By using swapped = False, you give the computer a way to say:
"I'm done early because everything is already in order." It saves time and energy!
The - 1 is just the computer's way of saying: "Stop before you reach the very last plate, because you're already looking at its neighbor."
Summary Table
Pass Number (i)	How many at the end are "done"?	Where do we stop?
Pass 0	0	Stop at index 4 (5 - 0 - 1)
Pass 1	1	Stop at index 3 (5 - 1 - 1)
Pass 2	2	Stop at index 2 (5 - 2 - 1)
"""

def Bubble_Sort(arr): #arr means array, it takes array as input 
    n = len(arr) #Stores total number of items in variable called n  
    for i in range(n):
        swapped = False 
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j] 
                swapped = True 
                if not swapped:
                    break 
    return arr  
print(Bubble_Sort([64, 34, 25, 12, 22, 11, 90]))  
                

###################################################################################################################
###################################################################################################################










