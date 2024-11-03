class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Special case: If k equals the length of nums, all elements are equally frequent,
        # so we can return the entire nums list directly.
        if k == len(nums):
            return nums
        
        # Step 1: Count the frequency of each element in nums
        # Using Counter, we get a dictionary where each key is a unique element in nums
        # and each value is the count (frequency) of that element in nums.
        count = Counter(nums)
        print(count)
        
        # Step 2: Use a max heap to find the k most frequent elements
        # heapq.nlargest allows us to get the k largest values based on a custom key function.
        # Here, we use `count.get` as the key, which will return values (frequencies) from the count dictionary.
        # This returns the top k keys (elements) with the highest frequencies.
        return heapq.nlargest(k, count.keys(), key=count.get)

       