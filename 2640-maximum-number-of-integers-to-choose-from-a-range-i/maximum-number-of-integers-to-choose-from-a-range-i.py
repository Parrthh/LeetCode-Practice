class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned.sort()
        count = 0
        
        for num in range(1, n + 1):
            if self.binary_search(banned, num): continue
            maxSum -= num
            if maxSum < 0:
                break
            count += 1

        return count
    
    def binary_search(self, a: List[int], target: int) -> bool:
        left, right = 0, len(a) - 1
        while left <= right:
            mid = (left + right) // 2
            if a[mid] == target:
                return True
            if a[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

"""
TIME COMPLEXITY: O((m + n) * logm)
1. We are iterating through numbers from 1 to n, and for each number, performs a binary search of the banned array.
2. The binary search takes O(logm) time, and we do this n times.
3. Therefore, the total time complexity of the algorithm is O(n * logm) + O(m * logm) = O((m + n) logm)
"""