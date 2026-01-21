class Solution:
    def threeSum(self, nums):
        sorted_nums=sorted(nums)
        output=[]
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            
            while(l<r):
                sum=sorted_nums[i]+sorted_nums[l]+sorted_nums[r]
                if(sum==0):
                    if([sorted_nums[i],sorted_nums[l],sorted_nums[r]] not in output):
                        output.append([sorted_nums[i],sorted_nums[l],sorted_nums[r]])
                    l+=1
                    r-=1
                elif(sum<0):
                    l+=1
                else:
                    r-=1
        return output