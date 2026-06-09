class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry=1
        for i in range(len(digits)-1,-1,-1):
            sum=digits[i]+carry
            if(sum>9):
                carry=sum//10
                sum=sum%10
            else:
                carry=0
            digits[i]=sum
        return digits
