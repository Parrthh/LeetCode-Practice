class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        # Just concatenate the string and you can find different variations of the original string
        double_string = s + s
        # Check if the goal is a part of the concatenated string 
        # If yes -> return True
        return True if goal in double_string else False


"""
TIME COMPLEXITY: O(n)
1. Concatenating the string takes O(n)
2. Checking the lengths of both strings are different takes O(n)

SPACE COMPLEXITY: O(n)
1. Since it is storing a string that is double the size of s (specifically: O(2 *n) similar to O(n))
2. Overall space complexity is O(n)


"""