class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Initializing both the pointer at 0
        i = 0
        j = 0

        # While loop to check if s is a subsequence of t or not
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1
            j+=1
        
        if i == len(s):
            return True
        else:
            return False
        
        