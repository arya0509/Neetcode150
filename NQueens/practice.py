class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res=[]
        combination=[]
        for row in range(n):
            temp=[]
            for col in range(n):
                temp.append(".")
            combination.append(temp)
           
        def backtracking(row):
            if(row==n):
                temp=[]
                for row in combination:
                    temp.append("".join(row))
                res.append(temp)
                print(res)
                return
            for c in range(n):
                if(isValid(row,c,combination)):
                    combination[row][c]="Q"
                    backtracking(row+1)
                    combination[row][c]="."
        def isValid(row,col,combination):
            r=row
            while(r>=0):
               
                if(combination[r][col]=="Q"):
                    return False
                r-=1
            r,c=row,col
            while(r>=0 and c>=0):
               
                if(combination[r][c]=="Q"):
                    return False
                r-=1
                c-=1
            r,c=row,col
            while(r>=0 and c<len(combination[0])):
                
                if(combination[r][c]=="Q"):
                    return False
                r-=1
                c+=1
            return True
        backtracking(0)
    
            
        return res
            

