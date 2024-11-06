class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)     # right is max possible eating speed of Koko

        while left < right:
            mid = (left + right) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/mid)
            if hours <= h:
                right = mid
            else:
                left = mid + 1
        return left
                
"""
TIME COMPLEXITY: O(n log(max(piles)))
1. Since each step in the binary search takes O(n) time to compute the required hrs for the current speed
2. Binary search alone has a time complexity of O(log(max(piles))), as it depends on the maximum value in piles
3. Therefore, the total time complexity computation is O(n log(max(piles)))

SPACE COMPLEXITY:
1. The space complexity is O(1) since we only use a few extra variables and no additional data structure
"""