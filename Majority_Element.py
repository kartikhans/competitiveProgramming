def majorityElement(nums):
        result=0
        count=0
        for i in nums:
            if(count==0):
                result=i
                count+=1
            elif(i==result):
                count+=1
            else:
                count-=1
        return(result)