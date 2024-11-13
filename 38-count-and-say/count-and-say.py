class Solution:
    def countAndSay(self, n: int) -> str:
        # Start with the first sequence
        result = "1"

        # Build the sequence from 2 to n
        for _ in range(2, n + 1):
            current = ""  # This will store the new sequence
            count = 1  # Initialize the count of the current character
            
            # Traverse the previous sequence (result)
            for i in range(1, len(result)):
                # Check if the current character is the same as the previous character
                if result[i] == result[i - 1]:
                    count += 1  # Increment the count
                else:
                    # If the current character is different, append the count and previous character
                    current += str(count) + result[i - 1]
                    count = 1  # Reset the count for the new character
            
            # Append the count and last character (after the loop ends)
            current += str(count) + result[-1]
            
            # Update result to the current sequence
            result = current

        return result

"""
TIME COMPLEXITY: O(m * n)
1. Where n is the input integer and m is the length of the resulting string for each step

SPACE COMPLEXITY: O(m)
1. where m is the length of the current sequence

"""