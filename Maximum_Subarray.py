def maxSubArray(nums):
        n=len(nums)
        global_max = nums[0]
        maxi = nums[0]
        
        for i in range(1,n):
            if(maxi+nums[i]>nums[i]):
                maxi+=nums[i]
            else:
                maxi = nums[i]
            
            if(global_max<maxi):
                global_max = maxi
        return(global_max)