class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initializing an empty list
        result = []
        # Loop through each row
        for row_num in range(numRows):
            # Create a row with appropriate number of elements
            r = [None for _ in range(row_num+1)]
            # Set the first and last element to 1
            r[0],r[-1] = 1,1
            # Fill in the middle elements
            for j in range(1,len(r) - 1):
                r[j] = result[row_num - 1][j-1] + result[row_num - 1][j]
            result.append(r)

        return result


