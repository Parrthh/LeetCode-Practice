class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        letters = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = []
        def backtracking_method(index: int, current_combination: str):
            # If the current combination is the same length as digits
            if index == len(digits):
                res.append(current_combination)
                return 
            
            # Get the letters corresponding to the current digit
            current_digit = digits[index]
            for letter in letters[current_digit]:
                backtracking_method(index + 1, current_combination + letter)
        backtracking_method(0, "")
        return res

"""
TIME COMPLEXITY: O(3^n * 4^m)
1. Where n is the number of digits mapping to 3 letters (2,3,4,5,6,8)
and m is the number of digits mapping to 4 letters (7,9)

SPACE COMPLEXITY: O(N)
1. Where n is the depth of the recursion stack (equal to the length of digits)

"""