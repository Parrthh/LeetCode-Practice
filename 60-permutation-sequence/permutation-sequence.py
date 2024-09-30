from itertools import permutations

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # create permutation list
        p = list(permutations(range(1,n+1)))
        # return 'kth' element from permutation list
        return ''.join(str(i) for i in p[k-1])