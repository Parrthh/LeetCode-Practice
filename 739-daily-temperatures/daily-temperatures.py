class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Stores the number of days 
        n = len(temperatures)
        # Creates an answer array of the same lenght as temperatures
        # Because if there is no warmers day the answer remains 0
        answer = [0] * n
        # Monotonic stack
        # The stack here stores the indices keeping track of the indices of days with dec temp
        stack = []

        # The for loop iterates through the whole list of temperature
        # It keeps track of the current day and its temperature
        for current_day, current_temperature in enumerate(temperatures):
            # The while loop here checks for the current day of the temperature 
            # and if it is warmer than the day represented by the current top of the stack
            while stack and temperatures[stack[-1]] < current_temperature:
                # Pop the previous day to check
                previous_day = stack.pop()
                # Calculate the index
                answer[previous_day] = current_day - previous_day
            # Appending the index
            stack.append(current_day)
        
        return answer  

