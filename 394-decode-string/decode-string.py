class Solution:
    def decodeString(self, s: str) -> str:
        stack = []          # Stack to hold (current_string, current_repeat_count) paits
        current_string = "" # The current substring we are building
        current_num = 0

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == "[":
                stack.append((current_string, current_num))
                current_string = ""
                current_num = 0
            elif char == "]":
                last_string, repeat_count = stack.pop()
                current_string = last_string + current_string * repeat_count
            else:
                current_string += char
        return current_string


"""
TIME COMPLEXITY: O(N)
1. The time complexity is O(n), where n is the length of the string. 
2. Each character is processed once, and stack operations are efficient.

SPACE COMPLEXITY: O(N)
1. Due to stack used for storing intermediate states and the final decoded string


"""