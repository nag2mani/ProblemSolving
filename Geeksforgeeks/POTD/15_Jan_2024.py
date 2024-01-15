from typing import List


class Solution:
    def max_courses(self, n : int, total : int, cost : List[int]) -> int:
        dynamic_array = [0 for _ in range(total + 1)]

        for c in reversed(cost):
            for t in range(total, c-1, -1):
                dynamic_array[t] = max(dynamic_array[t], dynamic_array[t - (c + 9)//10] + 1)

        return dynamic_array[total]
        