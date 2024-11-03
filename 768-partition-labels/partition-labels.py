class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Step 1: Create a dictionary to store the last occurrence of each character in the string
        last = {c: i for i, c in enumerate(s)}
        # `last` will hold the furthest index of each character in `s`
        # Example for s = "abacbc": {'a': 2, 'b': 4, 'c': 5}

        # Initialize two pointers:
        # `start_point` will track the end of the current partition
        # `end_point` will track the beginning of the current partition
        start_point, end_point = 0, 0
        
        # `res` will store the sizes of each partition
        res = []

        # Step 2: Iterate through each character and its index in the string
        for i, c in enumerate(s):
            # Update `start_point` to the farthest last occurrence of any character in the current partition
            start_point = max(start_point, last[c])

            # Check if the current index `i` is the end of the current partition
            if i == start_point:
                # If so, calculate the size of this partition and add it to `res`
                # Partition size is `i - end_point + 1`
                res.append(i - end_point + 1)
                
                # Move `end_point` to the start of the next partition
                end_point = i + 1

        # Step 3: Return the result list containing the sizes of each partition
        return res

# Time Complexity: O(n)
# - We iterate over the string twice: once to create the `last` dictionary and once to find partitions.
# - Each operation inside the loop (like `max` and dictionary access) takes constant time.
# - Therefore, the overall time complexity is O(n), where n is the length of the string `s`.

# Space Complexity: O(1) if we ignore the output list `res`
# - The `last` dictionary requires O(26) space at most, as there are at most 26 lowercase letters.
# - `res` will store partition sizes and is directly proportional to the number of partitions, which in the worst case is limited to 26 partitions for 26 characters.
# - So, if we exclude the output `res`, the auxiliary space complexity is O(1) since the dictionary has a fixed size.
