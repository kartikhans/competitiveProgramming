def missingNumber(nums):
        n=len(nums)
        arr=[0]*(n+1)
        for i in nums:
            arr[i]=1
        for i in range(n+1):
            if(arr[i]==0):
                return(i)