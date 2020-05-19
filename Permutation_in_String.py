def checkInclusion(s1,s2):
        arr=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        flip=1
        for i in s1:
            flip*=arr[ord(i)-97]
        arr2=s2[:len(s1)]
        gap=1
        for i in arr2:
            gap*=arr[ord(i)-97]
        para=0
        if(gap==flip):
            return(True)
        for i in range(len(s1),len(s2)):
            gap=gap//arr[ord(s2[para])-97]
            para+=1
            gap*=arr[ord(s2[i])-97]
            if(gap==flip):
                return(True)
        return(False)