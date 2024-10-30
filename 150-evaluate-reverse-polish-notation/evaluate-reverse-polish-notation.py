class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Initializing an empty stack
        stack = []
        # For loop to iterate over token and append characters after changing them into int
        for elements in tokens:
            # So basically, if our elements are not "+-*/"
            # then we are converting them into int data type and appending in stack
            # Once we encounter a arithmetic operand, we pop the elements and perform operations
            if elements not in "+-*/":
                stack.append(int(elements))
                continue
            # Pop the elements when we encounter a arithmetic operand
            element2 = stack.pop()
            element1 = stack.pop()
            # Initializing the result to 0 to store our computations
            result = 0
            if elements == "+":
                result = element1 + element2
            elif elements == "-":
                result = element1 - element2
            elif elements == "*":
                result = element1 * element2
            else:
                result = int(element1 / element2)
            # To append the result calculated
            stack.append(result)
        # We pop 0 because at this point we know all the operations are carried out
        # Our stack just consumes one elements which is stored after all the computations
        return stack.pop(0)
