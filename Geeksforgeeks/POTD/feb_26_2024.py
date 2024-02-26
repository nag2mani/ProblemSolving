from itertools import combinations, permutations

class Solution:
	def AllPossibleStrings(self, s):
		a=[]
		for i in range(1,len(s)+1):
			for j in list(combinations(s,i)):
				a.append("".join(j))
		# a.sort()
		return a


sol = Solution()
s = 'abc'
print(sol.AllPossibleStrings(s))


print(list(permutations('ABCD',2)))
print(list(combinations('ABCD',2)))
