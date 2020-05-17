def findJudge(N, trust):
        arr=[0]*(N+1)
        for i in trust:
            arr[i[0]]-=1
            arr[i[1]]+=1
        for i in range(1,N+1):
            if(arr[i]==N-1):
                return(i)
        return(-1)