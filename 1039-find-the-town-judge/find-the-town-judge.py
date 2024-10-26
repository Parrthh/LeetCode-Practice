class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int: 
        # STEP - 1: Edge to check if there is only one person in town or trust list is incomplete:
        if n == 1 and trust:
            return 1
        # Initialize two counters indegree and outdegree  of size n + 1 due to 1-based indexing
        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)

        # For each trust relationship increase the outdegree of a by 1
        # For each trust relationship increase the indegree of b by 1
        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1

        # Loop through each person from 1 to n, to find the judge
        for i in range(1, n+1):
            if indegree[i] == n-1 and outdegree[i] == 0:
                return i
        # EGDE CASE: Wherein there is no outdegree == 0, return -1
        return -1

        