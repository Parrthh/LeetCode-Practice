class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic_t = {}
        for a,b in zip(s,t):
            if dic_t.get(a, False) == b:
                continue
            elif b in dic_t.values():
                return False
            elif dic_t.get(a, False) == False:
                dic_t[a] = b
            else:
                return False

        return True
        