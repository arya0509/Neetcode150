class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX=0x7fffffff
        sign=-1 if x<0 else 1
        x=x*sign
        res=0
        while(x):
            d=x%10
            x=x//10
            if(res>MAX//10 or (res==MAX//10 and d>MAX%10)):
                return 0
            res=res*10 +d
        return res *sign
            
            