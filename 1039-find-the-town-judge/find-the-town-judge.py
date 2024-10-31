from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # STEP - 1: Handle an edge case where there is only one person in the town.
        # If n is 1, they are the judge by default (if trust list is empty or incomplete).
        if n == 1 and not trust:
            return 1
        
        # STEP - 2: Initialize two counters for each person to track:
        # - 'indegree': the number of people who trust them.
        # - 'outdegree': the number of people they trust.
        # We add 1 to size due to 1-based indexing.
        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)

        # STEP - 3: Process the trust relationships.
        # For each pair (a, b), person 'a' trusts person 'b':
        for a, b in trust:
            outdegree[a] += 1  # Person 'a' trusts someone (increase their outdegree).
            indegree[b] += 1    # Person 'b' is trusted by 'a' (increase their indegree).

        # STEP - 4: Find the judge.
        # A judge would have indegree == n - 1 (trusted by everyone else)
        # and outdegree == 0 (they trust no one).
        for i in range(1, n + 1):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i  # Return the judge's label.

        # STEP - 5: Edge case where no judge is found (no one meets the conditions).
        return -1

# TIME COMPLEXITY:
# - Processing the trust list takes O(m), where m is the length of the trust list.
# - Checking each person's indegree and outdegree takes O(n), where n is the number of people.
# - Overall, the time complexity is O(n + m).

# SPACE COMPLEXITY:
# - We use two lists of size n + 1 for indegree and outdegree, leading to O(n) space complexity.
