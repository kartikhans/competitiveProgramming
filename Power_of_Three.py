def isPowerOfThree(n):
        if(n<=0):
            return(False)
        x = math.log(n,3)
        print(x)
        if(x%1==0 or 1-x%1<0.0000000000001):
            return(True)
        else:
            return(False)