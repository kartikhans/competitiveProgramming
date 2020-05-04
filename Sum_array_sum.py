from collections import defaultdict
def subArraySum(nums,k):
        dicti = defaultdict(int)
        res = 0
        
        curr = 0
        n=len(nums)
        for i in range(n):
            curr+=nums[i]
            if(curr == k):
                res+=1
            if curr-k in dicti:
                res+=dicti[curr-k]
            
            dicti[curr]+=1
            
        return(res)