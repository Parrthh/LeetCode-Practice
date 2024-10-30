class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        if len(intervals) == 1:
            return 1
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        left, right = 0, 0
        used = 0
        while left < len(intervals):
            if start[left] >= end[right]:
                used -= 1
                right += 1
            used += 1
            left += 1

        return used
 
        