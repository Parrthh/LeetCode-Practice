class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Initializing left hand side sum to 0
        lhs_sum = 0
        # Taking a sum and store in rhs_sum
        rhs_sum = sum(nums)

        '''n = len(nums)
        print(n)
        if n/2 != 0:
            return -1'''
        # Initializing i to 0, and we will increment it when sum(lhs == rhs)
        i=0
        # Looping over nums
        for x in nums:
            # Taking out the first index and then comparing with rhs
            rhs_sum -= x

            # Comparing the rhs and lhs
            if rhs_sum == lhs_sum:
                # If the sum on both sides is same, returning i which has the variable
                return i
            # if not, incrementing i by 1
            i+=1
            # Adding x to lhs, which has the first index value
            lhs_sum += x
        # if nothing found returning -1
        return -1
                

        
        