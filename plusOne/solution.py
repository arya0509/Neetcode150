class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n=""
        for i in digits:
            n+=str(i)
        sum=int(n)+1
        res=[]
        for i in str(sum):
            res.append(i)
        return res 