class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        cache=[]
        ROWS=(m)-1
        COLS=(n)-1
        for r in range(ROWS):
            ls=[]
            for c in range(COLS):
                ls.append(-1)
            cache.append(ls)
        def dfs(r,c):
            if(r>ROWS or c>COLS):
                return 0
            if(r==ROWS and c==COLS):
                return 1
            if(cache[r][c]!=-1):
                return cache[r][c]

            cache[r][c]= dfs(r,c+1)+cache(r+1,c)
        return dfs(0,0)

