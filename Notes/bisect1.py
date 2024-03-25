import bisect

a = [1,2,3,6,8,9,45,89]

print(bisect.bisect(a,8))
# print(bisect.bisect_left(a,8))



# binary search

def binar_search(a,x):
    i = bisect.bisect_left(a,x)
    if (i != len(a)) and (a[i]== x):
        return i
    else:
        return -1

print(binar_search(a,8))





