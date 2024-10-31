from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Sorts an array of integers using merge sort.
        
        Time Complexity: O(n log n) - where n is the number of elements in the array.
            - The array is repeatedly split in half (log n times) and then each split array is merged (O(n) time).
        Space Complexity: O(n) - Auxiliary space used for temporary storage during the merge process.
        
        :param nums: List[int] - The input array of integers.
        :return: List[int] - The sorted array.
        """
        def merge_sort(arr):
            # Base case: If the array has 1 or 0 elements, it is already sorted.
            if len(arr) <= 1:
                return arr

            # Step 1: Divide the array into two halves.
            mid = len(arr) // 2
            left_arr = arr[:mid]   # Left half of the array.
            right_arr = arr[mid:]  # Right half of the array.

            # Step 2: Recursively sort both halves.
            left_sorted = merge_sort(left_arr)
            right_sorted = merge_sort(right_arr)

            # Step 3: Merge the two sorted halves.
            return merge(left_sorted, right_sorted)

        def merge(left, right):
            """
            Merges two sorted arrays into a single sorted array.
            
            Time Complexity: O(n) - where n is the sum of the lengths of left and right arrays.
            Space Complexity: O(n) - Auxiliary space used for storing the merged array.
            
            :param left: List[int] - The left sorted array.
            :param right: List[int] - The right sorted array.
            :return: List[int] - The merged sorted array.
            """
            sorted_arr = []  # Temporary array to store merged elements.
            i = j = 0  # Pointers for the left and right arrays.

            # Step 1: Compare elements from both arrays and merge in sorted order.
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    # Append the smaller element to the sorted array.
                    sorted_arr.append(left[i])
                    i += 1  # Move the pointer for the left array.
                else:
                    sorted_arr.append(right[j])
                    j += 1  # Move the pointer for the right array.

            # Step 2: Append any remaining elements from the left array.
            while i < len(left):
                sorted_arr.append(left[i])
                i += 1

            # Step 3: Append any remaining elements from the right array.
            while j < len(right):
                sorted_arr.append(right[j])
                j += 1

            # Step 4: Return the merged and sorted array.
            return sorted_arr

        # Call the merge_sort function on the input array.
        return merge_sort(nums)
