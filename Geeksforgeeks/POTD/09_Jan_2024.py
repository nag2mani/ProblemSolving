# Knuth-Morris-Pratt (KMP) String Matching Algorithm

class Solution:
    # def Brutforce(self, pat, txt):
    # M = len(pat)
    # N = len(str) 
    # for i in range(N - M + 1):
    #     j = 0
    #     while(j < M):
    #         if (str[i + j] != pat[j]):
    #             break
    #         j += 1
 
    #     if (j == M):
    #         print("Pattern found at index ", i)










    # def search(self, pat, txt):
    #     indices = []
    #     txt_length = len(txt)
    #     pat_length = len(pat)

    #     for i in range(txt_length - pat_length + 1):
    #         if txt[i:i+pat_length] == pat:
    #             indices.append(i + 1)

    #     if not indices:
    #         return [-1]
    #     else:
    #         return indices


