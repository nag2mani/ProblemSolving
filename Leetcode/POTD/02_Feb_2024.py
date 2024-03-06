# 01 Febraury 2024
import numpy as np
class Solution:
    def divideArray(self, nums, k):
        nums.sort()
        res = []
        for i in range(0, len(nums), 3):
            if i + 2 < len(nums):
                if nums[i + 2] - nums[i] > k:
                    return []
                res.append([nums[i], nums[i + 1], nums[i + 2]])

        return res



# 02 February 2024
class Solution:
    def sequentialDigits(self, low, high):
        res = []
        for i in range(1, 10):
            temp = i
            for j in range(i + 1, 10):
                temp = 10 * temp + j
                if temp in range(low, high + 1):
                    res.append(temp)
        res.sort()
        return res



# 03 February 2024
class Solution:
    def maxSumAfterPartitioning(self, arr, k):
        # Length of the input array
        n = len(arr)
        
        # Memoization dictionary
        memo = {}

        # Recursive function to find the maximum sum after partitioning
        def dfs(i):
            # Base case: end of the array
            if i == n:
                return 0

            # Check if result for index i is memoized
            if i in memo:
                return memo[i]

            curMax = curSum = 0

            # Iterate over the next k elements or until the end of the array
            for j in range(i, min(i + k, n)):
                curMax = max(curMax, arr[j])
                cur = curMax * (j - i + 1) + dfs(j + 1)
                curSum = max(curSum, cur)

            # Memoize result for index i
            memo[i] = curSum
            return curSum

        return dfs(0)



# 04 February 2024
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        a, c, d, r = 0, Counter(), Counter(t), [inf, '']
        for b in range(len(s)):
            c[s[b]] += 1
            while all(c[v] >= d[v] for v in d):
                r = min(r, [b-a+1, s[a:b+1]])
                c[s[a]] -= 1
                a += 1
        
        return r[1]


# more optimised


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        char_frequency_t = defaultdict(int)
        for char in t:
            char_frequency_t[char] += 1

        left = 0
        min_len = float('inf')
        min_left = 0
        count = len(t)

        for right in range(len(s)):
            current_char = s[right]

            if current_char in char_frequency_t:
                char_frequency_t[current_char] -= 1
                if char_frequency_t[current_char] >= 0:
                    count -= 1

            while count == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left

                left_char = s[left]
                if left_char in char_frequency_t:
                    char_frequency_t[left_char] += 1
                    if char_frequency_t[left_char] > 0:
                        count += 1
                left += 1

        return "" if min_len == float('inf') else s[min_left:min_left + min_len]



# 05 February 2024
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s.rindex(s[i]) == s.index(s[i]):
                return i
        return -1


#Mind blowing.
class Solution:
    def firstUniqChar(self, s: str) -> int:
        return min([s.index(char) for char in set(s) if s.count(char) == 1] or [-1])


# 06 February 2024
class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        # Dictionary to store anagram groups
        anagram_groups = {}
        
        # Iterate through each word in the input list
        for word in words:
            # Sort the characters in the word to create a key
            key = "".join(sorted(word))
            
            # If key is not in the dictionary, add a new entry with the word as a list
            if key not in anagram_groups:
                anagram_groups[key] = [word]
            # If key is already present, append the word to the existing list
            else:
                anagram_groups[key].append(word)
        
        # Return the values (anagram groups) of the dictionary
        return anagram_groups.values()
        



# 07 February 2024
class Solution:
    def frequencySort(self, s: str) -> str:
        ans,freq = '',defaultdict(list)
        count = Counter(s)
        maxFreq = 0

        for key,val in count.items():
            freq[val]+=[key]*val
            maxFreq = max(maxFreq,val)

        while maxFreq:
            ans+=''.join(freq[maxFreq])
            maxFreq-=1

        return ans




# 08 February 2024
class Solution:
    def numSquares(self, n: int) -> int:
        dp=[0]*(n+1)
        for i in range(1,n+1):
            dp[i]=i
            for j in range(1,int(math.sqrt(i))+1):
                dp[i]=min(dp[i],dp[i-j*j]+1)
        return dp[n]



# 09 February 2024

class Solution:
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []

        nums.sort()
        n = len(nums)
        dp = [1] * n  # dp[i] stores the length of the largest divisible subset ending at index i
        prev = [-1] * n  # prev[i] stores the index of the previous element in the largest divisible subset

        max_len = 1
        max_idx = 0

        # Compute dp array
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
                    if dp[i] > max_len:
                        max_len = dp[i]
                        max_idx = i

        # Reconstruct the largest divisible subset
        result = []
        while max_idx != -1:
            result.append(nums[max_idx])
            max_idx = prev[max_idx]

        return result[::-1]



# 10 February 2024
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0

        for i in range(n):
            dp[i][i] = True
            count += 1

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    count += 1

        return count




##Best solution

class Solution:
    def countSubstrings(self, S: str) -> int:
        ans, n, i = 0, len(S), 0
        while (i < n):
            j, k = i - 1, i
            while k < n - 1 and S[k] == S[k+1]: k += 1                
            ans += (k - j) * (k - j + 1) // 2
            i, k = k + 1, k + 1
            while ~j and k < n and S[k] == S[j]:
                j, k, ans = j - 1, k + 1, ans + 1
        return ans



