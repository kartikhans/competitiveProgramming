def firstMissingPositive(nums):
        posi=1
        dicti=defaultdict(int)
        for i in nums:
            dicti[i]+=1
        while(1):
            if(dicti[posi]==0):
                return(posi)
            else:
                posi+=1
        return(posi)