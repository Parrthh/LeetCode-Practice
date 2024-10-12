class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #To keep track of numbers in the array
        
        dic_t = {}
        for num in nums:
                dic_t[num] = 1

        # Initializing an empty list
        result = []
        for num in range(1,len(nums)+1):
            if num not in dic_t:
                result.append(num)
        return result
        



        