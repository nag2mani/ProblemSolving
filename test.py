def infpoint(a):
    for i in range(1, len(a)):
        if a[i] < a[i-1]:
            return a[i-1]
    return a[i]

def infpoint2(a):
    start = 0
    end = len(a)
    while (start < end - 1):
        mid = start + (end - start)//2
        if a[mid] > a[mid+1]:
            return mid
        else:
            


a1 = [2,4,50,6,3,1]
a2 = [2,5,67,80,900, 2]
a3 = [2,5,60,90]
a4 = [400, 39, 2,1]

print(infpoint(a1))
print(infpoint(a2))
print(infpoint(a3))
print(infpoint(a4))

print(infpoint2(a1))
print(infpoint2(a2))
print(infpoint2(a3))
print(infpoint2(a4))
