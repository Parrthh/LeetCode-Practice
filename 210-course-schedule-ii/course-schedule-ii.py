class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        list_prereq = { i: [] for i in range(numCourses)}

        for c,p in prerequisites:
            list_prereq[c].append(p)
        final_output = []
        visited_node,cyclic_node = set(), set()

        def dfs_method(c):
            if c in cyclic_node:
                return False
            if c in visited_node:
                return True
            cyclic_node.add(c)
            for p in list_prereq[c]:
                if dfs_method(p) == False:
                    return False
            cyclic_node.remove(c)
            visited_node.add(c)
            final_output.append(c)
            return True

        for c in range(numCourses):
            if dfs_method(c) == False:
                return []
        return final_output


            