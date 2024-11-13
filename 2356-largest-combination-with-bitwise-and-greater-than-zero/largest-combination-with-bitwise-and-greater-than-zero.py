class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # Step 1: Initialize a bit count array of size 24 with all zeros.
        # This array will store the count of set bits (1s) at each bit position (0 to 23).
        bitCount = [0] * 24

        # Step 2: Iterate through each number in the candidates list.
        for num in candidates:
            # Step 3: For each bit position (from 0 to 23), check if the bit is set.
            for i in range(24):
                # Check if the i-th bit of num is set using (num & (1 << i)) != 0
                if (num & (1 << i)) != 0:
                    # If the i-th bit is set, increment the count for this bit position.
                    bitCount[i] += 1

        # Step 4: Find the maximum value in the bitCount array.
        # The maximum value represents the largest combination of numbers
        # that have a common set bit at the same position.
        return max(bitCount)
