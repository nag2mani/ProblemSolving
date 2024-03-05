"""
Author : Nagmani Kumar
Date : 5th March, 2024

Algorithm-1 : Earliest Finish time first (Left to right sweep).
Input: A set of activities with start times and finish times.
Output: Maximum sized set of non-conflicting activities that may be scheduled.

Algorithm-2: Latest Start time First (right to left sweep).
Input: A set of activities with start times and finish times.
Output: Maximum sized set of non-conflicting activities that may be scheduled.
"""


def Earliest_finish_time_first(lst):
    # Sorted list on the basis of Earliest Finish time earlier (Left to right sweep).
    k = sorted(lst, key=lambda x: x[1])

    candidate_list = []
    prev_finish_time = 0
    for i in k:
        if i[0] >= prev_finish_time:
            candidate_list.append(i)
            prev_finish_time = i[1]
    return candidate_list



def Latest_start_time_first(lst):
    # Sorted list on the basis of Latest Start time First or decreasing start time (right to left sweep).
    kp = sorted(lst, key=lambda x: x[0], reverse = True)

    candidate_list = []
    latest_start_time = float("inf")
    for i in kp:
        if i[1] <= latest_start_time:
            candidate_list.append(i)
            latest_start_time = i[0]
    return sorted(candidate_list, key=lambda x: x[0])



def main():
    lst1 = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
    lst2 = [(1,4), (4, 5), (0,6), (5,7), (8, 9)]
    print(Earliest_finish_time_first(lst2))
    print(Latest_start_time_first(lst2))


main()