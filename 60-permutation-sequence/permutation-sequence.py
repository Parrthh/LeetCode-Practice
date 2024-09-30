from itertools import permutations

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        p = list(permutations(range(1,n+1)))
        return ''.join(str(i) for i in p[k-1])