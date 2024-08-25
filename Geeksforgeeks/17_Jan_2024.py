from itertools import permutations

class Solution:
    def uniquePerms(self, arr, n):
        r = set(permutations(arr))
        return sorted(list(r))


#This need to be done in details.