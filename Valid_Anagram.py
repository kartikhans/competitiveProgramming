from collections import defaultdict

def validAnagram(s,t):
        dicti = defaultdict(int)
        for i in s:
            dicti[i]+=1
        if(len(s)!=len(t)):
            return(False)
        for i in t:
            if(dicti[i]==0):
                return(False)
            dicti[i]-=1
        return(True)