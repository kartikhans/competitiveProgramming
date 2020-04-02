def twoSum(nums, target):
        maps={}
        for i in range(len(nums)):
            maps[nums[i]]=i
        for i in range(len(nums)):
                if(target-nums[i] in maps and i!=maps[target-nums[i]]):
                    return(i, maps[target-nums[i]])