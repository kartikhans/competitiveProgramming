def removeDuplicates(nums):
        if(nums==[]):
            return(0)
        prev=nums[0]
        count=1
        for i in range(len(nums)):
            if(nums[i]!=prev):
                prev=nums[i]
                (nums[count],nums[i])=(nums[i],nums[count])
                count+=1
        return(count)