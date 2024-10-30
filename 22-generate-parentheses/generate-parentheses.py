class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtracking_solution(current: str, open: int, close: int):
            if len(current) == 2 * n:
                result.append(current)
                return
            if open < n:
                backtracking_solution(current + "(", open +1, close)
            
            if close < open:
                backtracking_solution(current + ")", open, close + 1)
        backtracking_solution("", 0 , 0)
        return result