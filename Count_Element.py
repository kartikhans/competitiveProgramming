def countElement(arr):
        dicti = defaultdict(int)
        counter=0
        for i in arr:
            dicti[i]+=1
        for i in arr:
            if(dicti[i+1]>0):
                counter+=1
        return(counter)