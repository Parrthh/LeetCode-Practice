class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([char.lower() for char in s if char.isalnum()])
        if len(s) == 1:
            return True
        
        return bool(s == ''.join(reversed(s)))
