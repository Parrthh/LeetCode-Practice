class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # The goal is to find the number of plates that are enclosed betwen candes for given query
        # We want to avoid repeatedly scanning the entire substring for each query
        # Step - 1: Build the prefix sum array for plates
        n = len(s)
        prefix_sum = [0] * n
        plate = 0
        left_candle = [-1] * n
        right_candle = [-1] * n

        # Step - 2: Calculating prefix sum for plates
        for i in range(n):
            if s[i] == "*":
                plate += 1
            prefix_sum[i] = plate
        
        # Step - 3: Build the left candle array
        last_candle = -1
        for i in range(n):
            if s[i] == "|":
                last_candle = i
            left_candle[i] = last_candle
        
        # Step -4: Build the right candle array
        last_candle = -1
        for i in range(n-1, -1, -1):
            if s[i] == "|":
                last_candle = i
            right_candle[i] = last_candle
        
        # Step - 5: Process each query
        result = []
        for left, right in queries:
            left_boundary = right_candle[left]
            right_boundary = left_candle[right]
        
            if left_boundary != -1 and right_boundary != -1 and left_boundary < right_boundary:
                plates_between = prefix_sum[right_boundary] - prefix_sum[left_boundary]
                result.append(plates_between)
            else:
                result.append(0)
        return result


"""
TIME COMPLEXITY: O(n + q)
1. where n is the length of the sting, and q is the number of queries

SPACE COMPLEXITY: O(1)
1. The solution uses O(n) spaces for the prefix sum and candle arrays


"""