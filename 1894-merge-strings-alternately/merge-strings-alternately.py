class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        i, j = 0, 0

        while i < len(word1) or j < len(word2):
            if i < len(word1):
                merged.append(word1[i])
                i += 1
            
            if j < len(word2):
                merged.append(word2[j])
                j += 1
        return "".join(merged)


"""
TIME COMPLEXITY: O(max(n,m))
1. Where n and m are the lengths of word1 and word2

SPACE COMPLEXITY: O(n + m)
1. Due to the merged string
"""