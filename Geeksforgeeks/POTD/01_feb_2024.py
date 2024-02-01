class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        d = s.lower()
        for i in range(26):
            if alphabet_list[-1] in d:
                alphabet_list.pop()
        
        if len(alphabet_list)==0:
            return 1
        else:
            return 0