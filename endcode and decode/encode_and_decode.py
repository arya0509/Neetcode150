class Solution:

    def encode(self, strs):
       
        if not strs:
            return ''
        output=""
        for size in strs:
            output+=str(len(size))+','
        output+="#"

        for words in strs:
            output+=words
        
        return output 


    def decode(self,  s) :
       
        if not s:
            return [ ]
        sizes=[]
        output=[]
        i=0
        while(s[i]!="#"):
            num=''
            while(s[i]!=','):
                num+=s[i]
                i+=1
            sizes.append(int(num))
            i+=1
        i+=1
        
        for size in sizes:
            output.append(s[i:i+size])
            print('We are here')
            i+=size

        return output 

sol=Solution()
print(sol.decode(sol.encode(["",""])))