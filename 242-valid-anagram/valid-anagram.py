class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s, dict_t = {}, {}
        for i in s:
            if dict_s.get(i, None) == None:
                dict_s[i] = 1
            else:
                dict_s[i] += 1
            
        for i in t:
            if dict_t.get(i, None) == None:
                dict_t[i] = 1
            else:
                dict_t[i] += 1
            

        return True if dict_s == dict_t else False

        