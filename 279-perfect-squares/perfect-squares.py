class Solution:
    def numSquares(self, n: int) -> int:
        # Step 1: Initialize a dp array where dp[i] will store the minimum number of perfect squares required to get the sum i.
        # We set each dp[i] to infinity initially, as we're looking for the minimum.
        dp = [float('inf')] * (n + 1)
        
        # Base case: To make a sum of 0, we need 0 perfect squares.
        dp[0] = 0

        # Step 2: Process each number from 1 to n.
        for i in range(1, n + 1):
            j = 1  # Start with the smallest square (1^2)
            
            # Step 3: For each i, try all squares j^2 where j^2 <= i.
            # This loop checks every perfect square up to i.
            while j * j <= i:
                # Update dp[i] by taking the minimum between the current value of dp[i]
                # and dp[i - j*j] + 1 (using one more square, j^2, to reach i)
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1  # Move to the next square
        
        # After filling up dp array, dp[n] will hold the minimum number of squares for sum n.
        return dp[n]


"""
TIME COMPLEXITY:  
1. The time complexity of this solution is O(n *sqrt(n)).
2. Because for every integer from 1 to n, we check up to the square root of i in inner loop,
resulting in roughly sqrt(n) operations per i.
3. Therefore, O(n * sqrt(n))

SPACE COMPLEXITY: O(N)
1. The space complexity is O(n) for the dp array used to store the minimum number of squares required
for each value up to n


SPACE COMPLEXITY:




"""