# 11 February 2024
class Solution:
    def cherryPickup(self, grid) -> int:
        rows, cols = len(grid), len(grid[0])

        # @lru_cache(None)
        #why after adding above line take less time than not adding
        
        def dp(row, col1, col2):
            if row == rows:
                return 0
            cherries = grid[row][col1] + (grid[row][col2] if col1 != col2 else 0)
            max_cherries = 0
            for d1 in [-1, 0, 1]:
                for d2 in [-1, 0, 1]:
                    new_col1, new_col2 = col1 + d1, col2 + d2
                    if 0 <= new_col1 < cols and 0 <= new_col2 < cols:
                        max_cherries = max(max_cherries, dp(row + 1, new_col1, new_col2))
            return cherries + max_cherries
        
        return dp(0, 0, cols - 1)



# 12 February 2024
#my solution
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]


# other solution
class Solution:
    def majorityElement(self, nums):
        counter = 1
        value = nums[0]
        
        for i in range(len(nums)):
            if i == 0:
                continue
            
            if counter == 0:
                value = nums[i]
            
            if nums[i] == value:
                counter += 1
            else:
                counter -= 1
        
        return value




# 13 February 2024
#my solution

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPal(w):
            s = []
            for i in range(len(w)//2):
                s.append(w[i])
            if len(w) % 2 != 0:
                for j in range(len(w)//2 +1 , len(w)):
                    if w[j] == s[-1]:
                        s.pop()
                        continue
                    else:
                        return False
            if len(w) % 2 == 0:
                for j in range(len(w)//2 , len(w)):
                    if w[j] == s[-1]:
                        s.pop()
                        continue
                    else:
                        return False
            return True

        for k in words:
            if isPal(k) == True:
                return k
        return ""
    


#good solution
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            if i == i[::-1]:
                return i
        return ""



# 14 February 2024
#my code

class Solution:
    def rearrangeArray(self, nums):
        result = []
        positive_stack = []
        negative_stack = []
        for i in nums:
            if i>0:
                positive_stack.append(i)
            else:
                negative_stack.append(i)
        for j, k in zip(positive_stack, negative_stack):
            result.append(j)
            result.append(k)
        return result



# 15 February 2024
#My solution;
class Solution:
    def largestPerimeter(self, nums):
        n = len(nums)
        nums.sort()
        for i in range(n-1, 1, -1):
            if nums[i] >= sum(nums[:i]):
                continue
            else:
                return sum(nums[:i+1])

        return -1



#Optimised Solution;
class Solution:
    def largestPerimeter(self, nums):
        while(True):
            if len(nums) != 0:
                m = max(nums)
            else:
                break
            nums.remove(m)
            if sum(nums) > m:
                return sum(nums) + m
        return -1



# 16 February 2024

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



# 17 February 2024
import heapq
from collections import List

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
       p, i = [], 0
       for i in range(len(heights) - 1):
           diff = heights[i + 1] - heights[i]
           if diff <= 0:
               continue
           bricks = bricks - diff
           x = heapq.heappush(p, -diff)
           print(x)
           if bricks < 0:
               bricks = bricks + -heapq.heappop(p)
               ladders = ladders - 1
           if ladders < 0:
               return i
       return len(heights)-1



# 18 February 2024
#solution;
class Solution:
    def mostBooked(self, n, meetings):
        ans = [0] * n
        times = [0] * n
        meetings.sort()

        for start, end in meetings:
            flag = False
            minind = -1
            val = float('inf')
            for j in range(n):
                if times[j] < val:
                    val = times[j]
                    minind = j
                if times[j] <= start:
                    flag = True
                    ans[j] += 1
                    times[j] = end
                    break
            if not flag:
                ans[minind] += 1
                times[minind] += (end - start)

        maxi = -1
        id = -1
        for i in range(n):
            if ans[i] > maxi:
                maxi = ans[i]
                id = i
        return id



#Good Solution;
class Solution:
    def mostBooked(self, n, meetings):
        available_rooms = list(range(n))
        used_rooms = []
        meetings_per_room = [0] * n
 
        for start, end in sorted(meetings):
            while used_rooms and used_rooms[0][0] <= start:
                _, room = heappop(used_rooms)
                heappush(available_rooms, room)

            if available_rooms:
                room = heappop(available_rooms)
                heappush(used_rooms, (end, room))
            else:
                room_end, room = heappop(used_rooms)
                room_end += end - start
                heappush(used_rooms, (room_end, room))
            meetings_per_room[room] += 1

        max_index, max_value = max(enumerate(meetings_per_room), key=operator.itemgetter(1))
        return max_index



# 19 February 2024




# 20 February 2024

class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        sl = sum(nums)
        s = (n * (n+1)) // 2
        return s - sl




# 21 February 2024
#good
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        result = 0
        while left != right:
            left >>= 1
            right >>= 1
            result += 1
        return left << result




#best solution by other.
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        bl, br = bin(left)[2:], bin(right)[2:]
        if len(br) > len(bl):
            return 0
        
        for i in range(len(br)):
            if bl[i] != br[i]:
                break
        
        return int(bl[:i + 1].ljust(len(br), '0'), 2)



# 22 February 2024
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusting = [0] * (n + 1)
        trusted = [0] * (n + 1)

        for t in trust:
            trusting[t[0]] += 1
            trusted[t[1]] += 1

        ans = -1

        for i in range(1, n + 1):
            if trusting[i] == 0 and trusted[i] == n - 1:
                ans = i

        return ans



# 23 February 2024
    



# 24 February 2024
    



# 25 February 2024
    



# 26 February 2024
    



# 27 February 2024
    


# 28 February 2024
    


# 29 February 2024
    
