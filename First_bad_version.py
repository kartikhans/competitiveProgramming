def firstBadVersion(n):
        l=1
        r=n
        if(n==1):
            return(1)
        while(l<=r):
            if(r-l==1):
                if(isBadVersion(l)==True):
                    return(l)
                return(r)
            mid = l+(r-l)//2
            if(isBadVersion(mid)==True):
                r=mid
            elif(isBadVersion(mid)==False):
                l=mid