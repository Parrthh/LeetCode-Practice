class Solution:
    # Brute-Force Solution:
    # def climbStairs(self, n: int) -> int:
            # Calling our helper function for 0 -> n
    #     return self.climbing_stairs(0,n)
    
    # def climbing_stairs(self, i: int, n: int) -> int:
            # To check if we are going out of bounds
    #     if i > n:
    #         return 0
            # This means we reach our final step
    #     if i == n:
    #         return 1

    #     return self.climbing_stairs(i+1, n) # No of ways to reach the top from the current step, simulates taking 1 step
            #  + self.climbing_stairs(i+2, n) # No. of ways to reach the top from the current step, simulates taking 2 steps
    # The sum of these two recursive calls represents the no. of ways to reach the top from step i

    # Time Complexity: O(2**n)

    # Bottom-Up DP Solution
    def climbStairs(self, n: int) -> int:
        # We initialize and one and two pointers
        # The idea behind this approach is
        # Two -> basically is at the last step in the array
        # One -> is one a previous step
        one, two = 1,1 

        # To calculate the result we will be looping from n - 1, because we already know
        # The ways we are going to get to the last step

        for i in range(n-1):
            # Before shifting the pointers, we store the value of in temp
            # Because when two will be shifted it will be at the previous step where one was
            temp = one
            # To move one pointer we need to add one + two 
            one = one + two
            two = temp
        # Because pointer one will reach the last step first
        return one
