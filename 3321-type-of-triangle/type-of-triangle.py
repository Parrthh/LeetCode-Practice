class Solution:
    def triangleType(self, nums: List[int]) -> str:
        i,j,k = nums

        if i + j <= k or i + k <= j or k + j <= i:
            return "none"
        
        if i == j == k:
            return "equilateral"
        elif i == j or i == k or j == k:
            return "isosceles"
        else:
            return "scalene"
        
        