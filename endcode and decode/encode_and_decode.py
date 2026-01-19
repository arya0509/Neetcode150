class Solution:

    def encode(self, strs):

        size=[]
        output=""
        for word in strs:
            size.append(len(word))

        for i in size:
            output+=str(i)+","
        output+="#"

        for word in strs:
            output+=word
        
        return output 
            
    def decode(self,  s) :
        size=[]
        output=[]

        index=0

        while(s[index]!='#'):
            num=''
            while(s[index]!=','):
                num+=s[index]
            size.append(int(num))
        index+=1

        for sz in size:
            output.append(s[index:sz+index])
            index+=sz
                    
        return output


           
           
        

sol=Solution()

print((sol.encode(["Hello","World"])))