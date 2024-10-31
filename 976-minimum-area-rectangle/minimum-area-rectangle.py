from typing import List

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # Step 1: Convert points to a set for fast lookup
        # We use set(map(tuple, points)) to store each point as a tuple in a set.
        # This allows O(1) average time complexity for checking if a point exists.
        point_set = set(map(tuple, points))
        
        # Initialize min_area to infinity. This variable will store the minimum area found.
        # If no rectangle is found, we will return 0.
        min_area = float('inf')
        
        # Step 2: Iterate over all pairs of points to identify potential diagonals of rectangles
        # We use two nested loops to examine each unique pair of points.
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                # Unpack coordinates of the two points in the pair
                x1, y1 = points[i]
                x2, y2 = points[j]

                # Check if points (x1, y1) and (x2, y2) can form a diagonal
                # To form a diagonal of a rectangle, the points must have different x and y coordinates.
                if x1 != x2 and y1 != y2:
                    # Step 3: Check for the other two points needed to complete the rectangle
                    # Specifically, we need (x1, y2) and (x2, y1) to exist in the set.
                    # If both points exist, (x1, y1) and (x2, y2) form a valid diagonal.
                    if (x1, y2) in point_set and (x2, y1) in point_set:
                        # Step 4: Calculate the area of the rectangle formed by this pair
                        # The area of the rectangle is the absolute difference in x-coordinates
                        # multiplied by the absolute difference in y-coordinates.
                        area = abs(x2 - x1) * abs(y2 - y1)
                        
                        # Update min_area if we find a smaller area
                        min_area = min(min_area, area)

        # Step 5: Return the result
        # If min_area is still infinity, it means no rectangle was found, so we return 0.
        # Otherwise, we return the minimum area found.
        return min_area if min_area != float('inf') else 0

# TIME COMPLEXITY: O(N^2)

#We use two nested loops to iterate over each unique pair of points, which gives us O(n^2)
# For each pair of points, checking if (x1,y2) and (x2,y1) exist in point_set takes O(1) on average, due to the set lookup.
# Therefore, the total time complexity is dominated by the nested loop, resulting in O(n^2).

# SPACE COMPLEXITY: O(N)

# We store all points in a set, which requires O(n) space, where n is the number of points.
#Other variables (such as min_area and loop variables) use constant space.
#Therefore, the overall space complexity is O(n).

