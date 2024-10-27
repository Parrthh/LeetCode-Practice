class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Mapping all the courses in dict
        list_prereq = {i: [] for i in range(numCourses)}
        # For every course append their prerequisite
        for c,p in prerequisites:
            list_prereq[c].append(p)
        # Initialize an empty set to track the visited nodes
        visited_node = set()

        def dfs_method(c):
            # If course is already present in the visited node -> return False
            if c in visited_node:
                return False
            # If the course has no prerequisites -> return True
            if list_prereq[c] == []:
                return True
            # If all the above cases dont match add it into the visited node set
            visited_node.add(c)
            # For every prerquisite for a course, implement dfs, if cannot perform -> return False
            for p in list_prereq[c]:
                if not dfs_method(p):
                    return False
            # If the loop is executed that means the course can be done
            # Therefore, remove it from the visited nodes
            visited_node.remove(c)
            # Set the course as the prereq is not required, as it is completed
            # This means the course has been fully processed
            list_prereq[c] = [] # Clear the prerequisite to mark as completed
            return True
        # Run DFS implementation on each course
        for c in range(numCourses):
            # If the loop cannot be executed based on the edge cases -> return False
            if not dfs_method(c):
                return False
        # If everything works out return True
        return True
