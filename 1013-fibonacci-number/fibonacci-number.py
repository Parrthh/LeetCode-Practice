class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        cache = [0] * (n + 1)
        cache[0] = 0
        cache[1] = 1
        for i in range(2, n +1):
            cache[i] = cache[i - 1] + cache[i - 2]
        return cache[n]


"""
TIME COMPLEXITY: O(N) -> bottom-up approach
1. Each number, starting at 2 up to and incuding N, is visited computed and then sorted for O(1)
access later on


SPACE COMPLEXITY: O(n)
1. The size of the data structure is proportional to N


"""
