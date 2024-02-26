def findMinArrowShots(points):
    #Sorted list on the basis of 2nd element.
    #(Finish time earlier).
    k = sorted(points,key= lambda x:x[1])

    count = 0
    maxx = float("-inf")
    for i in k:
        if i[0]>maxx:
            maxx = i[1]
            count += 1
    return count

    ##m-2
    # def findMinArrowShots(self, points):
    #     # Sorted list on the basis of 2nd element. (Finish time earlier).
    #     k = sorted(points, key=lambda x: x[1])
    #     count = 0
    #     end = float("-inf")
    #     for start, finish in k:
    #         if start > end:
    #             end = finish
    #             count += 1
    #     return count


points = [[10,16],[2,13],[1,6],[7,12]]
print(findMinArrowShots(points))

# Both are same thing;
print(sorted(points,key= lambda x:x[0]))
print(sorted(points))


# --------------------------------------------------------------------


def findMinArrowShots(points):
    def findMinArrowShots(self, points):
        # Sorted list on the basis of 1st element. (latest start time).
        k = sorted(points, key=lambda x: x[0])
        count = 0
        end = float("-inf")  # Initialize end time to negative infinity
        
        for start, arrow in k:
            if start > end:
                count += 1
                end = arrow  # Update end time to the end of the current balloon
            else:
                end = min(end, arrow)  # Update end time to the minimum of current and previous end times
        
        return count


points = [[10,16],[2,13],[1,6],[7,12]]
print(findMinArrowShots(points))