def canJump(nums):
        if(len(nums)<=1):
            return(True)
        maxi=nums[0]
        for i in range(len(nums)):
            if(maxi<=i and nums[i]==0):
                return(False)
            if(i+nums[i]>maxi):
                maxi=i+nums[i]
            if(maxi>=len(nums)-1):
                return(True)
        return(False)