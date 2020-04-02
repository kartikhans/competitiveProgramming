from collections import Counter

def singleNumber(nums):
	s=Counter(nums)
	print(s)
    for i in s.items():
    	if(i[1]==1):
        	return(i[0])

print(singleNumber([4,1,2,1,2]))