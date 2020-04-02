def firstUniqChar(s):
        maps = {}
        for i in s:
            if i not in maps:
                maps[i]=1
            else:
                maps[i]+=1
        for i in range(len(s)):
            if(maps[s[i]]==1):
                return(i)
        return(-1)



print(firstUniqChar("kartik"))