class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Initializing right most element as -1
        r = -1
        # Reverse Iteration
        for i in range(len(arr) - 1, -1, -1):
            n = max(r, arr[i])
            arr[i] = r
            r = n
        return arr