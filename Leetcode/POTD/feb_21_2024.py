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