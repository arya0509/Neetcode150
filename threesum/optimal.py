class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sorted_nums=sorted(nums)
        output=[]
        for i in range(len(nums)-2):
            if(sorted_nums[i]>0):
                print('this breaks')
                break

            if(sorted_nums[i]==sorted_nums[i-1] and i!=0):
                continue
            l=i+1
            r=len(nums)-1
            
            while(l<r):
                sum=sorted_nums[i]+sorted_nums[l]+sorted_nums[r]
                if(sum==0):
                    
                    output.append([sorted_nums[i],sorted_nums[l],sorted_nums[r]])
                    l+=1
                    r-=1

                    while(sorted_nums[l]==sorted_nums[l-1] and l<r):
                        l+=1
                elif(sum<0):
                    l+=1
                else:
                    r-=1
        return output 
    
sol=Solution()
print(sol.threeSum([0,0,0]))