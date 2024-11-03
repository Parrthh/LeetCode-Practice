class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = 0  # Minimum possible open parentheses count
        max_open = 0  # Maximum possible open parentheses count

        for c in s:
            if c == '(':
                min_open += 1
                max_open += 1
            elif c == ')':
                min_open = max(min_open - 1, 0)  # Don't let min_open go below 0
                max_open -= 1
            else:  # `c == '*'`
                min_open = max(min_open - 1, 0)  # `*` acts as a close or empty
                max_open += 1  # `*` acts as an open parenthesis

            # If max_open becomes negative, it means we have too many closing parentheses
            if max_open < 0:
                return False

        # After the loop, `min_open` should be 0 for the string to be balanced
        return min_open == 0
