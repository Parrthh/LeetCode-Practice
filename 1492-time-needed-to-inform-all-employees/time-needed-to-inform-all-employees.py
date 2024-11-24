class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Create an adjacency list to store subordinates of each manager
        subordinate = defaultdict(list)

        # Build the adjacency list representation of the tree
        for i in range(n):
            # If the employee has a manager, add the employee to the manager's subordinate list
            if manager[i] != -1:
                subordinate[manager[i]].append(i)

        # Depth-First Search (DFS) function to calculate the time to inform all subordinates
        def dfs_method(employee: int) -> int:
            # Base case: if the employee has no subordinates, return 0
            if employee not in subordinate:
                return 0

            # Variable to store the maximum time taken by any subordinate
            max_time = 0

            # Recursively calculate the time for each subordinate and keep track of the maximum time
            for s in subordinate[employee]:
                max_time = max(max_time, dfs_method(s))

            # The total time to inform all subordinates of this employee is the employee's inform time
            # plus the maximum time taken by any of its subordinates
            return informTime[employee] + max_time

        # Start the DFS from the head of the company (headID)
        return dfs_method(headID)
"""
TIME COMPLEXITY: O(n)
1. where n is the number of employee
2. Each employee is visited once during DFS traversal

SPACE COMPLEXITY: O(n)
1. for the recursion stack in the worst case (if the tree is a straight line),
and for storing the adjacency list


"""