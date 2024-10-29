class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the last seen index of each character in the current window
        char_map = {}
        
        # Variable to keep track of the maximum length of a substring without repeating characters
        max_length = 0
        
        # Left pointer for the sliding window
        left = 0

        # Expand the window by moving the right pointer across the string
        for right in range(len(s)):
            current_char = s[right]  # The current character at the right pointer

            # Check if the current character is already in the map and within the window
            if current_char in char_map and char_map[current_char] >= left:
                # If it is, move the left pointer to the position after the last occurrence of this character
                # This removes the duplicate character from the current window
                left = char_map[current_char] + 1

            # Update the last seen index of the current character in the map
            char_map[current_char] = right

            # Calculate the length of the current window (right - left + 1)
            current_window_length = right - left + 1

            # Update the maximum length if the current window is longer
            max_length = max(max_length, current_window_length)

        # Return the length of the longest substring without repeating characters
        return max_length
