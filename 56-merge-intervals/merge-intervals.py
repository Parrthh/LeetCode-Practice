class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # If there are no intervals, return an empty list
        if not intervals:
            return []
        
        # Sort the intervals based on the start time
        intervals.sort(key = lambda x:x[0])

        # Initialize the result list with the first interval
        result = [intervals[0]]

        # Iterate through the intervals to merge overlapping ones
        for i in range(1, len(intervals)):
            # Get the last interval in the result list
            last_interval = result[-1]
            current_interval = intervals[i]
            # If the current interval overlaps with the last interval
            if current_interval[0] <= last_interval[1]:
                # Merge them by updating the end of the last interval
                last_interval[1] = max(last_interval[1], current_interval[1])
            else:
                # Otherwise, add the current interval to the result list
                result.append(current_interval)
        return result
                

"""
TIME COMPLEXITY : O(n log n)


SPACE COMPLEXITY: O(n)

"""
        