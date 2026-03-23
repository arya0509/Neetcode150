from collections import defaultdict
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj=defaultdict(list)
        for course in prerequisites:
            adj[course[0]].append(course[1])
        visited=set()
        completed=set()
        res=[]

        def dfs(course):
            if course in visited:
                return False
            if course in completed:
                return True  
            if course not in adj:
                res.append(course)
                completed.add(course)
                return True
           
            visited.add(course)
            for c in adj[course]:
                if( not dfs(c)):
                    return False
            completed.add(course)
            res.append(course)
            visited.remove(course)
            return True
        for i in range(numCourses):
            if(not dfs(i)):
                return []
        return res
        

        