class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j =  0,0
        n = len(word1)
        m = len(word2)
        res = []
        while i <n or j <m:
            if i <n:
                res.append(word1[i])
                i+=1
            if j <m:
                res.append(word2[j])
                j+=1
        return "".join(res)