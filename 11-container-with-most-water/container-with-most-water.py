class Solution:
    def maxArea(self, height: List[int]) -> int:
        # BRUTE FORCE SOLUTION:
        # if not height:
        #     return 0
        # area = 0
        # for left in range(len(height)):
        #     for right in range(left + 1, len(height)):
        #         w = right - left
        #         area = max(area, min(height[left], height[right]) * w)
        # return area

        # TWO POINTER SOLUTION:
        if not height:
            return 0
        
        left, right, area = 0, len(height) - 1, 0

        while left < right:
            w = right - left
            area = max(area, min(height[left], height[right]) * w)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return area            