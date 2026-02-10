 l=0
        r=len(nums)-1

        while(l<=r):
            mid=(l+r)//2

            if(nums[mid]==target):
                return mid
            if(nums[l]==target):
                return l
            elif(nums[mid]>target and nums[r]<=target):
                if(nums[r]==target):
                    return r
                l=mid+1
                continue
            r=mid-1
        
        return -1