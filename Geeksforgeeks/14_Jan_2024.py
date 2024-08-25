class Solution:
    def repeatedRows(self, arr, m ,n):
        
        duplicates_row = []
        
        for rows in range(m):
            for i in range(rows+1, m):
                if arr[rows] == arr[i]:
                    if i not in duplicates_row:
                        duplicates_row.append(i)
        
        return sorted(duplicates_row)