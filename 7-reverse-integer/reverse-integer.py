class Solution:
    def reverse(self, x: int) -> int:
        # Define the 32-bit signed integer range
        # MIN is the smallest integer (-2^31), and MAX is the largest integer (2^31 - 1)
        MIN = -2147483648  # -2^31
        MAX = 2147483647   # 2^31 - 1

        res = 0
        while x:
            # Get the last digit of x using `math.fmod(x, 10)`, which works better for negative numbers
            digit = int(math.fmod(x,10)) # Python's mod operator handles -1 % 10 as 9
            x = int(x/10)# Remove the last digit from x

            # Check for overflow before adding the next digit
            if (res > MAX // 10) or (res == MAX // 10 and digit > MAX % 10):
                return 0  # Overflow condition for positive range
            
            if (res < MIN // 10) or (res == MIN // 10 and digit < MIN % 10):
                return 0  # Overflow condition for negative range

            # Update the reversed number with the current digit
            res = (res * 10) + digit
        return res

"""
# Time Complexity : O(log x) -> since we process each digit x
# Space Complexity: O(1) -> as we use constant amount of extra space

"""