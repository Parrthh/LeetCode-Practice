class Solution:
    # Brute - Force solution:
    # def numDecodings(self, s: str) -> int:
    #     return self.decode_way(s,0)
        
    # def decode_way(self, s: str, idx: int) -> int:
    #     if idx == len(s):
    #         return 1
    #     if s[idx] == '0':
    #         return 0
    #     count = self.decode_way(s, idx + 1)

    #     if idx + 1 < len(s) and (s[idx] == '1' or (s[idx] == '2' and s[idx + 1] in "0123456")):
    #         count += self.decode_way(s, idx + 2)
        
    #     return count

    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}  # Base case: one way to decode an empty string

        def decode_way(i):
            if i in dp:
                return dp[i]
            if s[i] == '0':
                return 0

            # Single digit decode
            count = decode_way(i + 1)

            # Two-digit decode (if valid)
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in '0123456')):
                count += decode_way(i + 2)

            dp[i] = count  # Memoize the result
            return count

        return decode_way(0)

