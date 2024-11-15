class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # To count the numbers of tasks
        count = Counter(tasks)
        # To store in descending order we have to negate the values
        # because heap stores by default in ascending order
        # List comprehension is used to traverse the values because we wont be considering characters
        # But we will be counting the characters and negating their values
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        # Time variable to track the time
        time = 0
        q = deque()     # We are going to stores values in this way [-cnt, idletime]
        while maxHeap or q:
            # Each loop we are going to increment the time
            time += 1
            if maxHeap:
                # Because we are processing the task, so we reduce it by 1 as we are done executing it
                cnt = 1 + heapq.heappop(maxHeap)
                # Until the count is non-zero, we will append it to 1
                if cnt:
                    # Since when we consider time i.e 
                    # We consider the time when we executed + the interval
                    # Therefore, when we append we append (time + n)
                    q.append([cnt, time + n]) 
            # If our queue is non empty and our time has just reached current time
            if q and q[0][1] == time:
                # As we our implementing deque
                # because we care about the count (cnt), we will be getting that
                heapq.heappush(maxHeap, q.popleft()[0])
        # As we are interested in the time it took to execute the operation
        return time 
        # Time complexity: O(n*m) -> As we have 26 characters (n elements ), idle time (n) -> used as m
