class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort the people list
        # - Sort by height in descending order (-x[0] ensures taller people are placed first)
        # - For people with the same height, sort by k value in ascending order (x[1])
        people.sort(key=lambda x: (-x[0], x[1]))

        # Step 2: Initialize an empty list to represent the queue
        queue = []

        # Step 3: Iterate through the sorted list and place each person in the queue
        for person in people:
            # Insert the person at the index equal to their k value
            # - The k value specifies the number of people taller or equal to the person
            #   who should stand in front of them
            queue.insert(person[1], person)

        # Step 4: Return the reconstructed queue
        return queue

"""
TIME COMPLEXITY: O(n log n)
1. where n is the number of people
2. Each insertion into the queue takes O(n) in the worst case (shifting elements)
3. For n people, the total insertion cost is O(n ^ 2)

SPACE COMPLEXITY: O(n)
1. For the output queue
"""