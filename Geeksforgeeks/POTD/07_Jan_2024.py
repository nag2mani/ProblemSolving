#User function Template for python3

class Solution:
    def splitArray(self, arr, N, K):
        lo = max(arr)
        hi = sum(arr)

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.partitioning_is_valid(arr, K - 1, mid):
                hi = mid
            else:
                lo = mid + 1

        return lo

    def partitioning_is_valid(self, arr, partitions, partition_max_sum):
        accumulate_curr_partition = 0
        for num in arr:
            if num > partition_max_sum:
                return False
            elif accumulate_curr_partition + num <= partition_max_sum:
                accumulate_curr_partition += num
            else:
                partitions -= 1
                accumulate_curr_partition = num
                if partitions < 0:
                    return False
        return True

#finished