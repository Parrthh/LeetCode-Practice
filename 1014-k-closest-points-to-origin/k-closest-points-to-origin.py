class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Empty list that will store the points along with their squared distance
        minHeap = []
        # To traverse the input list
        for x,y in points:
            # Squaring the distance
            dist = (x ** 2) + (y ** 2)
            # Appending the distance and the points in the form a list into minHeap
            minHeap.append([dist, x, y])
        # This function converts the minHeap list into a min-heap
        # A min-heap is binary tree like data structure where the smallest elements
        # is always at the root (the first element of the heap)
        # After using this function the minHeap will be stored in ascending order
        heapq.heapify(minHeap)
        # Empty list that will store the final "k" closest points
        res = []
        while k > 0:
            # This operation pops the smallest elements from the minHeap
            dist, x, y = heapq.heappop(minHeap)
            # Appending them into the final result list
            res.append([x,y])
            # Decrementing the value of k, until it gets 0
            k -= 1
        return res
