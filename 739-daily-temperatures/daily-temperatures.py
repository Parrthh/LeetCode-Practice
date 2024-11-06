from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Step 1: Initialize necessary variables
        n = len(temperatures)  # Get the length of the temperatures list
        answer = [0] * n  # Initialize the answer list with 0s for all days
        stack = []  # Initialize a stack to keep track of indices of decreasing temperatures

        # Step 2: Iterate over each day and its temperature in the temperatures list
        for current_day, current_temperature in enumerate(temperatures):
            # Check if there's a day in the stack with a lower temperature than the current day
            while stack and temperatures[stack[-1]] < current_temperature:
                # Pop the last day from the stack to calculate the waiting days
                previous_day = stack.pop()
                # Calculate the difference in days between the current day and previous day
                answer[previous_day] = current_day - previous_day
            
            # Step 3: Push the current day index onto the stack
            stack.append(current_day)
        
        # Step 4: Return the filled answer array
        return answer
"""
TIME COMPLEXITY: O(N)
Each element is pushed and popped from the stack once, giving an O(n) time complexity

SPACE COMPLEXITY: O(N)
The answer list and the stack grow up to size of n, so the space complexity is O(n)

"""