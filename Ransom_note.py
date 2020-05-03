def canContruct(ransomNote, magazine):
	dicti = defaultdict(int)
        for i in magazine:
            dicti[i]+=1
        for i in ransomNote:
            if(dicti[i]==0):
                return(False)
            dicti[i]-=1
        return(True)