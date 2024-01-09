class Solution:
    def search(self, pat, txt):
        indices = []
        txt_length = len(txt)
        pat_length = len(pat)

        for i in range(txt_length - pat_length + 1):
            if txt[i:i+pat_length] == pat:
                indices.append(i + 1)

        if not indices:
            return [-1]
        else:
            return indices