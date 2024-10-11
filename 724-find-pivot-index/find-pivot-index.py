class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lhs_sum = 0
        rhs_sum = sum(nums)

        '''n = len(nums)
        print(n)
        if n/2 != 0:
            return -1'''
        i=0
        for x in nums:
            
            rhs_sum -= x

            
            if rhs_sum == lhs_sum:
                return i
            i+=1
            lhs_sum += x

        return -1
                

        
        
        # lhs_sum = 0
        # rhs_sum = sum(nums)

        
        