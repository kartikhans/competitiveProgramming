def lastStoneWeight(stones):
        if(len(stones)==0):
            return(0)
        elif(len(stones)==1):
            return(1)
        while(len(stones)>1):
            stones.sort()
            s1=stones[-1]
            s2=stones[-2]
            if(s1==s2):
                stones.pop(-1)
                stones.pop(-1)
            else:
                s2=abs(s1-s2)
                stones.pop(-1)
                stones[-1]=s2
        if(len(stones)==1):
            return(stones[-1])
        return(0)