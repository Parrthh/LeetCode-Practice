class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # If there are no meetings, no rooms are needed
        if not intervals:
            return 0
        
        # If there's only one meeting, we need only one room
        if len(intervals) == 1:
            return 1

        # Step 1: Separate start and end times, and sort them
        start = sorted([i[0] for i in intervals])  # Sorted start times of meetings
        end = sorted([i[1] for i in intervals])    # Sorted end times of meetings

        # Time Complexity for sorting: O(n log n), where n is the number of intervals
        # Space Complexity: O(n) for storing the start and end times separately

        # Step 2: Initialize pointers for the start and end lists
        left, right = 0, 0  # 'left' for start times, 'right' for end times
        used = 0            # Tracks the current number of rooms in use

        # Step 3: Loop through each meeting start time
        while left < len(intervals):
            # If the current meeting can start after the earliest meeting ends
            if start[left] >= end[right]:
                # Free up a room by decrementing 'used' since one meeting has ended
                used -= 1
                # Move the 'right' pointer to the next end time
                right += 1
            
            # Increment 'used' to account for the current meeting starting
            used += 1
            # Move the 'left' pointer to the next start time
            left += 1

            # The maximum number of rooms used at any time will be stored in `used`
        
        # Return the maximum number of rooms used at any time
        return used
    
        