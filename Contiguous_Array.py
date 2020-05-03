def findMaxLength(nums):
        arr=[]
        count=0
        for i in nums:
            if(i==0):
                count-=1
            else:
                count+=1
            arr.append(count)
        dicti=defaultdict(list)
        high=0
        for i in range(len(arr)):
            dicti[arr[i]].append(i)
        for i in range(len(arr)):
            if(arr[i]==0):
                if(high<i+1):
                    high=i+1
            else:
                if(len(dicti[arr[i]])!=1):
                    if(dicti[arr[i]][-1]-dicti[arr[i]][0]>high):
                        high = dicti[arr[i]][-1]-dicti[arr[i]][0]
        return(high)
