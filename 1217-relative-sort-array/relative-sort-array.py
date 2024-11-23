class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        for i in arr2:
            for j in range(len(arr1)):
                if arr1[j] == i:
                    result.append(arr1[j])
                    arr1[j] = -1
        arr1.sort()
        for v in arr1:
            if v != -1:
                result.append(v)
        return result


"""
TIME COMPLEXITY: O(m * n + nlogn)
1. Iterate through each element of arr2 and for each element, we iterate through arr1 -> O(m * n)
2. Sorting the arr1 -> O(nlogn)
3. Iterating through arr1 to add non-marked elements to the result has a time complexity of O(n)

4. Therefore, overall time complexity: O(m * n + nlogn)

SPACE COMPLEXITY: O(n) or O(logn)
1. Apart from the result array and a few variables, the algorithms doesn't use any additional data structures.
"""