# Code to be insterted here

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # recursion to go through all possible combinations.
        def dfs(left, right, s):
            
            # ---- BASE CASE ----
            # exit condition to break out of recusive loop
            if len(s) == n * 2:
                res.append(s)
                return 

            # recursive cases
            # continue recursion based on conditions

            # first recursive case
            if left < n:
                dfs(left + 1, right, s + '(')

            # ssecond recursive case
            if right < left:
                dfs(left, right + 1, s + ')')

        res = []
        dfs(0, 0, '')
        return res
        
