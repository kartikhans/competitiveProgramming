def containsDuplicate(nums):
        maps={}
        for i in range(len(nums)):
            if nums[i] not in maps:
                maps[nums[i]]=i
            else:
                return(True)
        return(False)