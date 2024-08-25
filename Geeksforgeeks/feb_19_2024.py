class Solution:
    def minValue(self, s, k):
        def get_key(d, v):
            for key, value in d.items():
                if v == value:
                    return key
                    
        dict = {}
        s1 = set(s)
        for i in s1:
            dict[i] = s.count(i)
        sum = 0
        for i in range(k):
            m = max(dict.values())
            corr_key = get_key(dict, m)
            dict[corr_key] -= 1
            
        for i in dict.keys():
            x = dict[i]
            sum += x*x
            
        return sum
        