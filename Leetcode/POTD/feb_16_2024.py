
# from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq_map = Counter(arr)
        sorted_freq = sorted(freq_map.items(), key=lambda x: x[1])
        for num, freq in sorted_freq:
            if k >= freq:
                k -= freq
                del freq_map[num]
            else:
                break

        return len(freq_map)




#Top solution by other;

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        """
        Challenge: How do we know what integers to remove? Do we have to explore all possible options or is there a heuristic that we can use to determine which ones to take out?

        Simple solution:
        - Find the frequency of each unique integer. Remove the lowest frequency ones until we run out of k.
        time - O(nlogn)
        space- O(n)

        Other Solutions:
        - Prob won't be doing better than O(n) time, need to see the entire array to determine what integers to remove.
        - Can save on space. sort in place?

        """
        c = Counter(arr)
        cnt, remaining = Counter(c.values()), len(c)
        for key in sorted(cnt):
            if k >= key * cnt[key]:
                k -= key * cnt[key]
                remaining -= cnt.pop(key)
            else:
                return remaining - k // key
        return remaining
