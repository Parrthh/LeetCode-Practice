class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            # Add the current subset (path) to the result list
            result.append(path[:])

            # Loop through elements starting from 'start' index
            for i in range(start, len(nums)):
                # Include nums[i] in the current subset
                path.append(nums[i])
                # Recurse with the next index
                backtrack(i + 1, path)
                # Backtrack: Remove nums[i] to explore the next possibility
                path.pop()

        # Start the backtracking process with an empty subset
        backtrack(0, [])
        return result


"""
TIME COMPLEXITY: O(2 ^ n)
1. There are 2 ^ n possible subsets for an array of size n

SPACE COMPLEXITY: O(N)
1. The maximum depth of the recursion tree is n and each subset can use up to n space
"""