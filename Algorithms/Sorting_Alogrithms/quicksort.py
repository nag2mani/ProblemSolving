def quick_sort(b, h, k):
    """
    This is a sorting algorithm which is using divide and conquer rule to sort a list.
    b : list to be sorted.
    h : first index of list from where you want to sort.
    k : last index of list up to which you want to sort.
    """
    if (k-h) < 1 :
        #It will return None and exit the program, if the length of the list is 1
        return
    else:
        j = partition(b, h, k)
        quick_sort(b, h, j-1)
        quick_sort(b, j+1, k)

#helper function for swaping the element.
def swap(b,x,y):
    """It replace y from x and vice versa in b"""
    b[x], b[y] = b[y], b[x]

#helper function to partition the list.
def partition(b, i, j):
    """Partition list b[h...k] around a pivot x = b[h]
    where smalller element will be on the left hand side and bigger
    will be on right hand side of the pivot.
    b : list to be partition.
    i : first index of list from where you want to partition.
    j : last index of list up to which you want to partition.
    """
    while i < j:
        if b[i+1] >= b[i]:
            # Move to end of block.
            swap(b,i+1,j)
            j = j - 1
        else:
            swap(b,i,i+1)
            i = i + 1
    return i


b=[10,5, 8,4,12,4,7,0,15, 9,0, -33, 82, 6,3, -1]
quick_sort(b,0, len(b)-1)
print(b)





