class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        # STEP - 1: Reverse the graph that tracks the incoming edges
        reversed_graph = defaultdict(list)
        # print(reversed_graph)
        # Array to store the number of outgoing edges for each node
        outdegree = [0] * n

        for node in range(n):
            # For each outgoing edge from 'node
            for neighbor in graph[node]:
                # Add 'node' as an incoming edge to 'neighbor'
                reversed_graph[neighbor].append(node)
                # print(reversed_graph)
            # Count the number of outgoing edges for 'node'
            outdegree[node] = len(graph[node])
            # print(outdegree)
        
        # STEP - 2: Initialize the queue with terminal node (outdegree = 0)
        queue = deque([i for i in range(n) if outdegree[i] == 0])

        # STEP - 3: Perform BFS to find all safe nodes
        safe_nodes = []

        while queue:
            # Process the next node in the queue
            node = queue.popleft()
            # print(node)
            # Mark the node as safe
            safe_nodes.append(node)
            # print(safe_nodes)

            # Process all neighbors of the node in the reversed graph
            for neighbor in reversed_graph[node]:
                # Decrease the outdegree of the neighbor
                outdegree[neighbor] -= 1
                # If the neighbor becomes a terminal node
                if outdegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # STEP - 4: Return the sorted list of safe nodes
        return sorted(safe_nodes)

"""
TIME COMPLEXITY: O(V + E + VlogV)
1. where V -> is the number of nodes, E -> number of edges
2. BFS Traversal: O(V + E)
3. Sorting the result: O(V log V)
4. Overall: O(V + E + VlogV)

SPACE COMPLEXITY: O(V + E)
1. Reversed graph storage: O(V + E)
2. Queue: O(V)
3. Outdegree array: O(V)
4. Overall: O(V + E)
"""



