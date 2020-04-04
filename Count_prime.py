def isPrime(n):
        
        prime = [True for i in range(n+1)]
        
        x = 2
        while(x**2<=n):
            if(prime[x]==True):
                for i in range(2*x,n+1,x):
                    prime[i]=False
            x+=1
        
        count=0
        for i in range(2,n):
            if(prime[i]==True):
                count+=1
        return (count)