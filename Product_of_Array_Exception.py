def productExceptSelf(nums):
        arr=[]
        cap=[]
        sam=1
        for i in nums:
            arr.append(sam)
            sam*=i
        sam=1
        for i in range(len(nums)-1,-1,-1):
            cap.append(sam)
            sam*=nums[i]
        cap.reverse()
        ret=[]
        for i in range(len(nums)):
            ret.append(arr[i]*cap[i])
        return(ret)