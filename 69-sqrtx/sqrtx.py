class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        i = 1
        while i * i <= x:
            i += 1

        return i - 1

"""
TIME COMPLEXITY : O(log x)

SPACE COMPLEXITY : O(1)
"""