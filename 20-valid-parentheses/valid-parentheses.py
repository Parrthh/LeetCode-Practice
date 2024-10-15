class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        close_and_open = {')':'(',']':'[','}':'{'}

        for checking in s:
            if checking in close_and_open:
                if stack and stack[-1] == close_and_open[checking]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(checking)
        return not stack 