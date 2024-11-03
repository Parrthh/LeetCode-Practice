class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Define a helper function to recursively calculate power
        def helper_function(x, n):
            # Base case 1: If x is 0, x^n will be 0 for any positive n
            if x == 0:
                return 0
            
            # Base case 2: If n is 0, x^0 is always 1
            if n == 0:
                return 1
            
            # Recursive call to calculate x^(n//2)
            res = helper_function(x, n // 2) # Also known as Exponentiation by Squaring (or Fast Exponentiation)
            
            # Square the result to get (x^(n//2))^2, which is x^n for even n
            res *= res
            
            # If n is odd, multiply one extra x to get x^n
            return x * res if n % 2 != 0 else res

        # Calculate the result for the absolute value of n
        res = helper_function(x, abs(n))
        
        # If n is positive, return res; if n is negative, return 1 / res
        return res if n >= 0 else 1 / res

# TIME COMPLEXITY: O(log n)
# - The function recursively divides n by 2 at each step, which reduces the number of recursive calls to log(n).
# - For each recursive call, we perform constant-time operations (multiplication), so the overall time complexity is O(log n).

# SPACE COMPLEXITY: O(log n)
# - The function uses a recursive call stack. Since n is divided by 2 at each step, there are log(n) levels of recursion.
# - Therefore, the space complexity is O(log n) due to the recursion stack.



