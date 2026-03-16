from collections import defaultdict
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        completed=[]
        res=set()
        path=set()
        courses=defaultdict(list)
        for course in prerequisites:
            courses[course[0]].append(course[1])
        
        def dfs(course):
            if(course in res):
                return True
            if(course not in courses):
                if(course not in res):
                    res.add(course)
                    completed.append(course)
                return True
            
            if(course in path):
                return False
            path.add(course)

            for c in courses[course]:
                if(not dfs(c)):
                    path.remove(course)
                    return False
            path.remove(course)
            completed.append(course)
            res.add(course)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return completed
