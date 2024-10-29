class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        # Step 2: Initialize merged list to hold merged intervals
        merged = []

        # Step 3: Iterate through the sorted intervals
        for interval in intervals:
            # If merged is empty or there is no overlap, add the interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # There is an overlap, so merge with the last interval in merged
                merged[-1][1] = max(merged[-1][1], interval[1])

        # Step 4: Return the merged intervals
        return merged
        