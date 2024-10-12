class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_pattern = {}
        map_s = {}

        w = s.split(' ')

        if len(w) != len(pattern):
            return False

        for a,b in zip(pattern,w):
            if a not in map_pattern:
                if b in map_s:
                    return False
                
                else:
                    map_pattern[a] = b
                    map_s[b] = a
            else:
                if map_pattern[a] != b:
                    return False
        return True
        
        
