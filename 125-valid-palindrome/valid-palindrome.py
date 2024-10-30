class Solution:
    def isPalindrome(self, s: str) -> bool:
        # BRUTE FORCE APPROACH:
        # s = ''.join([char.lower() for char in s if char.isalnum()]) 
        # return bool(s == ''.join(reversed(s)))

        """
        TIME COMPLEXITY : O(N) -> 
        1. We iterate through each character in the string s to check if its alphanumeric and convert it to lowercase if it is.
        2. This step takes O9n), where n is the lenght of the input string
        3. Reversing the string takes O(n) time to iterate through each cleaned string in reverse
        4. Constructing the a new string is also O(n)
        5. Comparing the original string with its reversed version requires o(n) times

        SPACE COMPLEXITY: O(N) ->
        1. The cleaned version of s takes up O(n) space because it stores a copy of the filtered, lowercase characters
        2. The reversed version of s also takes O(n) space
        3. therefore, space complexity is O(n) + O(n) -> O(n)
         """
        # TWO POINTER APPROACH:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            
            while left<right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
        return True

        """
        TIME COMPLEXITY -> O(N)
        1. Two pointer left and right traverse the string at most once from both ends, moving towards the center
        2. Since each character is visited once, this approach takes O(n) time.

        SPACE COMPLEXITY -> O(1)
        1. The two pointer approach only uses a constant amount of extra space for the pointers and character comparisons
        2. Therefore, space complexity is O(1) because no additional storage is required for a cleaned or reversed string
        """




