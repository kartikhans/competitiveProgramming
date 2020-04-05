def maxProfit(prices):
        profit=0
        n=len(prices)
        for i in range(n-1):
            if(prices[i+1]-prices[i]>0):
                profit+=prices[i+1]-prices[i]
        return(profit)