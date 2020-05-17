def findAnagrams(s,p):
        arr=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        mull=1
        for i in p:
            mull*=arr[(ord(i)-97)]
        kappa=s[:len(p)]
        flip=1
        for i in kappa:
            flip*=arr[ord(i)-97]
        ans=[]
        if(flip==mull):
            ans.append(0)
        jam=0
        for i in range(len(p),len(s)):
            flip=flip//arr[ord(s[jam])-97]
            flip*=arr[ord(s[i])-97]
            jam+=1
            if(flip==mull):
                ans.append(jam)
        return(ans)