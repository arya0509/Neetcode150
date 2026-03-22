from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj=defaultdict(list)
        completed=set()
        visited=set()
        for course in prerequisites:
            adj[course[0]].append(course[1])
        
        def dfs(course):
            if(course in visited):
                return False
            if(course not in adj) or course in completed:
                completed.add(course)
                return True
            visited.add(course)
            for courses in adj[course]:
                if(not dfs(courses)):
                    return False
            visited.remove(course)
            completed.add(course)
            return True
        for i in range(numCourses):
            
            if not dfs(i):
                return False
        return True 