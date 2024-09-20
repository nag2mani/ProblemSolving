from collections import Counter
from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        result = []
        for i in freq:
            if freq[i]==2:
                result.append(i)
        return result

