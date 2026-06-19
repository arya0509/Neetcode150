class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if(num1=="0" or num2=="0"):
            return "0"
        res=""
        zero=0
        for i  in range(len(num2)-1,-1,-1):
            prod=self.mul(num1,num2[i],zero)
            res=self.addition(res,prod)
            zero+=1
        return res 
            

    def mul(self,num,n,zero):
        carry=0
        n=int(n)
        res=""
        for i in range(len(num)-1,-1,-1):
            prod=(int(num[i]) * n) + carry
            carry=0
            if(prod>9):
                carry=prod//10
                prod=prod%10
            res+=str(prod)
        if(carry):
            res+=str(carry)
        return res[::-1] + ("0"*zero)
    def addition(self,n1,n2):
        carry=0
        res=""
        while(a>=0 or b>=0):
            num1=int(n1[a]) if a>=0 else 0
            num2=int(n2[b]) if b>=0 else 0
            s=num1+num2+carry
            carry=0
            if(s>9):
                carry=s//10
                s=s%10
            
            res+=str(s)
            a-=1
            b-=1
        
        if(carry):
            res+=str(carry)
        sum=res[::-1]
        return sum

                

        