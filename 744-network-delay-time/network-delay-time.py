class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Step 1: Build the graph using an adjacency list
        # Each node u has a list of tuples (v, w) where:
        # - v is the destination node
        # - w is the time it takes to travel from u to v
        # Time Complexity for building the graph: O(E), where E is the number of edges

        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        
        # Step 2: Initialize a min-heap (priority queue) for Dijkstra's algorithm
        # Start with the source node `k`, with a travel time of 0
        # `minHeap` stores tuples of (current travel time, current node)
        # This allows us to always process the node with the shortest travel time first
        
        minHeap = [(0, k)]  # (time to reach node, node)
        
        # `visited_nodes` keeps track of nodes we've processed (i.e., confirmed shortest time to reach)
        # Space Complexity of visited_nodes set: O(V), where V is the number of nodes
        visited_nodes = set()
        
        # `res` will store the maximum time it takes to reach any node from the source node `k`
        # This is our result, as we need the time when the last node receives the signal
        res = 0

        # Step 3: Process the min-heap until it's empty (Dijkstra's algorithm)
        # Time Complexity of Dijkstra's algorithm: O((E + V) * log V), due to heap operations
        while minHeap:
            # Extract the node with the shortest current travel time
            w1, n1 = heapq.heappop(minHeap)  # w1 is time to reach n1
            
            # If we've already visited this node, skip it
            # This ensures that each node is only processed once, which is important for efficiency
            if n1 in visited_nodes:
                continue
            
            # Mark this node as visited
            visited_nodes.add(n1)
            
            # Update the maximum time taken to reach any node so far
            res = max(res, w1)
            
            # Step 4: Explore all neighbors of the current node `n1`
            # For each neighbor `n2` of `n1`, `w2` is the travel time from `n1` to `n2`
            for n2, w2 in edges[n1]:
                # If the neighbor `n2` has not been visited, calculate the travel time to `n2`
                if n2 not in visited_nodes:
                    # Push the neighbor onto the heap with the updated travel time (w1 + w2)
                    # `w1 + w2` is the time to reach `n2` from `k` via `n1`
                    heapq.heappush(minHeap, (w1 + w2, n2))
        
        # Step 5: Check if all nodes have been visited
        # If the number of visited nodes is equal to `n`, return `res`, which is the time taken to reach all nodes
        # Otherwise, return -1, indicating that not all nodes are reachable from `k`
        return res if len(visited_nodes) == n else -1

"""
TIME COMPLEXITY: O((E+V)log V)
1. Building the graph takes O(E), where E is number of edges
2. Each node can be added to minHeap once, and we may process each edge once, 
    so the while-loop process O(E + V) elements
3. Each "heappop" and "heappush" operation takes O(logV) leading to a total time complexity of O((E+V) logV)


SPACE COMPLEXITY: O(E + V)
1. The adjacency list edges requires O(E) space
2. The "visited_nodes" set and "minHeap" priority queue require O(V) space
3. Thus, the total space complexity is O(E+V)
"""