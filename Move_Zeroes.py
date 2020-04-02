def moveZeroes(nums):
        place=len(nums)-1
        i=0
        while(i<place):
            if(nums[i]==0):
                for m in range(i,place):
                    nums[m],nums[m+1]=nums[m+1],nums[m]
                place-=1       
            else:
                i+=1