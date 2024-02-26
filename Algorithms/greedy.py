def findMinArrowShots(points):
    #Sorted list on the basis of 2nd element.
    k = sorted(points,key= lambda x:x[1])

    count = 0
    maxx = float("-inf")
    for i in k:
        if i[0]>maxx:
            maxx = i[1]
            count += 1
    return count

points = [[10,16],[2,8],[1,6],[7,12]]
print(findMinArrowShots(points))