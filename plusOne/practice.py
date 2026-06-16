class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry=1
        res=[]
        for i in range(len(digits)-1,-1,-1):
            curr=digits[i]
            sum=curr+carry
            if(sum>9):
                dig=sum%10
                res.append(dig)
                carry=sum//10
            else:
                res.append(sum)
                carry=0
        if carry:
            return [1]+res[::-1]
        a=10
        
        return res[::-1]