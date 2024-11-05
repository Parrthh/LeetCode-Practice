class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # Step 1: Sort logs by timestamp to process them in chronological order
        logs = sorted(logs, key=lambda x: x[0])
        
        # Step 2: Initialize a graph with each person as a set, using a defaultdict
        graph = collections.defaultdict(set)
        
        # Step 3: Initialize each person in their own set
        for i in range(n):
            graph[i].add(i)
        
        # Step 4: Process each log entry to merge friend groups
        for timestamp, person1, person2 in logs:
            # Merge the sets of person1 and person2
            graph[person1] = graph[person1].union(graph[person2])
            for person in graph[person1]:
                graph[person] = graph[person1]  # Update each person's group reference

            # Check if all persons are in the same group
            if len(graph[person1]) == n:
                return timestamp
        
        # If not all are connected by the end of the logs, return -1
        return -1