class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sortedList=sorted(nums)
        output=[]
        i=0
        while(i<len(sortedList)-2):
            while(i!=0 and sortedList[i]==sortedList[i-1]):
                i+=1
                if(i==len(sortedList)-2):
                    break
            print(f"index: {i}  element: {sortedList[i]}")

            l=i+1
            r=len(nums)-1

            while(l<r):
                sum=sortedList[i] +sortedList[l]+sortedList[r]

                if(sum==0):
                    output.append([sortedList[i],sortedList[l],sortedList[r]])
                    l+=1
                    r-=1

                    while(l<r and sortedList[l]==sortedList[l-1]):
                        l+=1
                    while(l<r and sortedList[r]==sortedList[r+1]):
                        r-=1
                
                elif(sum>0):
                    r-=1
                else:
                    l+=1
            i+=1
        return output

sol=Solution()
print(sol.threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]))