class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for i in strs:
            # We are encoding the input string in the following way:
            # 1. Every string will have a str(len(s)) + the delimiter ("#") + the word
            res += str(len(i)) + "#" + i
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        res = []
        i = 0
        while i < len(s):
            # Move j to find the position of the delimiter '#'
            j = i
            while s[j] != "#":
                j += 1
            
            # Extract the length of the next string (from i to j)
            length = int(s[i:j])
            
            # Extract the string using the length after the '#'
            res.append(s[j + 1: j + 1 + length])
            
            # Move i to the start of the next encoded part
            i = j + 1 + length
        return res

"""
TIME COMPLEXITY: 
ENCODE: 
1. Each string in strs processed once. Sorting each string takes O(L), where L -> length of string
2. The overall time complexity is O(N L), where N -> number of strings, L -> avg length of string
DECODE: 
We process each character in the encoded string s once, so it also takes O(N L)

SPACE COMPLEXITY:
1. both encode and decode methods have space complexity O(N L)
where, N -> number of strings
L -> avg length of strings in strs
2. This is due to the storage required for the encoded string and the decoded list of strings

"""



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))