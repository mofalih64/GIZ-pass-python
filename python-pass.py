class Solution:

    @staticmethod
    def longest_palindromic(s: str) -> str:
         if len(s) <= 1:
            return s
        i,k=0,0
        for j in range(len(s)):
            if s[j-k: j+1] == s[j-k: j+1][::-1]:
                i, k = j-k, k+1
               
            elif j-k > 0 and s[j-k-1: j+1] == s[j-k-1: j+1][::-1]:
                i, k = j-k-1, k+2
        return s[i: i+k]