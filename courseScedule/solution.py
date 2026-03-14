from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        courseDict=defaultdict(list)
        for course in prerequisites:
            courseDict[course[0]].append(course[1])
        path=set()
        completed=set()
        def dfs(course):
            if(course not in courseDict):
                completed.add(course)
                return True
            if(course in path):
                return False
            if(course in completed):
                return True 
            path.add(course)
            for c in courseDict[course]:
                if(not dfs(c)):
                    path.remove(course)
                    return False
            path.remove(course)
            completed.add(course)
            return True
        for id in range(numCourses):
            if(not dfs(id)):
                return False
        return True
        