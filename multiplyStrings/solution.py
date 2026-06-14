class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=="0" or num2=="0":
            return "0"
        res=0
        padding=0
        for i in range(len(num2)-1,-1,-1):
            prod=self.mul(num1,num2[i],padding)
            res=self.sum(prod,res)
            padding+=1
        return res
    def mul(self,num1,digit,zero):
        carry=0
        res=[]
        d=int(digit)
        i=len(digit)-1
        while(i>=0 or carry):
            n=int(num1[i]) if i>=0 else 0
            prod=n*d+carry
            res.append(str(prod%10))
            carry=prod//10
        return "".join(res[::-1])+"0"*zero
    def sum(self,num1,num2):
        carry=0
        i=len(num1)
        j=len(num2)
        res=[]
        while(i>=0 or j>=0 or carry):
            n1=int(num1[i]) if i>=0 else 0
            n2=int(num2[j]) if j>=0 else 0
            s=n1+n2+carry
            res.append(str(s%10))
            carry=s//10
            i-=1
            j-=1
        return "".join(res[::-1])

        
