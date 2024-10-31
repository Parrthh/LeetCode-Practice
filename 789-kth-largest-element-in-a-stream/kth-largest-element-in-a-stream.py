class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Initialize the object with the k-th largest position and an initial list of numbers
        self.k = k
        self.streams = nums
        
        # Sort the list in ascending order to maintain a sorted list of elements
        self.streams.sort()

    def add(self, val: int) -> int:
        # Insert the new value `val` in its correct sorted position
        index = self.getIndex(val)  # Find the correct index to insert `val`
        self.streams.insert(index, val)  # Insert `val` in sorted order
        
        # Return the k-th largest element, which is the `-k` position from the end of the list
        return self.streams[-self.k]

    def getIndex(self, val: int) -> int:
        # Perform binary search to find the correct index for inserting `val` in sorted order
        left, right = 0, len(self.streams) - 1
        while left <= right:
            mid = (left + right) // 2  # Calculate the middle index
            mid_element = self.streams[mid]  # Element at the middle index
            
            # If mid_element is equal to `val`, return the middle index for insertion
            if mid_element == val:
                return mid
            
            # If mid_element is greater than `val`, search the left half
            elif mid_element > val:
                right = mid - 1
            
            # If mid_element is less than `val`, search the right half
            else:
                left = mid + 1
                
        # Return the index where `val` should be inserted (this will be `left` when the loop ends)
        return left

# TIME COMPLEXITY:
# __init__() function:
# - Sorting the list `streams` during initialization takes `O(n log n)`, where `n` is the length of `nums`.
#
# add() function:
# - The add method calls getIndex() (which has a time complexity of `O(log n)` for binary search)
#   and insert (which has a time complexity of `O(n)` due to shifting elements).
# - Therefore, each call to add() has a time complexity of `O(n)`.
#
# Overall:
# - The overall time complexity for multiple add calls is `O(m * n)`, where `m` is the number of add calls
#   and `n` is the number of elements in `streams`.

# SPACE COMPLEXITY: O(n)
# - We store `n` elements in the list `streams`, so the space complexity is `O(n)`.

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)